//Joyneel Misra - IIIT Hyderabad
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
	cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
	const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
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
			newnode->keys.PB(key);
			return;
		}
		pair<Node*,Node*> propagate(Node* root,Node* left,Node* right,int key){
			if(root==NULL){
				Node* newnode=new Node;
				newnode->setSize(max_int_p);
				newnode->keys.PB(key);
				newnode->ptrs[0]=left;
				newnode->ptrs[1]=right;
				m_root=newnode;
				return make_pair(newnode,newnode);
			}
			else{
				if(((int)root->keys.size()+1)<=max_leaf_k){
					root->keys.PB(key);
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
					(root->keys).PB(key);
					sort(root->keys.begin(),root->keys.end());
					vector<Node*> ptrs_new;
					int i=0,k=0;
					if(root->keys[0]==key){
						ptrs_new.PB(left);
						ptrs_new.PB(right);
						k++;
						for(i=1;i<(int)root->keys.size();i++){
							ptrs_new.PB(root->ptrs[i]);
						}
					}
					else{
						for(i=0;i<(int)root->keys.size()-1;i++){
							if(root->keys[i+1]==key){
								if(i==0)ptrs_new.PB(root->ptrs[k++]);
								ptrs_new.PB(left);
								k++;
							}
							else if(root->keys[i]==key){ptrs_new.PB(right);k++;}
							else{
								if(i==0)ptrs_new.PB(root->ptrs[k++]);
								ptrs_new.PB(root->ptrs[k++]);
							}
						}
						if(root->keys[i]==key){ptrs_new.PB(right);k++;}
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
							newnode1->keys.PB(root->keys[i]);
							if(i==0)newnode1->ptrs[i]=(root->ptrs[i]);
							newnode1->ptrs[i+1]=(root->ptrs[i+1]);
						}
						if(i>=limit){
							if(i==index_to_prop){
								key_to_prop=root->keys[i];
								newnode2->ptrs[k++]=(root->ptrs[i+1]);
							}
							else{
								newnode2->keys.PB(root->keys[i]);
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
					if(line[i]==','){a.PB(t);t=0;i+=1;j+=1;continue;}
					t=(t*10)+(line[i]-'0');
					i+=1;
				}
				a.PB(t);
				if(hash_table.find(a)==hash_table.end()){
					hash_table[a]=key;
					key+=1;
					if(flag==2){btree->insert(btree->lookUp(btree->m_root,key-1),key-1);iterate_next(btree->block_size);}
				}
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
	return 0;
}
