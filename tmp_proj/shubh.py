import ujson
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import sys

def eprint(msg):
    sys.stderr.write(msg)

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
	tokens_nn = [i for i in tokens if not i.isdigit() or len(i)>1]
	stopped_tokens = [i for i in tokens_nn if not i in en_stop]
	stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
	texts.append(stemmed_tokens)

eprint("creating dictionary ...\n")

with open('dictnet_vgg_labels.txt') as data_file:
	dict_data = data_file.readlines()

dict_data = [item.strip() for item in dict_data]
dict_texts = []

for i in dict_data:
	raw = i.lower()
	tokens = tokenizer.tokenize(raw)
	tokens_nn = [i for i in tokens if not i.isdigit() or len(i)>1]
	stopped_tokens = [i for i in tokens_nn if not i in en_stop]
	stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
	if stemmed_tokens:
		dict_texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(dict_texts)

eprint("generating corpus in bow format ...\n")

corpus = [dictionary.doc2bow(text) for text in texts]

eprint("generating LDA model ...\n")

lda = gensim.models.ldamodel.LdaModel(corpus, id2word = dictionary, num_topics=10)

eprint("generating topic probability distribution for documents ...\n")

outfile = {}
for i in range(len(corpus)):
	key = im_ids_txt[i]
	document = corpus[i]
	fname = data[key][u'file_name']
	tmp_dict = {}
	tmp_dict['dt_pd'] = lda[document]
	tmp_dict['file_name'] = fname
	outfile[key] = tmp_dict  

with open('dt_pd_ntop10.json', 'w') as fp:
    ujson.dump(outfile, fp)

eprint("generating word probability distribution for documents ...\n")

outfile = {}
for i in range(10): 
	topic_pdf = lda.print_topic(i,topn=len(dictionary)).split('+')
	words = [item.split('*')[1] for item in topic_pdf]
	word_probs = [item.split('*')[0] for item in topic_pdf]
	outfile[i] = dict(zip(words, word_probs))

with open('wt_pd_ntop10.json', 'w') as fp: 
    ujson.dump(outfile, fp)

eprint("done\n")