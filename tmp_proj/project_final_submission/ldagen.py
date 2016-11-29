import ujson
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import sys
NTOP = int(sys.argv[1])
DNO = sys.argv[2]

def eprint(msg):
    sys.stderr.write(msg)

with open('data.json') as data_file:
    data = ujson.load(data_file)
im_ids_txt = data.keys()
eprint("creating dictionary ...\n")
with open('doc_set.json') as f:
    texts = ujson.load(f)
with open('dict_'+DNO+'.json') as f:
	dict_texts = ujson.load(f)

print len(dict_texts)
print len(texts)


dictionary = corpora.Dictionary(dict_texts)

eprint("generating corpus in bow format ...\n")

corpus = [dictionary.doc2bow(text) for text in texts]

eprint("generating LDA model ...\n")

lda = gensim.models.ldamodel.LdaModel(corpus, id2word = dictionary, num_topics=NTOP)

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

with open('DT_PD/dt_pd_ntop'+str(NTOP)+'_'+DNO+'.json', 'w') as fp:
    ujson.dump(outfile, fp)

eprint("generating word probability distribution for documents ...\n")

outfile = {}
for i in range(NTOP): 
	topic_pdf = lda.print_topic(i,topn=len(dictionary)).split('+')
	words = [item.split('*')[1].strip() for item in topic_pdf]
	word_probs = [item.split('*')[0] for item in topic_pdf]
	outfile[i] = dict(zip(words, word_probs))

with open('WT_PD/wt_pd_ntop'+str(NTOP)+'_'+DNO+'.json', 'w') as fp: 
    ujson.dump(outfile, fp)

eprint("done\n")
