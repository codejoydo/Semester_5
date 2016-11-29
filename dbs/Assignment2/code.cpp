

#include<bits/stdc++.h>
using namespace std;
#define pb(x) push_back(x)
#define ULL unsigned long long int
#define LL long long int

map < int , set < vector < int > > > hash_function;

int global;

void print()
{
	//cout << "GONE in this " << global << endl;
	global++;
	return;
}

// B-Tree code taken from Internet
//////////////////////////////////////////////////////   BTREE STARTS  ////////////////////////////////////////////////

// A BTree node
class BTreeNode
{
	ULL *keys;  // An array of keys
	int t;      // Minimum degree (defines the range for number of keys)
	BTreeNode **C; // An array of child pointers
	int n;     // Current number of keys
	bool leaf; // Is true when node is leaf. Otherwise false
	public:
	BTreeNode(int _t, bool _leaf);   // Constructor

	void insertNonFull(ULL k);

	void splitChild(int i, BTreeNode *y);

	void traverse();

	BTreeNode *search(ULL k);   // returns NULL if k is not present.

	friend class BTree;
};
class BTree
{
	BTreeNode *root; // Pointer to root node
	int t;  // Minimum degree
	public:
	BTree(int _t)
	{  root = NULL;  t = _t; }

	void traverse()
	{  if (root != NULL) root->traverse(); }

	BTreeNode* search(ULL k)
	{  return (root == NULL)? NULL : root->search(k); }

	void insert(ULL k);
};

BTreeNode::BTreeNode(int t1, bool leaf1)
{
	t = t1;
	leaf = leaf1;
	keys = new ULL[2*t-1];
	C = new BTreeNode *[2*t];
	n = 0;
}

BTreeNode *BTreeNode::search(ULL k)
{
	int i = 0;
	while (i < n && k > keys[i])
		i++;

	if (keys[i] == k)
		return this;

	if (leaf == true)
		return NULL;

	return C[i]->search(k);
}

void BTree::insert(ULL k)
{
	if (root == NULL)
	{
		// Allocate memory for root
		root = new BTreeNode(t, true);
		root->keys[0] = k;  // Insert key
		root->n = 1;  // Update number of keys in root
	}
	else // If tree is not empty
	{
		if (root->n == 2*t-1)
		{
			BTreeNode *s = new BTreeNode(t, false);
			s->C[0] = root;
			s->splitChild(0, root);
			int i = 0;
			if (s->keys[0] < k)
				i++;
			s->C[i]->insertNonFull(k);
			root = s;
		}
		else  // If root is not full, call insertNonFull for root
			root->insertNonFull(k);
	}
}

void BTreeNode::insertNonFull(ULL k)
{
	int i = n-1;
	if (leaf == true)
	{
		while (i >= 0 && keys[i] > k)
		{
			keys[i+1] = keys[i];
			i--;
		}
		keys[i+1] = k;
		n = n+1;
	}
	else // If this node is not leaf
	{
		while (i >= 0 && keys[i] > k)
			i--;
		if (C[i+1]->n == 2*t-1)
		{
			splitChild(i+1, C[i+1]);
			if (keys[i+1] < k)
				i++;
		}
		C[i+1]->insertNonFull(k);
	}
}

void BTreeNode::splitChild(int i, BTreeNode *y)
{
	BTreeNode *z = new BTreeNode(y->t, y->leaf);
	z->n = t - 1;
	for (int j = 0; j < t-1; j++)
		z->keys[j] = y->keys[j+t];
	if (y->leaf == false)
	{
		for (int j = 0; j < t; j++)
			z->C[j] = y->C[j+t];
	}
	y->n = t - 1;
	for (int j = n; j >= i+1; j--)
		C[j+1] = C[j];
	C[i+1] = z;
	for (int j = n-1; j >= i; j--)
		keys[j+1] = keys[j];
	keys[i] = y->keys[t-1];
	n = n + 1;
}


///////////////////////////////////////////////////////// B TREE ENDS /////////////////////////////////////////////////////////


unsigned long hashit(string str)
{
	unsigned long hash = 5381;

	for(string::iterator it=str.begin();it!=str.end();it++)
		hash = ((hash << 5) + hash) + *it; /* hash * 33 + character */

	return hash;
}



void Getnext(string relation_file_name,int relations,int m, int type_index)
{
	ifstream inp(relation_file_name);
	string line;
	int distinct_string=0;
	BTree t(3);
	while(getline(inp,line))
	{
		string ints;
		stringstream tuple;
		tuple << line;
		vector < int > temp;
		int sum1=0;
		while(tuple>>ints)
		{
			int y=stoi(ints);
			sum1+=y;
			sum1%=m;
			temp.pb(y);
			print();
		}
		if(type_index==0)
		{
			if(hash_function[sum1].find(temp)==hash_function[sum1].end())
			{
				hash_function[sum1].insert(temp);
				cout<<line<<endl;
			}
		}
		else	
		{
			ULL hash_val=hashit(line);
			if(t.search(hash_val) == NULL)
			{
				cout << line << endl;
				t.insert(hash_val);
				print();
			}
		}
	}
	inp.close();
	return;
}

void open(string relation_file_name,int relations,int m, int type_index)
{
	return;
}

void distinct(string relation_file_name,int relations,int m, int type_index)
{
	open(relation_file_name,relations,m,type_index);
	Getnext(relation_file_name,relations,m,type_index);
	return;
}


int main( int argc , char * argv[])
{
	string relation_file_name =  argv[1];
	int relations = stoi(argv[2]);
	int m = stoi(argv[3]); 
	string index=argv[4];
	int type_index=1;
	if(index[0]=='h')
		type_index=0;
	else
		type_index=1;
	distinct(relation_file_name,relations,m,type_index);
	return 0;
}


