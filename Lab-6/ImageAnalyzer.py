import ast
import base64
import os
from collections import Counter
from venv import logger

import googleapiclient.discovery
import tweepy
from tweepy import OAuthHandler, api
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import sys
import boto3
import plotly.plotly as py
import plotly.graph_objs as go

py.plotly.tools.set_credentials_file(username = os.environ.get('PLOTLY_USERNAME'), api_key = os.environ.get('PLOTLY_KEY'))

TAG_TABLE = 'twitter-images'
AWS_REGION = 'eu-west-1'


def get_image_from_tweet(status):
    a=json.loads(status)
    media_list = list()  # in case a single tweet contains more than one image
    if 'extended_entities' in a:
        for media in a['extended_entities']['media']:
            if 'media' in a['extended_entities'] and media['type'] == 'photo':
                image_uri = media['media_url']
                media_list.append(image_uri)
    else:
        pass

    return media_list


def get_tags(image_uri):
    """Run a label request on a single image"""

    # [START authenticate]
    service = googleapiclient.discovery.build('vision', 'v1')
    # [END authenticate]

    # [START construct_request]
    service_request = service.images().annotate(body={
        "requests": [
            {
                "image": {
                    "source": {
                        "imageUri": image_uri
                    }
                },
                'features': [{
                'type': 'LABEL_DETECTION'
            }]
        }]
    })
    # [END construct_request]

    # [START parse_response]
    try:
        response = service_request.execute()
        print("Results for image: " + image_uri)
        for result in response['responses'][0]['labelAnnotations']:
            print("%s - %.3f" % (result['description'], result['score']))
        return response
    except Exception as e:
        return None
    # [END parse_response]

def tags_to_json(tags_response):
    data = []
    item = {}
    if(tags_response):
        for result in tags_response['responses'][0]['labelAnnotations']:
            item[result['description']] = str(result['score'])
        data.append(item)
        jsonData = json.dumps(data)
        return jsonData
    return None

def get_tweets_from_db():
    try:
        dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
        table = dynamodb.Table('twitter-images')
    except Exception as e:
        logger.error(
            'Error connecting to database table: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args))
        return None

    response = table.scan(
        ReturnConsumedCapacity='TOTAL',
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return response['Items']
    logger.error('Unknown error retrieving items from database.')
    return None

def plot_tags():

    tweets = get_tweets_from_db()
    tag_scores = {}
    for tweet in tweets:
        tweet_tags_dict = json.loads(tweet['tags'])
        for tag,score in tweet_tags_dict[0].items():
            if not tag in tag_scores:
                tag_scores[tag] = float(score)
            else:
                tag_scores[tag] += float(score)

    for k,v in tag_scores.items():
        print(k + ": " + str(v) + '\n')

    top = Counter(tag_scores)
    top = dict(top.most_common(20))

    data = [go.Bar(
        x=list(top.keys()),
        y=list(top.values())
    )]
    layout=dict(
        tickangle=45
    )


    py.plot(data, filename='basic-bar',layout=layout)


class TwitterListener():

    image_counter = 0

    def __init__(self):
        dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
        try:
            self.table = dynamodb.Table(TAG_TABLE)
        except Exception as e:
            print('\nError connecting to database table: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args))
            sys.exit(-1)

    def get_tweets(self, data):
        tweet = json.dumps(data)
        a=json.loads(tweet)

        image_list = get_image_from_tweet(tweet)
        tags_response = ""
        for image in image_list:
            # Check if we gathered 100 images already
            self.image_counter += 1
            if (self.image_counter > 100):
                break

            tags_response = get_tags(image)

            # Convert tags to JSON
            tags_json = tags_to_json(tags_response)

            if tags_json:
                # Add tags to database
                try:
                    response = self.table.put_item(
                        Item={
                            'tweet_id': a['id_str'],
                            'image_uri': image,
                            'tags' : tags_json
                        }
                    )
                except Exception as e:
                    print('\nError adding item to database: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args))


    def on_error(self, status):
        print('status:%d' % status)
        return True

consumer_key = os.environ.get('APIKEY')
consumer_secret = os.environ.get('APISECRET')
access_token = os.environ.get('ACCESSTOKEN')
access_secret = os.environ.get('ACCESSSECRET')


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
listener = TwitterListener()
# for i in range(0,99):
#    tweets = api.user_timeline(screen_name='EarthPix',include_rts=False,exclude_replies=True, tweet_mode = 'extended',count=100)[i]
#    listener.get_tweets(tweets)

plot_tags()


