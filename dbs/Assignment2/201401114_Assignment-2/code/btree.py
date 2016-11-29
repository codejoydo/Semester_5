#/bin/python
global argv,filename,n_attr,mem_blocks,M, t
global fp, op, min_size_buffer, max_size_buffer, answer, block_size, hash

class BTreeNode:
	def __init__(self, t=3, isLeaf=True):
		self.t = t
		self.isLeaf = isLeaf
		self.n = 0
		self.keys = []
		self.C = []

	def search(self, k):
		i=0
		while i<n and k>keys[i]:
			i+=1

		if i!=n and k==keys[i]:
			return self

		if isLeaf is True:
			return None

		return C[i].search(k)

	def insertNonFull(self, k):
		i = n-1
		while i>=0 and k<keys[i]:
			i-=1
		
		if isLeaf is True:	
			keys.insert(i+1,k)
			n=n+1
		
		else:
			if C[i+1].n == 2*t-1:
				splitChild(i+1, C[i+1])
				if keys[i+1]<k:
					i=i+1
			C[i+1].insertNonFull(k)

	def splitChild(i, y):
		z = BTreeNode(y.t, y.isLeaf)
		z.n = t-1

		for j in range(t-1):
			z.keys[j] = y.keys[j+t]

		if y.isLeaf is False:
			for j in range(t):
				z.C[j] = y.C[j+t]
		y.n = t-1

		C.insert(i+1,z)
		keys.insert(i, y.keys(t-1))
		n=n+1



class BTree:
	def __init__(self, t):
		self.t = t;
		self.root = None

	def search(self, k):
		if root is None:
			return None
		else:
			return root.search(k)

	def insertTree(self,k):
		if root is None:
			root = BTreeNode(t, True)
			root.keys.insert(0, k)
			root.n=1
		else:
			if root.n == 2*t-1:
				s = BTreeNode(t, False)
				s.C.insert(0, root)
				s.splitChild(0, root)
				i=0
				if s.keys[0] <k:
					i+=1
				s.C[i].insertNonFull(k)
				root = s
			else:
				root.insertNonFull(k)


#tr = BTree(3)