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

eprint("loading corpus ...\n")

with open('data.json') as data_file:
    data = ujson.load(data_file)

doc_set = []
im_ids_txt = []

for key in data.keys():
    im_ids_txt.append(key)
    doc_content_list = []
    for itemkey in data[key].keys():
        for item in data[key][u'captions']:
            doc_content_list.append(item)
        for item in data[key][u'text']:
            doc_content_list.append(item)
    doc_set.append(' '.join(doc_content_list))

texts = []

eprint("processing documents ...\n")

for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    tokens_nn = [i for i in tokens if not hnum(i) and len(i)>1]
    stopped_tokens = [i for i in tokens_nn if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(getuniq(stemmed_tokens))

eprint("generating texts.json ...\n")

outfile = {}
for i in range(len(texts)):
    key = im_ids_txt[i]
    fname = data[key][u'file_name']
    tmp_dict = {}
    tmp_dict['text'] = texts[i]
    tmp_dict['file_name'] = fname
    outfile[key] = tmp_dict  

with open('texts.json', 'w') as fp:
    ujson.dump(outfile, fp)

eprint("done\n")