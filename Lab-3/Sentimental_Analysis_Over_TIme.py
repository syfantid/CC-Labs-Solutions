import time
import pandas as pd
import json
def getTweet(file):
    tweets_data = []
    tweets_file = open(file, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    tweets_data=tweets_data
    return tweets_data


def ConvertJsonToTable():
    tweets_data=getTweet()
    #Pull the data we're interested in out of the Twitter data we captured
    rows_list = []
    now = time.mktime(time.gmtime())
    for tweet in tweets_data:
        SentimentalAnalysis(tweet['text'])
        author = ""
        rtauthor = ""
        # If it was a retweet, get both the original author and the retweeter
        try:
            author = tweet['user']['screen_name']
            rtauthor = tweet['retweeted_status']['user']['screen_name']
        except:
            #Otherwise, just get the original author
            try:
                author = tweet['user']['screen_name']
            except:
                continue

        reply_to = ""
        if (tweet['in_reply_to_screen_name'] != None):
            reply_to = tweet['in_reply_to_screen_name']
        followers = tweet['user']['followers_count']
        text=tweet['text']
        created_at= time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        location=tweet.get('user', {}).get('location', {})
        dict1 = {}
        dict1.update(
            {'author': author, 'retweet_of': rtauthor, 'reply_to': reply_to, 'followers': followers ,'created_at':created_at,'text':text,'location':location})
        rows_list.append(dict1)

    tweets = pd.DataFrame(rows_list)
    print(tweets.head(1))

def SentimentalAnalysis(tweet):
    polarity = round(textblob.TextBlob(tweet).sentiment.polarity, 4)
    print(polarity,)

getTweet('trump.json')
ConvertJsonToTable()

