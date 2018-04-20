import os
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import sys
import boto3
import label
from dateutil import parser

TAG_TABLE = 'twitter-images'
AWS_REGION = 'eu-west-3'


def get_image_from_tweet(status):
    media_list = list()
    if 'media' in status['extended_entities']:
        for media in status['extended_entities']['media']:
            if media['type'] == 'photo':
                print('\n' + status['text'])  # print uri of status
                image_uri = media['media_url']
                print(image_uri + '\n')
                media_list.append(image_uri)
    return media


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
        try:
            image_list = get_image_from_tweet(tweet)
            self.image_counter += len(image_list)

            for image in image_list:
                label.main(image)

            # response = self.table.put_item(
            #     Item={
            #         'id': tweet['id_str'],
            #         'c0': str(tweet['coordinates']['coordinates'][0]),
            #         'c1': str(tweet['coordinates']['coordinates'][1]),
            #         'text': tweet['text'],
            #         # "created_at": time.strptime(tweet['created_at'], '%b %d %Y %T %Z %Y'),
            #         "created_at" : str(parser.parse(tweet["created_at"]).timestamp()),
            #     }
            # )
            if (self.image_counter > 100):
                twitter_stream.stop()
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

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(locations=[-2.5756, 39.0147, 5.5982, 43.957])

