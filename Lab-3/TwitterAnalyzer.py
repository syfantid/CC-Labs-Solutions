import json
import string
import sys
sys.path.insert(0,'/home/sofia/PycharmProjects/Labs-solutions/Lab-2')
from collections import Counter
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (6,6)
import matplotlib.pyplot as plt

from nltk.sentiment.vader import SentimentIntensityAnalyzer as sentiment

from Twitter_3 import preprocess

def open_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])
            print(tokens)

stop = list(string.punctuation) + ['rt', 'via', 'RT']

def count_frequencies(file_name):
    with open(file_name, 'r') as f:
        count_terms = Counter()
        count_hashtags = Counter()
        count_terms_no_mentions_hashtags = Counter()
        for line in f:
            tweet = json.loads(line)
            # Create a list with all the terms
            # terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            count_terms.update(get_terms(tweet))
            count_hashtags.update(get_hashtags(tweet))
            count_terms_no_mentions_hashtags.update(get_terms_no_mentions_hashtags(tweet))

        return [count_terms,count_hashtags,
                count_terms_no_mentions_hashtags]

def get_terms(tweet):
    # Create a list with all the terms
    return [term for term in preprocess(tweet['text']) if term not in stop]

def get_hashtags(tweet):
    # Create a list with all the terms
    return [term for term in preprocess(tweet['text']) if term.startswith('#')]

def get_terms_no_mentions_hashtags(tweet):
    return [term for term in preprocess(tweet['text']) if term not in stop if not term.startswith(('#', '@'))]

def print_list(list):
    i = 1
    for word,index in list:
        print('%d. %s : %s' % (i, word, index))
        i+=1

def create_chart(counter, fig_name):
    sorted_x, sorted_y = zip(*counter.most_common(15))
    print(sorted_x, sorted_y)

    plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
    plt.xticks(range(len(sorted_x)), sorted_x, rotation=90)
    plt.axis('tight')
    plt.tight_layout()

    #plt.show()  # show it on IDE

    plt.savefig(fig_name)  # save it on a file

def calculate_sentiment():


# Hawking case
top_terms,top_hashtags,top_terms_no_mentions_hashtags = count_frequencies('Hawking.json')
print('Top ten most frequent tokens :\n')
print_list(top_terms.most_common(10))
print('\n')
print('Top ten most frequent hashtags:\n')
print_list(top_hashtags.most_common(10))
print('\n')
print('Top ten most frequent terms, skipping mentions and hashtags: \n')
print_list(top_terms_no_mentions_hashtags.most_common(10))
print('\n')
#create_chart(top_hashtags,'hawking.png')

# Barcelona case
# top_terms,top_hashtags,top_terms_no_mentions_hashtags = count_frequencies('Lab3.CaseStudy.json')
create_chart(top_hashtags,'barca.png')