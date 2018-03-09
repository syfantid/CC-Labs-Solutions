import nltk
nltk.download('punkt')
import re

from collections import Counter

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    tokens = nltk.word_tokenize(text)
    return tokens

tokens = get_tokens()
no_punctuation = re.sub(r'[^\w\s]','',lowers)
tokens = nltk.word_tokenize(no_punctuation)
count = Counter(tokens)
print (count.most_common(10))