import re

emoticons_str = r"""
    (?:
        [<>]?
        [:;=8]                          # eyes
        [\-o\*\'-]?                     # optional nose
        [\)\]\(\[dDpP/\:\>\<\}\{@\|\\]  # mouth
        |
        [\)\]\(\[dDpP/\:\>\<\}\{@\|\\]  # mouth
        [\-o\*\'-]?                     # optional nose
        [:;=8]                          # eyes
        [<>]?
        |
        <3                              # heart
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
    r'[^@]+@[^@]+\.[^@]+ ' #e-mails

]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


tweet = 'RT @JordiTorresBCN: just an example! 08:00 www.google.weirddomain :D http://JordiTorres.Barcelona #masterMEI s.yfant._idou@upc.fib.edu CH4 www.google.com/query=love elpais.com/elpais2017 +306931102082 0030 6931102082'
print(preprocess(tweet))