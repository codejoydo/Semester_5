import numpy as np
import csv
import pdb
from collections import defaultdict

def nb_train(train_data,plabel,nlabel):
    num_attributes = len(train_data[0]) - 1
    pdict = [defaultdict(float) for x in range(num_attributes)]
    ndict = [defaultdict(float) for x in range(num_attributes)]
    plist = [0]*num_attributes
    nlist = [0]*num_attributes
    num_psample = 0
    num_nsample = 0
    for row in train_data:
        # count number of positive and negative labels
        class_label = row[-1]
        if class_label == plabel:
            num_psample += 1
            cdictlist = pdict
            clist = plist
        elif class_label == nlabel:
            num_nsample += 1
            cdictlist = ndict
            clist = nlist

        # compute feature freq and attr freq for each class
        feat_vec = row[:-1]
        ind = -1
        for feat in feat_vec:
            ind += 1
            if feat == '?':
                continue
            cdictlist[ind][feat] += 1
            clist[ind] += 1

    # compute priors
    priors = [np.log(float(num_psample)/(num_psample + num_nsample)), np.log(float(num_nsample)/(num_psample + num_nsample))]
    # take log of probabilities
    for i in range(num_attributes):
        for feat in pdict[i]:
            if pdict[i][feat]!=0:
                pdict[i][feat] = np.log(pdict[i][feat]/plist[i])
            else:
                pdict[i][feat] = np.log(0.000000001)
        for feat in ndict[i]:
            if ndict[i][feat]!=0:
                ndict[i][feat] = np.log(ndict[i][feat]/nlist[i])
            else:
                ndict[i][feat] = np.log(0.000000001)
    return [priors, pdict, ndict]    

def nb_predict(priors, pdict, ndict, test_data, plabel, nlabel):
    classified = 0
    misclassified = 0
    ans = 0
    
    for row in test_data:
    	# compute posterior probability for each test sample against each class
        ground_truth = row[-1]
        feat_vec = row[:-1]
        ind = -1
        pcumulative = priors[0]
        ncumulative = priors[1]
        for feat in feat_vec:
            ind += 1
            if feat=='?':
                continue
            pcumulative += pdict[ind][feat]
            ncumulative += ndict[ind][feat]
        # predict label based on posterior probabilities
        if pcumulative > ncumulative:
            predicted = plabel
        else:
            predicted = nlabel
        # check against ground truth
        if predicted == ground_truth:
            classified += 1
        else:
            misclassified += 1
    print "Accuracy",float(classified)/(classified+misclassified)," over ", classified + misclassified, " samples."
    return classified, misclassified

total_classified = 0
total_misclassified = 0
# process data
raw_data = csv.reader(open("census-income.data"))
data0 = []
for i in list(raw_data):
    data0.append([item.strip() for item in i])
data = np.array(data0)
data = data[:,[2,3,4,41]]
np.random.shuffle(data)
data = data[:10000]
acc = []
for i in range(10):
    np.random.shuffle(data)
    train_data = data[0:5000]
    test_data = data[5001:10000]
    [priors, pdict, ndict] = nb_train(train_data,'50000+.','- 50000.')
    [classified, misclassified] = nb_predict(priors, pdict, ndict, test_data, '50000+.','- 50000.')
    total_classified += classified
    total_misclassified += misclassified
    acc.append(float(classified)/(classified+misclassified))
acc = np.array(acc)
mean_acc = float(total_classified)/(total_classified+total_misclassified)
sd = np.std(acc)
print "Mean Accuracy",mean_acc,"Standard Deviation",sd