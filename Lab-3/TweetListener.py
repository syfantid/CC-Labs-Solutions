import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('trump.json', 'a') as f:
                print(data)
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

    def connect_twitter(self):
        consumer_key = os.environ.get('APIKEY')
        consumer_secret = os.environ.get('APISECRET')
        access_token = os.environ.get('ACCESSTOKEN')
        access_secret = os.environ.get('ACCESSSECRET')

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        return auth


listener = MyListener()
auth = listener.connect_twitter()
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['trump'],languages=['en'])
#twitter_stream.filter(languages=['en'])
