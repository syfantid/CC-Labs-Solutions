import time
import pandas as pd
import json
import os
import plotly
# from plotly.plotly import plot
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

plotly.tools.set_credentials_file(username = os.environ.get('PLOTLY_USERNAME'), api_key = os.environ.get('PLOTLY_KEY'))
import numpy
import re

import textblob
from TwitterPreprocessing import preprocess

def getTweets(file):
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


def ConvertJsonToTable(filename):
    tweets_data=getTweets(filename)
    # Pull the data we're interested in out of the Twitter data we captured
    rows_list = []
    now = time.mktime(time.gmtime())
    for tweet in tweets_data:
        polarity = SentimentalAnalysis(tweet['text'])
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
        text = tweet['text']
        created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        location = tweet.get('user', {}).get('location', {})
        state = getState(location)
        if state != "": # If tweet is from US
            dict1 = {}
            dict1.update(
                {'author': author, 'retweet_of': rtauthor, 'reply_to': reply_to, 'followers': followers ,
                 'created_at': created_at,'text': text,'location': location,'state': state, 'polarity': polarity})
            rows_list.append(dict1)

    tweets = pd.DataFrame(rows_list)
    # print(tweets.head(10))
    return tweets

# Get US state based on tweet's location; if tweet posted outside of the US get emty string
def getState(location):
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if location is None:
        return ""

    # Match state
    regex = r"(?:\w+),\s*([a-zA-Z]{2}\b)"
    matches = re.finditer(regex, location)

    for match in matches:
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            state = match.group(groupNum)
            if state in states:
                return state
    return ""

def SentimentalAnalysis(tweet):
    preprocessed_tweet = ' '.join(preprocess(tweet))
    # print(preprocessed_tweet)
    polarity = round(textblob.TextBlob(preprocessed_tweet).sentiment.polarity, 4)
    return polarity

# Calculate the average sentiment polarity per US state
def GetAveragePolarityPerState(filename):
    tweets = ConvertJsonToTable(filename)

    state_tweets = []
    for state in tweets['state']:
        average_polarity = numpy.mean(tweets.loc[tweets['state'] == state]['polarity'])
        state_dict = {'state': state, 'polarity': average_polarity}
        state_tweets.append(state_dict)

    return pd.DataFrame(state_tweets)


def getStateFromCode(state_codes):
    us_state_abbrev = {
        'AK': 'Alaska',
        'NH': 'New Hampshire',
        'CA': 'California',
        'CT': 'Connecticut',
        'AL': 'Alabama',
        'OH': 'Ohio',
        'NM': 'New Mexico',
        'WV': 'West Virginia',
        'ND': 'North Dakota',
        'IL': 'Illinois',
        'VT': 'Vermont',
        'MN': 'Minnesota',
        'NV': 'Nevada',
        'KS': 'Kansas',
        'OK': 'Oklahoma',
        'ME': 'Maine',
        'PA': 'Pennsylvania',
        'NY': 'New York',
        'FL': 'Florida',
        'MD': 'Maryland',
        'UT': 'Utah',
        'TN': 'Tennessee',
        'MT': 'Montana',
        'HI': 'Hawaii',
        'WA': 'Washington',
        'MA': 'Massachusetts',
        'VA': 'Virginia',
        'AR': 'Arkansas',
        'WI': 'Wisconsin',
        'CO': 'Colorado',
        'IN': 'Indiana',
        'SD': 'South Dakota',
        'LA': 'Louisiana',
        'RI': 'Rhode Island',
        'AZ': 'Arizona',
        'NJ': 'New Jersey',
        'KY': 'Kentucky',
        'MI': 'Michigan',
        'ID': 'Idaho',
        'NC': 'North Carolina',
        'WY': 'Wyoming',
        'MO': 'Missouri',
        'IA': 'Iowa',
        'OR': 'Oregon',
        'TX': 'Texas',
        'SC': 'South Carolina',
        'GA': 'Georgia',
        'DE': 'Delaware',
        'NE': 'Nebraska',
        'MS': 'Mississippi'
    }

    state_names = []
    for state_code in state_codes:
        state_names.append(us_state_abbrev.get(state_code))
    return pd.Series(state_names)


def PlotSentiment(filename):
    df = GetAveragePolarityPerState(filename)

    for col in df.columns:
        df[col] = df[col].astype(str)

    # scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
    #        [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

    scl = [[0.0, 'rgb(6,17,9)'], [0.2, 'rgb(22,54,32)'], [0.4, 'rgb(53,125,77)'], \
        [0.6, 'rgb(94,186,125)'], [0.8, 'rgb(166,217,183)'], [1.0, 'rgb(219,240,226)']]

    df['text'] = getStateFromCode(df['state']) + '<br>' + \
                 'Polarity ' + df['polarity']

    data = [dict(
        type='choropleth',
        colorscale=scl,
        autocolorscale=False,
        locations=df['state'],
        z=df['polarity'].astype(float),
        locationmode='USA-states',
        text=df['text'],
        marker=dict(
            line=dict(
                color='rgb(255,255,255)',
                width=2
            )),
        colorbar=dict(
            title="Sentiment Polarity")
    )]

    layout = dict(
        title='Sentiment Polarity about Refugees by State<br>(Hover for breakdown)',
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'),
    )

    fig = dict(data=data, layout=layout)
    plot(fig, filename='d3-cloropleth-map')


PlotSentiment('refugees.json')
