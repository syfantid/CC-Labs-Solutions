import re
from Twitter_1 import setup_twitter
from Twitter_2 import get_tweets_about_topic
import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords


emoticons_str = r"(?:[<>]?[:;=8][\-o\*\'-]?[\)\]\(\[dDpP\/\:\>\<\}\{@\|\\]|[\)\]\(\[dDpP\/\:\>\<\}\{@\|\\][\-o\*\'-]?[:;=8][<>]?|<3)"

regex_str = [
    emoticons_str,
    r'(?:[01]?[0-9]|2[0-3]):[0-5][0-9]',  # time
    r'(?:\d{2})[\/.-](?:\d{2})[\/.-](?:\d{2,4})', # date format: dd-MM-yy(yy) and dd.MM.yy(yy) and dd/MM/yy(yy)
    r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', # date time with 3 letter month name
    r'<[^>]+>',  # HTML tags

    r'(?:@[\w_]+)',  # @-mentions

    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'(?:(?:http|https):\/\/)?(?:[-a-zA-Z0-9.]{2,256}\.[a-z]{2,15})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',  # links
    # URLs (deprecated by links' regex above that can handle multiple domains
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',

    # Phone numbers of 9 or 10 digits including optional country code in the following formats
    # (hyphens are optional and can be replaced by whitespace or no space):
    # The formats were acquired by online resources such as:
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_Spain
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_Greece
    r"(?:[\(]?(?:\+|00)\d{1,3}[\)]?(?: |\-)?)?" # County code +x(xx) or 00x(xx) with or without parentheses
    r"(?:\d{4}(?:\s?|[\-])\d{6}" # Format xxxx-xxxxxx (10 digits)
    r"|\d{3,4}(?:\s?|[\-]?)\d{2}(?:\s?|[\-]?)\d{2}(?:\s?|[\-]?)\d{2}|" # Fomrat: xxx(x)-xx-xx-xx (10 digits)
    r"\d{2,3}(?:\s?|[\-]?)\d{3}(?:\s?|[\-]?)\d{2}(?:\s?|[\-]?)\d{2}|" # Format: xx(x)-xxx-xx-xx (9 or 10 digits)
    r"\d{3}(?:\s?|[\-]?)\d{3}(?:\s?|[\-]?)\d{3})", # Format: xxx-xxx-xxx (9 digits)

    r"(?:[a-zA-Z]\.){2,}", # Abbreviations e.g. U.K., U.S.A., D.I.Y., A.S.A.P., etc.
    r'[\w.-]+@[\w.-]+',  # e-mails
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_’]+[a-z])",  # words with - or ' or ’
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def remove_stopwords(tokens):
    sw = stopwords.words('english')
    filtered = [w for w in tokens if not w.lower() in sw]
    return filtered

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    for token in tokens: # Remove single-character tokens that are not alphanumeric (punctuation)
        #print(token + '\n')
        if len(token) <= 1 and not token.isalnum():
            tokens.remove(token)
    return remove_stopwords(tokens) # return tokens without stopwords

# Uncomment this block to test the functionality of the regex
# tweet = 'RT @JordiTorresBCN:  10/03/2017 12.25.2016 10-09-1985 03 may 2014 03.02.12 "just" :D U.S.A. an example! 08:00 www.google.weirddomain www.fdksfd.com.tr :D http://JordiTorres.Barcelona #masterMEI s.yfant._idou@upc.fib.edu CH4 www.google.com/query=love elpais.com/elpais2017 +30 6931 102082 +30 6931102082 +306931102082 0030 6931102082'
# print(preprocess(tweet))

# Given that Tweepy does not provide functionality to our knowledge to filter results based on language at retrieval
# time (only possibility is filtering after retrieval), we implemented a method to retrieve tweets about a specified
# topic e.g. Cloud Computing on a specified language. Now the benefits of our tokenizer can be explored. Otherwise, we
# could have simply filter out non-english tweets in an if statement in python using the field tweet.lang.
def main():
    api = setup_twitter()
    print(len("“"))
    tweets = get_tweets_about_topic(10,'Cloud Computing',api)
    for tweet in tweets:
        print('Original text: ' + tweet.full_text)
        print(preprocess(tweet.full_text))
        print('\n')


if __name__ == "__main__":
    main()
