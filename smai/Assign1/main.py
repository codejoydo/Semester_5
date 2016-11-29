from layer import *
import numpy as np
import math

layerType = {0:'input', 1:'hidden', 2:'output'}
nUnits = {0:64, 1:20, 2:10}
nUnitsPrev = {0:64, 1:64, 2:20}

def process():
	'''
		processing stuff
	'''
	TEST_FILE = 'optdigits.tes'
	TRAIN_FILE = 'optdigits.tra'
	# read training data
	with open(TRAIN_FILE) as f:
	    tra_raw = f.readlines()
	# process training data
	tra_list = [map(int, item.strip().split(',')) for item in tra_raw]
	tra_data = np.transpose(np.asmatrix([item[:-1] for item in tra_list]))
	tra_gt = [item[-1] for item in tra_list]
	# normalise training data
	mean_sample = np.divide(tra_data.sum(axis = 1), tra_data.shape[1])
	tra_data = np.subtract(tra_data, mean_sample)
	# read testing data
	with open(TEST_FILE) as f:
	    tes_raw = f.readlines()
	# process training data
	tes_list = [map(int, item.strip().split(',')) for item in tes_raw]
	tes_data = np.transpose(np.asmatrix([item[:-1] for item in tes_list]))
	tes_gt = [item[-1] for item in tes_list]
	# normalise training data
	mean_sample = np.divide(tes_data.sum(axis = 1), tes_data.shape[1])
	tes_data = np.subtract(tes_data, mean_sample)
	return tra_data,tra_gt,tes_data,tes_gt

def main():
	'''
		runs and trains NN
	'''
	#******************************************** TRAINING PART ***********************************
	tra_data, tra_gt, tes_data, tes_gt = process()

	learningRate_a = 3
	learningRate_p = 0.00001 
	nLayers = 3
	nEpochs = 100
	nSamples = tra_data.shape[1]
	layers = []

	for i in range(nLayers):
		tmpLayer = layer(layerType[i], nUnits[i], nUnitsPrev[i])
		layers.append(tmpLayer)

	for epoch in range(nEpochs):

		nCorrect = 0

		for i in range(nSamples):
			# feed forward
			layers[0].feedForward(tra_data[:,i])
			layers[1].feedForward(layers[0].outputVal)
			layers[2].feedForward(layers[1].outputVal)
			
			# check correctly classified
			OutputVec = layers[2].outputVal
			if np.argmax(OutputVec) == tra_gt[i]:
				nCorrect += 1

			# desired output
			desiredOutputVec = np.asmatrix(np.zeros((nUnits[2], 1), np.float))
			desiredOutputVec[tra_gt[i]] = 1.0

			# back prop
			learningRate = learningRate_a * math.pow(i, learningRate_p)
			layers[2].backProp(desiredOutputVec, learningRate)
			layers[1].backProp(layers[2].delta, learningRate, layers[2].weight)

		if epoch % 9 == 0:
			print "Training error after epoch", epoch, "is", (float(nSamples - nCorrect)/nSamples)*100, '%'

	#******************************************** TESTING PART ************************************

	nTestingSamples = tes_data.shape[1]
	nCorrect = 0

	for i in range(nTestingSamples):
		# feed forward
		layers[0].feedForward(tra_data[:,i])
		layers[1].feedForward(layers[0].outputVal)
		layers[2].feedForward(layers[1].outputVal)
			
		# check correctly classified
		OutputVec = layers[2].outputVal
		if np.argmax(OutputVec) == tra_gt[i]:
			nCorrect += 1
			
	print "Testing error is", (float(nTestingSamples - nCorrect)/nTestingSamples)*100, '%'
	np.savetxt("weight_hidden_lyr_lrdecay.csv", layers[1].weight, delimiter=",")
	np.savetxt("weight_output_lyr_lrdecay.csv", layers[2].weight, delimiter=",")
	np.savetxt("hidden_output_lrdecay.csv", layers[1].outputVal, delimiter=",")

if __name__ == "__main__":
	main()