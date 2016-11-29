import numpy as np
from numpy import linalg as LA
from scipy.spatial.distance import pdist, squareform
from sklearn import svm, preprocessing
from sklearn.model_selection import cross_val_score

def linearKernel(data1, data2):

    kernel = np.dot(np.transpose(data1), data2)
    return kernel

def polynomialKernel(data1, data2, p):

    mat = np.dot(np.transpose(data1), data2)
    mat = np.add(1, mat)
    kernel = np.power(mat, p)
    return kernel

def gaussianKernel(data1, data2, sigma):

    pairwise_dists = np.zeros((data1.shape[1], data2.shape[1]))
    for i in range(data1.shape[1]):
        for j in range(data2.shape[1]):
            pairwise_dists[i,j] = (LA.norm(data1[:,i]-data2[:,j]))**2
    # pairwise_dists = squareform(pdist(np.transpose(data), 'euclidean'))
    mat = np.divide(pairwise_dists, -2*sigma*sigma)
    kernel = np.exp(mat)
    return kernel

def kernelPCA(data, kerneltype = 'linear', p = 2, sigma = 0.5, numeig = 1):

    ''' compute n x n Gram Matrix K using a kernel function '''
    if kerneltype == 'linear':
        kernel = linearKernel(data, data)
    elif kerneltype == 'polynomial':
        kernel = polynomialKernel(data, data, p)
    elif kerneltype == 'gaussian':
        kernel = gaussianKernel(data, data, sigma)
    else:
        print "Wrong kernel type"
        raise

    ''' normalise kernel matrix '''
    N = data.shape[1]
    oneN = np.divide(np.ones((N, N)), N)
    kernel = kernel - np.dot(oneN, kernel) - np.dot(kernel, oneN) + np.dot(np.dot(oneN, kernel), oneN)

    ''' compute eigen-(values/vectors) of K '''
    eigenValues,eigenVectors = LA.eig(kernel)

    ''' sort eigen vectors according to corresponding eigen values '''
    idx = eigenValues.argsort()[::-1]
    idx = idx[:numeig]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]

    ''' normalise the eigen vectors '''
    eigenVectors = np.divide(eigenVectors, eigenValues[None, :])

    ''' project data points into lower dimensional space '''
    projectedData = np.dot(np.transpose(eigenVectors), kernel) 

    return [projectedData, eigenVectors]

def kernelLDA(data, labels, kerneltype = 'linear', p = 2, sigma = 0.5):

    ''' compute n x n Gram Matrix K using a kernel function '''
    if kerneltype == 'linear':
        kernel = linearKernel(data, data)
    elif kerneltype == 'polynomial':
        kernel = polynomialKernel(data, data, p)
    elif kerneltype == 'gaussian':
        kernel = gaussianKernel(data, data, sigma)
    else:
        print "Wrong kernel type"
        raise

    ''' compute number of elements in each class '''
    idx1 = np.argwhere(labels == 1)
    idx2 = np.argwhere(labels == -1)
    l1 = np.prod(idx1.shape)
    l2 = np.prod(idx2.shape)
    print l1, l2, kernel.shape
    
    ''' seperate kernels of 2 classes '''
    K1 = kernel[:, idx1]
    K2 = kernel[:, idx2]
    K1 = K1[:,:,0]
    K2 = K2[:,:,0]

    ''' compute Mi's '''
    M1 = np.divide(K1.sum(axis=1), l1)
    M2 = np.divide(K2.sum(axis=1), l2)

    ''' compute N matrix '''
    I1 = np.subtract(np.identity(l1), np.divide(np.ones((l1, l1)), l1))
    I2 = np.subtract(np.identity(l2), np.divide(np.ones((l2, l2)), l2))
    N = np.add(np.dot(np.dot(K1, I1), np.transpose(K1)),np.dot(np.dot(K2, I2), np.transpose(K2)))

    ''' check if N is invertible '''
    if N.shape[0] != LA.matrix_rank(N):
        #print LA.matrix_rank(N)
        eps = 0.000000001 * np.amin(N)
        N = np.add(N,np.dot(eps,np.identity(N.shape[0])))

    ''' compute alpha vector '''
    alpha = np.dot(LA.inv(N), np.subtract(M1, M2))

    ''' project data to one dimensional space '''
    #projectedData = np.transpose(np.dot(kernel, alpha))
    projectedData = np.dot(np.transpose(alpha), kernel) 

    return [projectedData, alpha]

def train(data, labels, vdata, vlabels):

    classifier = svm.SVC()
    #classifier = svm.LinearSVC()
    
    #scores = cross_val_score(classifier, data, labels, cv=10)
    #print "Accuracy: %0.9f (+/- %0.9f)" % (scores.mean(), scores.std() * 2)
    
    classifier.fit(preprocessing.scale(data), labels)
    pvlabels = classifier.predict(preprocessing.scale(vdata))
    error = np.mean( vlabels != pvlabels )
    print "Accuracy: %0.9f" % (1-error)

def main():
    data = np.loadtxt('data/madelon_train.data')
    labels = np.loadtxt('data/madelon_train.labels')
    vdata = np.loadtxt('data/madelon_valid.data')
    vlabels = np.loadtxt('data/madelon_valid.labels')
    #data = np.loadtxt('data/arcene_train.data')
    #labels = np.loadtxt('data/arcene_train.labels')
    #vdata = np.loadtxt('data/arcene_valid.data')
    #vlabels = np.loadtxt('data/arcene_valid.labels')
    data = np.transpose(data)
    vdata = np.transpose(vdata)

    data = data[:,1:601]
    print data.shape
    print vdata.shape
    labels = labels[1:601]

    for kk in range(10, 110,10):
            
        [PCAdata, eigenVectors] = kernelPCA(data, 'gaussian', sigma=10000, p=3,numeig = kk)
        [LDAdata, alpha] = kernelLDA(data, labels, 'gaussian', sigma=10000,p=3)
        
        ''' create kernel for validation data and then normalise it '''    
        N1 = data.shape[1]
        N2 = vdata.shape[1]
        kernel = linearKernel(vdata, data)#, 3)
        kernelt = linearKernel(data, data)#, 3)
        oneN2 = np.divide(np.ones((N1, N1)), N1)
        kernelt = kernelt - np.dot(oneN2, kernelt) - np.dot(kernelt, oneN2) + np.dot(np.dot(oneN2, kernelt), oneN2)
        oneN = np.divide(np.ones((N2, N1)), N1)
        oneN1 = np.divide(np.ones((N1, N1)), N1)
        #print kernel.shape, oneN.shape, oneN1.shape, kernelt.shape
        kernel1 = kernel - np.dot(oneN, kernelt) - np.dot(kernel, oneN1) + np.dot(np.dot(oneN, kernelt), oneN1)

        PCAvdata = np.dot(np.transpose(eigenVectors), np.transpose(kernel))
        LDAvdata = np.dot(np.transpose(alpha), np.transpose(kernel))
       # train(np.transpose(data), labels, np.transpose(vdata), vlabels)
        train(np.transpose(PCAdata), labels, np.transpose(PCAvdata), vlabels)
        #train(np.transpose(LDAdata).reshape(-1,1), labels, np.transpose(LDAvdata).reshape(-1,1), vlabels)


if __name__ == '__main__':
    main()