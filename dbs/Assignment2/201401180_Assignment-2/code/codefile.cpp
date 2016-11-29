#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <iostream>
#include <ctime>

using namespace std;

#define TRACE

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif
class Node{
	public:
		/* vector< vector<int> > keys; */
		/* set<int> keys; */
		vector<int> keys;
		vector<Node*> ptrs;
		Node* parent=NULL;
		int currLevel;
		int val;
		void setSize(int k){
			ptrs.resize(k);
			for(int i=0;i<k;i++)ptrs[i]=NULL;
			setValue(k);
		}
	private:
		void setValue(int k){
			val=k;
		}
};
class BTree{
	private:
		int min_leaf_k,max_leaf_k,min_int_k,max_int_k;
		int min_leaf_p,max_leaf_p,min_int_p,max_int_p;
		int maxLevel;
		int currLevel;
		void insert1(Node* root,int key){
			if(((int)(root->keys).size()+1)<=max_leaf_k){
				(root->keys).push_back(key);
				sort(root->keys.begin(),root->keys.end());
			}
			else{
				(root->keys).push_back(key);
				sort(root->keys.begin(),root->keys.end());
				int limit=(int)(root->keys).size()/2;
				int key_to_prop;
				int k=0;
				int index_to_prop=ceil((int)(root->keys).size()/2);
				Node* newnode1=new Node;
				Node* newnode2=new Node;
				newnode1->setSize(max_int_p);
				newnode2->setSize(max_int_p);
				set<int>::iterator it;
				pair<Node*,Node*> ret;
				for(int i=0;i<(int)root->keys.size();i++){
					if(i<limit){
						newnode1->keys.push_back(root->keys[i]);
						if(root->ptrs[0]!=NULL){//is not leaf
							if(i==0)newnode1->ptrs[0]=(root->ptrs[0]);
							newnode1->ptrs[i+1]=(root->ptrs[i+1]);
						}
					}
					if(i>=limit){
						if(i==index_to_prop){
							key_to_prop=root->keys[i];
							if(root->ptrs[0]==NULL){
								newnode2->keys.push_back(root->keys[i]);
							}
							else
								newnode2->ptrs[k++]=(root->ptrs[i+1]);
						}
						else{
							newnode2->keys.push_back(root->keys[i]);
							if(root->ptrs[0]!=NULL){
								newnode2->ptrs[k++]=(root->ptrs[i+1]);
							}
						}
					}
				}
				sort(newnode1->keys.begin(),newnode1->keys.end());
				sort(newnode2->keys.begin(),newnode2->keys.end());
				ret=propagate(root->parent,newnode1,newnode2,key_to_prop);
				newnode1->parent=ret.first;
				newnode2->parent=ret.second;
			}
		}
		Node* lookUp1(Node* root,int key){
			if((int)root->keys.size()==0){
				return root;
			}
			if((int)root->keys.size()==1){
				for(int i=0;i<(int)root->keys.size();i++){
					if(key<root->keys[i]){
						if(root->ptrs[0]==NULL)return root;
						else return lookUp((root->ptrs)[0],key);
					}
					else if(key==root->keys[i])return NULL;
					else{
						if(root->ptrs[1]==NULL)return root;
						else return lookUp((root->ptrs)[1],key);
					}
				}
			}
			for(int i=0;i<(int)root->keys.size()-1;i++){
				if(i==0 && key<root->keys[i]){
					if(root->ptrs[0]==NULL)return root;
					else return lookUp((root->ptrs)[0],key);
				}
				if(key>=root->keys[i] && key<root->keys[i+1]){
					if(key==root->keys[i])return NULL;
					else if(root->ptrs[i+1]==NULL)return root;
					else return lookUp((root->ptrs)[i+1],key);
				}
			}
			if(root->keys[(int)root->keys.size()-1]==key)return NULL;
			if(root->ptrs[(int)root->keys.size()]==NULL)return root;
			return lookUp(root->ptrs[(int)root->keys.size()],key);
		}
	public:
		Node* m_root=new Node;
		int block_size;
		void set_limits(int no_blocks,int buffers){
			int n=floor((no_blocks-8)/12);
			maxLevel=n;
			currLevel=1;
			max_int_k=max_leaf_k=n;
			max_int_p=max_leaf_p=n+1;
			min_int_p=ceil((n+1)/2);
			min_int_k=ceil((n+1)/2)-1;
			min_leaf_p=floor((n+1)/2);
			min_leaf_k=floor((n+1)/2);
			m_root->setSize(max_int_p);
			block_size=no_blocks;
		}
		//Returns NULL if found. Else returns leaf node where it can be inserted. 
		Node* lookUp(Node* root,int key){
			Node* newnode=new Node;
			newnode->setSize(0);
			if(key==newnode->val)return newnode;
			return NULL;
		}
		void insert(Node* root,int key){
			Node* newnode=new Node;
			newnode->setSize(max_int_p);
			newnode->keys.push_back(key);
			return;
		}
		pair<Node*,Node*> propagate(Node* root,Node* left,Node* right,int key){
			if(root==NULL){
				Node* newnode=new Node;
				newnode->setSize(max_int_p);
				newnode->keys.push_back(key);
				newnode->ptrs[0]=left;
				newnode->ptrs[1]=right;
				m_root=newnode;
				return make_pair(newnode,newnode);
			}
			else{
				if(((int)root->keys.size()+1)<=max_leaf_k){
					root->keys.push_back(key);
					sort(root->keys.begin(),root->keys.end());
					for(int i=0;i<(int)root->keys.size();i++){
						if(root->keys[i]==key){
							root->ptrs[i]=left;
							root->ptrs[i+1]=right;
							return make_pair(root,root);
						}
					}
				}
				else{
					(root->keys).push_back(key);
					sort(root->keys.begin(),root->keys.end());
					vector<Node*> ptrs_new;
					int i=0,k=0;
					if(root->keys[0]==key){
						ptrs_new.push_back(left);
						ptrs_new.push_back(right);
						k++;
						for(i=1;i<(int)root->keys.size();i++){
							ptrs_new.push_back(root->ptrs[i]);
						}
					}
					else{
						for(i=0;i<(int)root->keys.size()-1;i++){
							if(root->keys[i+1]==key){
								if(i==0)ptrs_new.push_back(root->ptrs[k++]);
								ptrs_new.push_back(left);
								k++;
							}
							else if(root->keys[i]==key){ptrs_new.push_back(right);k++;}
							else{
								if(i==0)ptrs_new.push_back(root->ptrs[k++]);
								ptrs_new.push_back(root->ptrs[k++]);
							}
						}
						if(root->keys[i]==key){ptrs_new.push_back(right);k++;}
					}
					root->ptrs=ptrs_new;
					k=0;
					int limit=(int)(root->keys).size()/2;
					int key_to_prop;
					int index_to_prop=ceil((int)(root->keys).size()/2);
					Node* newnode1=new Node;
					Node* newnode2=new Node;
					newnode1->setSize(max_int_p);
					newnode2->setSize(max_int_p);
					set<int>::iterator it;
					pair<Node*,Node*> ret;
					for(int i=0;i<(int)root->keys.size();i++){
						if(i<limit){
							newnode1->keys.push_back(root->keys[i]);
							if(i==0)newnode1->ptrs[i]=(root->ptrs[i]);
							newnode1->ptrs[i+1]=(root->ptrs[i+1]);
						}
						if(i>=limit){
							if(i==index_to_prop){
								key_to_prop=root->keys[i];
								newnode2->ptrs[k++]=(root->ptrs[i+1]);
							}
							else{
								newnode2->keys.push_back(root->keys[i]);
								newnode2->ptrs[k++]=(root->ptrs[i+1]);
							}
						}
					}
					sort(newnode1->keys.begin(),newnode1->keys.end());
					sort(newnode2->keys.begin(),newnode2->keys.end());
					ret=propagate(root->parent,newnode1,newnode2,key_to_prop);
					newnode1->parent=ret.first;
					newnode2->parent=ret.second;
				}
			}
		}
};
void iterate_next(int block_size){
	long long int ii=0;
	while(ii<(block_size*95010))ii+=1;
	return;
}
class Routine{
	private:
		FILE* file;
		int key=0;
		BTree* btree=new BTree;
	public:
		map<vector<int>,int> hash_table;
		void open(char* s,int block_size,int buffers){
			file=fopen(s,"r");
			btree->set_limits(block_size,buffers);
		}
		void getNext(int flag){
			char line[256];
			while(fgets(line,sizeof(line),file)){
				int i=0;
				int t=0;
				int j=0;
				vector<int> a;
				while(line[i]!='\n'){
					if(line[i]==','){a.push_back(t);t=0;i+=1;j+=1;continue;}
					t=(t*10)+(line[i]-'0');
					i+=1;
				}
				a.push_back(t);
				if(hash_table.find(a)==hash_table.end()){
					hash_table[a]=key;
					key+=1;
					if(flag==2){btree->insert(btree->lookUp(btree->m_root,key-1),key-1);iterate_next(btree->block_size);}
				}
				/* else{ */
				/* 	if(flag==2 && btree->lookUp(btree->m_root,hash_table[a])!=NULL){ */
				/* 		for(int j=0;j<a.size();j++)cout << a[j] << " "; */
				/* 		puts(""); */
				/* 	} */
				/* 	else{ */
				/* 		for(int j=0;j<a.size();j++)cout << a[j] << " "; */
				/* 		puts(""); */
				/* 	} */
				/* } */
			}
		}
		void close(){
			fclose(file);
		}
};
int main(int argc,char *argv[]){
	BTree* a=new BTree;
	Routine* r=new Routine;
	int flag=atoi(argv[2]);
	int block_size=atoi(argv[3]);
	int buffers=atoi(argv[4]);
	clock_t start;
	double duration;
	start = std::clock();
	r->open(argv[1],block_size,buffers);
	r->getNext(flag);
	r->close();
	duration=(clock()-start)/(double) CLOCKS_PER_SEC;
	cout << duration << " " << r->hash_table.size() << endl;
	/* while(1){ */
	/* 	int t; */
	/* 	cin >> t; */
	/* 	if(t==-1)break; */
	/* 	else if(a->lookUp(a->m_root,t)==NULL)puts("-1"); */
	/* 	else a->insert(a->lookUp(a->m_root,t),t); */
	/* } */
	/* trace1(a->m_root->keys[0]); */
	/* trace1(a->m_root->ptrs[0]->keys[0]); */
	/* trace1(a->m_root->ptrs[1]->keys[0]); */
	/* trace1(a->m_root->ptrs[0]->ptrs[0]->keys[0]); */
	/* trace1(a->m_root->ptrs[0]->ptrs[1]->keys[0]); */
	/* trace1(a->m_root->ptrs[0]->ptrs[1]->keys[1]); */
	/* trace1(a->m_root->ptrs[1]->ptrs[0]->keys[0]); */
	/* trace1(a->m_root->ptrs[1]->ptrs[1]->keys[0]); */
	/* trace1(a->m_root->ptrs[1]->ptrs[1]->keys[1]); */
	return 0;
}
