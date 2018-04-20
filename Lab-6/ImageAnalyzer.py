import ast
import base64
import os
from venv import logger

import googleapiclient.discovery
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import sys
import boto3
import plotly.plotly as py
import plotly.graph_objs as go

py.plotly.tools.set_credentials_file(username = os.environ.get('PLOTLY_USERNAME'), api_key = os.environ.get('PLOTLY_KEY'))

TAG_TABLE = 'twitter-images'
AWS_REGION = 'eu-west-3'


def get_image_from_tweet(status):
    media_list = list() # in case a single tweet contains more than one image
    if 'media' in status['extended_entities']:
        for media in status['extended_entities']['media']:
            if media['type'] == 'photo':
                # print('\n' + status['text'])  # print uri of status
                image_uri = media['media_url']
                media_list.append(image_uri)
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
    item = {}
    if(tags_response):
        for result in tags_response['responses'][0]['labelAnnotations']:
            item[result['description']] = str(result['score'])
        jsonData = json.dumps(item)
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
        print(tweet)
        for tweet_tags in tweet['tags']:
            tweet_tags_dict = json.loads("[" + tweet_tags + "]")
            for tag,score in tweet_tags_dict.items():
                if not tag in tag_scores:
                    tag_scores[tag] = score
                else:
                    tag_scores[tag] += score

    for k,v in tag_scores.items():
        print(k + ": " + v + '\n')

    # data = [go.Bar(
    #     x=['giraffes', 'orangutans', 'monkeys'],
    #     y=[20, 14, 23]
    # )]
    #
    # py.iplot(data, filename='basic-bar')


class MyListener(StreamListener):

    image_counter = 0

    def __init__(self):
        dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
        try:
            self.table = dynamodb.Table(TAG_TABLE)
        except Exception as e:
            print('\nError connecting to database table: ' + (e.fmt if hasattr(e, 'fmt') else '') + ','.join(e.args))
            sys.exit(-1)

    def on_data(self, data):
        tweet = json.loads(data)
        if 'extended_entities' not in tweet:
            sys.stdout.write('.')
            sys.stdout.flush()
            return True

        image_list = get_image_from_tweet(tweet)

        tags_response = ""
        for image in image_list:
            # Check if we gathered 100 images already
            self.image_counter += 1
            if (self.image_counter > 100):
                self.twitter_stream.stop()
                break

            tags_response = get_tags(image)

            # Convert tags to JSON
            tags_json = tags_to_json(tags_response)

            if tags_json:
                # Add tags to database
                try:
                    response = self.table.put_item(
                        Item={
                            'tweet_id': tweet['id_str'],
                            'image_uri': image,
                            'tags:' : tags_json
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

plot_tags()
#
#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(locations=[-79.7619,40.4774,-71.7956,45.0159])

