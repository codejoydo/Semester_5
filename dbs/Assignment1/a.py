import sqlparse

TABLE_SCHEMA="metadata.txt" 
TABLE_VALUES=["table1.csv","table2.csv"]
CONDITION="="
L_E="\r\n"

def clear_stuff(txt):
	'''
		clear spaces quotes etc. from data read from files
	'''
	txt = txt.strip()
	txt_list = txt.split(',')
	junk_char = [' ','\r','\n','\"','\'','\t']
	for charr in junk_char:	
		txt_list = [ i.strip(charr) for i in txt_list ]
	return txt_list

def clean_list(dirty_list):
	'''
		cleans list of keywords, spaces and comas
	'''
	clean_list = []
	for i in dirty_list:
		clean_list.append(i.replace("SELECT", "").replace("FROM", "").replace("WHERE", "").strip().strip(","))
	for i in range(len(clean_list)):
		if '=' in clean_list[i]:
			lhs,rhs = clean_list[i].split('=')
			lhs = lhs.strip()
			rhs = rhs.strip()
			clean_list[i] = lhs + '=' + rhs
	return clean_list

def get_query():
	'''
		gets query as input
	'''
	sql = raw_input('>>>')
	sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
	return process_query(sql)

def process_query(sql):
	'''
		processes the query, finding the columns, tables and conditions
	'''
	if ';' not in sql:
		raise Exception('end query using \';\' operator')
	sql = sql.strip(';')
	if 'SELECT' not in sql:
		raise Exception('SELECT not in query')
	if 'FROM' not in sql:
		raise Exception('FROM not in query')
	if 'WHERE' not in sql:
		sql = sql + '\n' + "WHERE True"
	sql_list = sql.split('\n')
	select_idx = [ i for i,item in enumerate(sql_list) if "SELECT" in item ][0]
	from_idx = [ i for i,item in enumerate(sql_list) if "FROM" in item ][0]
	where_idx = [ i for i,item in enumerate(sql_list) if "WHERE" in item ][0]
	select_list = clean_list(sql_list[select_idx:from_idx])
	from_list = clean_list(sql_list[from_idx:where_idx])
	where_tmp_list = clean_list(sql_list[where_idx:])
	where_list = []
	for entry in where_tmp_list:
		for sub_entry in entry.split():
			where_list.append(sub_entry)
	return select_list, from_list, where_list

def merge_tables(table1,table2):
	'''
		performs natural-join of 2 tables
	'''
	ret_table = []
	for entry1 in table1:
		for entry2 in table2:
			tmp_dict = {}
			tmp_dict.update(entry1)
			tmp_dict.update(entry2)
			ret_table.append(tmp_dict)
	return ret_table

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def select_columns(table,fields,function):
	'''
		returns a table consisting only those fields
	'''
	ret_table = []
	if fields[0] == '*':
		fields = table[0].keys()
	for entry in table:
		tmp_list = []
		for key in entry:
			if key in fields:
				tmp_list.append(str(entry[key]))
#			else:
#				raise Exception('SELECT clause is wrong, ' + key + ' not in schema.')
		ret_table.append(tmp_list)
	print 
	if function == "max":
		ret_table = [int(item[0]) for item in ret_table]
		ret_table = [[str(max(ret_table))]]
	elif function == "min":
		ret_table = [int(item[0]) for item in ret_table]
		ret_table = [[str(min(ret_table))]]
	elif function == "avg":
		ret_table = [int(item[0]) for item in ret_table]
		ret_table = [[str(float(sum(ret_table))/len(ret_table))]]
	elif function == "sum":
		ret_table = [int(item[0]) for item in ret_table]
		ret_table = [[str(sum(ret_table))]]
	elif function == "distinct":
		ret_table = [','.join(item) for item in ret_table]
		ret_table = f7(ret_table)
		ret_table = [[item] for item in ret_table]
	#print ret_table
	return ret_table

def get_rows(join_table,cond):
		'''
			applies condition on natural-joined table
		'''
		ret_table = []
		#print join_table
		for entry in join_table:
			if eval(cond) == True:
				ret_table.append(entry)

		return ret_table

def print_result(old_select_list,final_table):
	'''
		prints output to the query
	'''
	print old_select_list
	for item in final_table:
		print ','.join(item)

