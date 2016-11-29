import ujson
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from collections import Counter
import sys

def eprint(msg):
    sys.stderr.write(msg)
def hnum(inputString):
    return any(char.isdigit() for char in inputString)
def getuniq(doc):
    cnt = Counter(doc).items()
    words = [item[0] for item in cnt]
    return words

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

eprint("creating dictionary 2 ...\n")

with open('dictnet_vgg_labels.txt') as data_file:
    dict_data = data_file.readlines()

dict_data = [item.strip() for item in dict_data]
dict_texts = []

for i in dict_data:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    tokens_nn = [i for i in tokens if not hnum(i) and len(i)>1]
    stopped_tokens = [i for i in tokens_nn if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    if stemmed_tokens:
        dict_texts.append(stemmed_tokens)

print len(dict_texts)

with open('dict_2.json', 'w') as fp:
    ujson.dump(dict_texts, fp)

eprint("creating dictionary 1 ...\n")

with open('data.json') as data_file:
    data = ujson.load(data_file)

doc_set = []
dict_texts = []
for key in data.keys():
    doc_content_list = []
    for itemkey in data[key].keys():
        for item in data[key][u'captions']:
            doc_content_list.append(item)
        for item in data[key][u'text']:
            doc_content_list.append(item)
    doc_set.append(' '.join(doc_content_list))

dict_texts = []
texts = []

for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    tokens_nn = [i for i in tokens if not hnum(i) and len(i)>1]
    stopped_tokens = [i for i in tokens_nn if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)
    dict_texts += getuniq(stemmed_tokens)

dict_texts = getuniq(dict_texts)
dict_texts = [[item] for item in dict_texts]
print len(dict_texts)

with open('doc_set.json', 'w') as fp:
    ujson.dump(texts, fp)
with open('dict_1.json', 'w') as fp:
    ujson.dump(dict_texts, fp)