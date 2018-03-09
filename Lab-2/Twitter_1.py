import os
import tweepy
from tweepy import OAuthHandler

def setup_twitter():
    consumer_key = os.environ.get('APIKEY')
    consumer_secret = os.environ.get('APISECRET')
    access_token = os.environ.get('ACCESSTOKEN')
    access_secret = os.environ.get('ACCESSSECRET')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

def get_my_twitter_details(api):
    user = api.me()

    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.followers_count))
    print('Created: ' + str(user.created_at))
    print('Description: ' + str(user.description))

def main():
    api = setup_twitter()
    get_my_twitter_details(api)


if __name__ == "__main__":
    main()
