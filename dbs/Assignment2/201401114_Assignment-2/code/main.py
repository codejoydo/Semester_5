#/bin/python
import os.path
import time
from btree import *
global argv,filename,n_attr,mem_blocks,M,tr
global fp, op, main_op, min_size_buffer, max_size_buffer, answer, block_size, hash

min_size_buffer=40
max_size_buffer=80

def write_to_file(vec):
	for record in vec:
		op.write(record+'\n')

def open_file(filename, type_index):
	"Opens a file for write"
	global fp, op
	fp = open(filename,'r')
	if type_index == 'btree':
		op=open('buf/output_btree.txt','w+')
	else:
		op=open('buf/output_hash.txt','w+')

def close_file():
	"Close the file"
	global fp, op
	fp.close()
	op.close()


def getnext():
	"Read each record and do operations"
	global M, fp, answer, block_size, type_index, hash, count_files, tr
	for i in range(M):
		record = fp.readline()
		if record == '':
			#End of file
			write_to_file(answer)
			return 0
		if len(answer) == block_size:	
			write_to_file(answer)
			answer = []
		record = ' '.join(record.strip(' ').strip('\t').strip('\n').split(','))

		if type_index == 0:
			if tr.search(record) is None:
				tr.insertTree(record)
				answer.append(record)
		else:
			if record not in hash:
				hash[record] = 1
				answer.append(record)
	return 1


if __name__ == "__main__":

	answer = []
	hash = {}
	main_op = open('output/201401114_output','a')
	query = raw_input("")
	argv = query.strip('\n').split(" ")

	mem_blocks = int(argv[0].strip(' '))
	filename = argv[1].strip(' ')
	filename = 'input/'+filename
	bsize = argv[2]
	type_index = argv[3]
	bsize = bsize.split('MB')[0].strip(' ')
	
	temp = open(filename,'r')
	rec = temp.readline()
	temp.close()
	
	n_attr = len(rec.strip('\n').strip(' ').split(','))
	block_size = int((float(bsize)*1000000)/(4*n_attr))
	M = (mem_blocks-1)*block_size

	n = int(((float(bsize)*1000000)-8)/12)
	tr = BTree(n)
	hash = {}
	answer = []
	open_file(filename,type_index)
	start_time = time.time()
	while(getnext()):
		1
	tot_time=str(time.time() - start_time)
	close_file()

	if type_index == 'btree':
		ptr = open('buf/output_btree.txt','r')
	else:
		ptr = open('buf/output_hash.txt','r')
	lines = ptr.readlines()
	count_files = len(lines)
	ptr.close()
	main_op.write(tot_time+' '+str(count_files)+'\n')
	print count_files
	main_op.close()
