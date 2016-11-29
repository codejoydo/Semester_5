import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import sys
from numpy import genfromtxt
my_data = genfromtxt('data1.txt', delimiter=',')

def similarity(a, b):
    
    return np.nan_to_num(np.divide(1, 1+la.norm(a-b)))

def merge(dsu, x, y):

    px = find(dsu, x)
    py = find(dsu, y)
    if px == py:
        return
    dsu[py-1] = px

def find(dsu, x):

    if dsu[x-1] == x:
        return x
    dsu[x-1] = find(dsu, dsu[x-1])
    return dsu[x-1]

def agglomerativeClustering(data, numClusters):
    
    inf = -1
    N = data.shape[0]
    C = np.zeros((N, N)) 
    dsu = range(1, N+1)
    for n in range(N):
        for i in range(N):
            C[n][i] = similarity(data[n,:], data[i,:])
    C = C + inf * np.identity(N)
    for k in range(N - numClusters):
        tmp =  np.where(C == np.max(C))
        i = tmp[0][0]
        m = tmp[1][0]
        C[i, m] = 0
        C[m, i] = 0
        merge(dsu, i+1, m+1)
        for j in range(N):
            C[i, j] = max(C[i, j], C[m, j])
            C[j, i] = C[i, j]
        C[m, :] = C[m, :] * 0 
        C[:, m] = C[:, m] * 0 
    for i in range(N):
        dsu[i] = find(dsu, i+1)
    return dsu

def main():

    raw = np.loadtxt('data.txt')
    #raw = genfromtxt('data2.txt', delimiter=',')
    data = raw[:,1:-1]
    labels = raw[:,-1].astype(int)
    N = data.shape[0]
    plabels = agglomerativeClustering(data, 2)
    plabels = np.array(plabels)
    total = 0
    for plabel in np.unique(plabels):
        idx = np.where(plabels == plabel)[0]
        vec = labels[idx]
        cnt = np.bincount(vec)
        total += float(np.amax(cnt))
    print "Purity",total/N
    '''plabels1 = np.where(plabels==1)
    plabels2 = np.where(plabels==26)
    for idx in plabels1[0]:
        plt.plot(data[idx, 0], data[idx, 1], 'ro')
    for idx in plabels2[0]:
        plt.plot(data[idx, 0], data[idx, 1], 'bo')
    plt.show()'''

if __name__ == '__main__':
    main()