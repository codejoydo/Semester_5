#!/bin/bash

python code/main.py <<end_limit
3 100MB_20percent 1MB btree
end_limit

python code/main.py <<end_limit
3 100MB_20percent 1MB hash
end_limit

python code/main.py <<end_limit
3 1MB_50percent 1MB btree
end_limit

python code/main.py <<end_limit
3 1MB_50percent 1MB hash
end_limit

python code/main.py <<end_limit
5 100MB_20percent 2MB btree
end_limit

python code/main.py <<end_limit
5 100MB_20percent 2MB hash
end_limit

python code/main.py <<end_limit
5 1MB_50percent 2MB btree
end_limit

python code/main.py <<end_limit
5 1MB_50percent 2MB hash
end_limit

python code/main.py <<end_limit
10 100MB_20percent 0.1MB btree
end_limit

python code/main.py <<end_limit
10 100MB_20percent 0.1MB hash
end_limit

python code/main.py <<end_limit
10 1MB_50percent 0.1MB btree
end_limit

python code/main.py <<end_limit
10 1MB_50percent 0.1MB hash
end_limit
