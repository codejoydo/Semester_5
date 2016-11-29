from layer1 import *
import numpy as np

layerType = {0:'input', 1:'hidden', 2:'output'}
nUnits = {0:64, 1:20, 2:10}
nUnitsPrev = {0:64, 1:64, 2:20}

def process():
	'''
		processing stuff
	'''
	TEST_FILE = 'optdigits.tes'
	TRAIN_FILE = 'optdigits.tra'
	with open(TRAIN_FILE) as f:
	    tra_raw = f.readlines()
	tra_list = [map(int, item.strip().split(',')) for item in tra_raw]
	tra_data = np.transpose(np.asmatrix([item[:-1] for item in tra_list]))
	tra_gt = [item[-1] for item in tra_list]
	mean_sample = np.divide(tra_data.sum(axis = 1), tra_data.shape[1])
	tra_data = np.subtract(tra_data, mean_sample)
	return tra_data,tra_gt

def main():
	'''
		runs and trains NN
	'''

	tra_data,tra_gt = process()

	learningRate = 1
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
			layers[2].backProp(desiredOutputVec, learningRate)
			layers[1].backProp(layers[2].delta, learningRate, layers[2].weight)

		if epoch % 1 == 0:
			print "error is", (float(nSamples - nCorrect)/nSamples)*100


if __name__ == "__main__":
	main()