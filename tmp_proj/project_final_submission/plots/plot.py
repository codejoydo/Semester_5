import scipy.interpolate as sp
import numpy as np
import pylab

arr = [10,80,40]
lgnd = ['topics='+str(elem) for elem in arr]
for i in range(len(arr)):
    with open('plot'+str(arr[i])+'_2') as f:
        c = f.readlines()

    y = np.array([float(i) for i in c[0].split()])
    x = np.array([float(i) for i in c[1].split()])

    fl = sp.interp1d(x, y,kind='linear')

    xnew = np.linspace(0, 100, 20)
    pylab.subplot(111)
    pylab.plot(xnew, fl(xnew))
        
pylab.legend(['baseline','LDA, topics=40','Deep CNN, topics=40'], loc='lower right')
pylab.show()