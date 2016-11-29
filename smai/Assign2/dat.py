TRAIN_FILE = "DOROTHEA/dorothea_train.data"
OUT_FILE = "DOROTHEA/train.data"
with open(TRAIN_FILE) as f:
	tra_raw = f.readlines()
tra_lis = [item.split() for item in tra_raw]
for item in tra_lis:
	print len(item)
f = open(OUT_FILE,'w')
f.write('\n'.join(tra_lis))
f.close()