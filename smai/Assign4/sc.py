import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
import sys
from numpy import genfromtxt


def getW(data, numNeighbours):

    pairwise_dists = squareform(pdist(data, 'sqeuclidean'))
    return np.nan_to_num(np.exp(-pairwise_dists))

def findEigenGap(vec):

    diff = np.ediff1d(vec)
    return np.argmin(diff)

def spectralClustering(data, numNeighbours, numClusters):

    N = data.shape[0]
    W = getW(data, numNeighbours)
    print W
    D = W.sum(axis = 0) * np.identity(N)
    print W[:,0].sum(axis = 0)
    L = D - W
    eigenValues,eigenVectors = la.eig(L)
    idx = eigenValues.argsort()
    kcrit = findEigenGap(eigenValues)
    k = 5
    idx = idx[:k] # ????
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx].reshape(-1,k)
    print eigenVectors
    kmeans = KMeans(n_clusters=2, random_state=0).fit(eigenVectors)
    label = kmeans.labels_
    return label

def main():

    raw = np.loadtxt('data.txt')
    #raw = genfromtxt('data2.txt', delimiter=',')
    data = raw[:,:-1]
    labels = raw[:,-1].astype(int)
    plabels = spectralClustering(data, 10, 2)
    plabels = np.array(plabels)
    print plabels
    N = data.shape[0]
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