import re

emoticons_str = r"(?:[<>]?[:;=8][\-o\*\'-]?[\)\]\(\[dDpP\/\:\>\<\}\{@\|\\]|[\)\]\(\[dDpP\/\:\>\<\}\{@\|\\][\-o\*\'-]?[:;=8][<>]?|<3)"

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    # Phone numbers of 9 or 10 digits including optional country code in the following formats
    # (hyphens are optional and can be replaced by whitespace or no space):
    # The formats were acquired by online resources such as:
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_Spain
    # https://en.wikipedia.org/wiki/Telephone_numbers_in_Greece
    r"(?:[\(]?(?:\+|00)\d{1,3}[\)]?(?: |\-)?)?" # County code +x(xx) or 00x(xx) or (Country Code)
    r"(?:\d{4}(?:\s?|[\-])\d{6}" # Format xxxx-xxxxxx (10 digits)
    r"|\d{3,4}(?:\s?|[\-]?)\d{2}(?:\s?|[\-]?)\d{2}(?:\s?|[\-]?)\d{2}|" # Fomrat: xxx(x)-xx-xx-xx (10 digits)
    r"\d{2,3}(?:\s?|[\-]?)\d{3}(?:\s?|[\-]?)\d{2}(?:\s?|[\-]?)\d{2}|" # Format: xx(x)-xxx-xx-xx (9 or 10 digits)
    r"\d{3}(?:\s?|[\-]?)\d{3}(?:\s?|[\-]?)\d{3})", # Format: xxx-xxx-xxx (9 digits)

    r"(?:[a-zA-Z]\.){2,}", # Abbreviations
    
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)




def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


tweet = 'RT @JordiTorresBCN: "just" :D U.S.A. an example! 08:00 www.google.weirddomain :D http://JordiTorres.Barcelona #masterMEI s.yfant._idou@upc.fib.edu CH4 www.google.com/query=love elpais.com/elpais2017 +30 6931 102082 +30 6931102082 +306931102082 0030 6931102082'
print(preprocess(tweet))