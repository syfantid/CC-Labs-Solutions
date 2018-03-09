import json
import tweepy
from Twitter_1 import setup_twitter

# we use 1 to limit the number of tweets we are reading
# and we only access the `text` of the tweet

def get_home_timeline(number_tweets,api):
    for status in tweepy.Cursor(api.home_timeline).items(number_tweets):
        print(json.dumps(status._json, indent=2))

def get_friends(number_friends,api):
    for friend in tweepy.Cursor(api.friends).items(number_friends):
        print(json.dumps(friend._json, indent=2))

def get_user_timeline(number_tweets,api):
    for tweet in tweepy.Cursor(api.user_timeline).items(number_tweets):
        print(json.dumps(tweet._json, indent=2))

def main():
    api = setup_twitter()
    print('Home Timeline\n')
    get_home_timeline(1,api)
    print('Friend list\n')
    get_friends(1,api)
    print('User List\n')
    get_user_timeline(1,api)


if __name__ == "__main__":
    main()
