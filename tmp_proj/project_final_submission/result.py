import sys
import ujson
import operator

def eprint(msg):
    sys.stderr.write(msg)

NTOPICS = 10
DTPD_FILE = "DT_PD/dt_pd_ntop"+str(NTOPICS)+"_1.json"
TWPD_FILE = "WT_PD/wt_pd_ntop"+str(NTOPICS)+"_1.json"
TEXT_FILE = "texts.json"

''' Load data Files '''
with open(DTPD_FILE) as f:
    dt_data = ujson.load(f)
with open(TWPD_FILE) as f:
    tw_data = ujson.load(f)
with open(TEXT_FILE) as f:
    data = ujson.load(f)

file_names = [elem[u'file_name'] for elem in data.values()]
for i in range(NTOPICS):
    words = tw_data[tw_data.keys()[0]].keys()

cntr = 0
print len(data.keys())
vec1 = []
vec2 = []
for i in range(11):
    ans = 0
    for key in data.keys():
        dt_pd_raw = dt_data[key][u'dt_pd']
        dt_pd_values = [item[1] for item in dt_pd_raw]
        dt_pd_keys = [item[0] for item in dt_pd_raw]
        dt_pd = dict(zip(dt_pd_keys, dt_pd_values))

        dw_pd = {}

        for word in words:
            prob = 0.0
            for topic in tw_data.keys():
                if int(topic) in dt_pd_keys:
                    prob += float(tw_data[topic][word]) * float(dt_pd[int(topic)])
            dw_pd[word] = prob
        tmp_list = dw_pd.items()
        tmp_list.sort(key=operator.itemgetter(1))
        tmp_list.reverse()
        #dw_pd.sort(key=operator.itemgetter(1))

        reranked_dictionary = [item[0] for item in tmp_list]
        x = int(float(len(reranked_dictionary)*i)/10)
        reranked_dictionary = reranked_dictionary[:x]
        text = data[key][u'text']
        
        #print key
        #print ' '.join(text)
        #print ' '.join(reranked_dictionary)
        
        cnt = 0
        for word in text:
            if word in reranked_dictionary:
                cnt+=1
    	#print key, len(text), float(cnt)/len(text)
    	ans += float(cnt)/len(text)
    	cntr += 1
        if cntr%200==0:
        	break   	 
    ans = ans/2
    print i, ans
    vec1.append(ans)
    vec2.append(i*10)
print vec1,vec2

# output = []
# for i in range(len(dw_pd)):
#   if dw_pd[-i][1]>0.0:
#       output.append(dw_pd[-i][0])
# print ", ".join(output)
#   print key,len(dw_pd)'''
