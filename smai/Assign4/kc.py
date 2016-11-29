import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
import sys
import random
from numpy import genfromtxt
my_data = genfromtxt('data1.txt', delimiter=',')

def linearKernel(data):

    kernel = data.T.dot(data)
    return kernel

def polynomialKernel(data, p):

    mat = data.T.dot(data)
    mat = np.add(1, mat)
    kernel = np.power(mat, p)
    return kernel

def gaussianKernel(data, sigma):

    pairwise_dists = squareform(pdist(np.transpose(data), 'sqeuclidean'))
    mat = np.divide(pairwise_dists, -2*sigma*sigma)
    kernel = np.exp(mat)
    return kernel


def kernelClustering(data, numClusters):

    N = data.shape[0]
    K = linearKernel(data.T)
    #K = polynomialKernel(data.T, 5)
    #K = gaussianKernel(data.T, 0.1)
    A = np.zeros((N, numClusters))
    f = np.zeros((1, N))[0]
    for i in range(N):
        f[i] = random.randint(0, numClusters-1)
    f.astype(int)
    for i in range(N):
        A[i, f[i]] = 1
    print A.shape
    change = 1
    while change == 1:
        change = 0
        E = A.dot(np.diag(np.divide(1.0, np.sum(A, axis=0))))
        Z = np.ones((N,1)).dot(np.diagonal(E.T.dot(K.dot(E))).reshape(1,-1)) - 2*K.dot(E)
        ff = np.argmin(Z, axis=1)
        for i in range(numClusters):
            if f[i] != ff[i]:
                A[i, ff[i]] = 1
                A[i, f[i]] = 0
                change = 1
        f = ff
    return f

def main():
    for haah in range(10):
    raw = np.loadtxt('data.txt')
    #raw = genfromtxt('data2.txt', delimiter=',')
    data = raw[:,:-1]
    labels = raw[:,-1].astype(int)
    N = data.shape[0]
    plabels = kernelClustering(data, 2)
    plabels = np.array(plabels)
    total = 0
    for plabel in np.unique(plabels):
        idx = np.where(plabels == plabel)[0]
        vec = labels[idx]
        cnt = np.bincount(vec)
        total += float(np.amax(cnt))
    print "Purity",total/N
    plabels1 = np.where(plabels==1)
    plabels2 = np.where(plabels==0)
    for idx in plabels1[0]:
        plt.plot(data[idx, 0], data[idx, 1], 'ro')
    for idx in plabels2[0]:
        plt.plot(data[idx, 0], data[idx, 1], 'bo')
    plt.show()

if __name__ == '__main__':
    main()