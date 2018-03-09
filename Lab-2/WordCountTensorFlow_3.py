import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords
from collections import Counter
from WordCountTensorFlow_2 import get_tokens_no_punct

def get_count_no_stopwords():
    tokens = get_tokens_no_punct()
    # lambda expression here
    # store stopwords in a variable for eficiency
    # avoid retrieving them from ntlk for each iteration
    sw = stopwords.words('english')
    filtered = [w for w in tokens if not w in sw]
    count = Counter(filtered)
    return count

count = get_count_no_stopwords()
print (count.most_common(10))
print(sum(count.values()))