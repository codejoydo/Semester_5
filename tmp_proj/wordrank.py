import sys
import ujson
import operator

DTPD_FILE = "dt_pd_ntop10.json"
TWPD_FILE = "wt_pd_ntop10.json"
NTOPICS = 10
FNAME = sys.argv[1]

def eprint(msg):
    sys.stderr.write(msg)

with open(DTPD_FILE) as data_file:
	dt_data = ujson.load(data_file)

with open(TWPD_FILE) as data_file:
	tw_data = ujson.load(data_file)

words = tw_data[tw_data.keys()[0]].keys()

dt_pd_raw = []

for key in dt_data.keys():
	if dt_data[key][u'file_name'] == FNAME:
		dt_pd_raw = dt_data[key][u'dt_pd']
		break

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

dw_pd = sorted(dw_pd.items(), key=operator.itemgetter(1))
# output = []
# for i in range(len(dw_pd)):
# 	if dw_pd[-i][1]>0.0:
# 		output.append(dw_pd[-i][0])
# print ", ".join(output)
print len(dw_pd)