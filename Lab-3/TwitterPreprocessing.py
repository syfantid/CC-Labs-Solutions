import re
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