def do_join(selected_columns,join_col):
	'''
		removes redundant column names
	'''
	#print selected_columns,join_col
	selected_columns.remove(join_col)
	return selected_columns


class Database:
	
	def process_field(self,field,table_list,flag=0):
		'''
			processes field as tablename.fieldname
		'''
		function = "NULL"
		if '(' in field and ')' in field:
			tmp_list = field.split('(')
			function = tmp_list[0]
			field = tmp_list[1].strip(')')
		ret = ""
		if len(field.split('.'))==2:
			if flag:
				ret = "entry['" + field + "']"
				return ret
			else:
			 	return function,field 
		if field.isdigit():
			return field
		if field == '*':
			return function,field
		probable_tables = []	
		for table_name in self.bad_schema:
			if table_name not in table_list:
				continue
			if field in self.bad_schema[table_name]:
				probable_tables.append(table_name)
		if len(probable_tables) == 1:
			if flag:
				ret = "entry['" + probable_tables[0] + "." + field + "']"
				return ret
			else:
				ret = probable_tables[0] + "." + field
				return function,ret
		else:
			raise Exception('fieldname '+field+' may be there in no table or multiple tables')

	def do_query(self,select_list, from_list, where_list):
		'''
			performs query on database, returns output string
		'''
		is_join = False
		join_col = ""
		new_select_list = select_list
		select_list_txt = ','.join(select_list)
		func = "NULL"
		for i in range(len(new_select_list)):
			function,new_select_list[i] = self.process_field(new_select_list[i],from_list)
			func = function
		join_table = self.get_join(from_list)
		for i in range(len(where_list)):
			item = where_list[i]
			if item == "AND" or item == "OR":
				where_list[i] = item.lower()
			elif CONDITION in item:
				lhs,rhs = item.split(CONDITION)
				if lhs.isdigit() == False and rhs.isdigit() == False:
					is_join = True
				lhs = self.process_field(lhs,from_list,1)
				rhs = self.process_field(rhs,from_list,1)
				if is_join:
					join_col = rhs.lstrip("entry[").rstrip("]").strip('\'')
				where_list[i] = lhs + CONDITION + CONDITION + rhs
		cond = " ".join(where_list)
		queried_table = get_rows(join_table, cond)
		final_table = select_columns(queried_table,list(set(new_select_list)),func)
		if select_list_txt == '*':
			#print is_join
			if is_join:
				selected_columns = do_join(queried_table[0].keys(),join_col)
			else:
				selected_columns = queried_table[0].keys()
			select_list_txt = ','.join(selected_columns)
		print_result(select_list_txt,final_table)

	def get_join(self,from_list):
		'''
			performs join of given tables
		'''
		ret_table = []
		for table_name in from_list:
			if ret_table == []:
				ret_table = self.tables[table_name]
			else:
				ret_table = merge_tables(ret_table,self.tables[table_name])
		return ret_table

	def load_db(self):
		'''
			loads everything :P
		'''
		metadata = open(TABLE_SCHEMA, 'r').readlines()[1:-1]
		table_list = "".join(metadata).split("%s<end_table>%s<begin_table>" %(L_E, L_E))
		table_list = [ i.split(L_E) for i in table_list]
		table_list = [ filter(lambda x: x, i) for i in table_list]
		for i in range(len(table_list)):
			for j in range(1,len(table_list[i])):
				table_list[i][j] = table_list[i][0]+'.'+table_list[i][j]
		for i in range(len(table_list)):
			data = open(TABLE_VALUES[i], 'r').readlines()
			data = [ clear_stuff(elem) for elem in data ]
			self.schema[table_list[i][0]] = tuple(table_list[i][1:])
			self.bad_schema[table_list[i][0]] = tuple(entry.split('.')[1] for entry in table_list[i][1:])
			self.tables[table_list[i][0]] = []
			for row in data:
				tmp_dict = {}
				for j,row_entry in enumerate(row):
					tmp_dict[self.schema[table_list[i][0]][j]] = int(row_entry)
				self.tables[table_list[i][0]].append(tmp_dict)
		
	def __init__(self):
		self.tables = {}
		self.schema = {}
		self.bad_schema = {}
		self.load_db()

def main():
	DB1 = Database()
	while True:
		select_list, from_list, where_list = get_query()
		DB1.do_query(select_list, from_list, where_list)

if __name__ == "__main__":
	main()