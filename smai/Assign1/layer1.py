import numpy as np

class layer:

	def __init__ (self, layerType, nUnits, nUintsPrev):
		'''
			NN layer constructor
		'''
		self.layerType = layerType
		if self.layerType == 'input':
			self.weight = np.asmatrix(np.identity(nUnits))
			self.bias = np.asmatrix(np.zeros((nUnits,1), np.float))
		else:
			self.weight = np.asmatrix(np.random.normal(0, np.sqrt(1.0/nUintsPrev), (nUnits, nUintsPrev)))
			self.bias = np.asmatrix(np.random.rand(nUnits, 1))
		self.netActiv = np.asmatrix(np.zeros((nUnits, 1), np.float))
		self.outputVal = np.asmatrix(np.zeros((nUnits, 1), np.float))
		self.inputVal = np.asmatrix(np.zeros((nUnits, 1), np.float))
		self.delta = np.asmatrix(np.zeros((nUnits, 1), np.float))

	def feedForward (self, inputVal): # inputVal is same as output of previous layer
		'''
			calculates netActiv and outputVal of the layer
		'''
		self.inputVal = inputVal
		self.netActiv = np.add(np.dot(self.weight, inputVal), self.bias)
		if self.layerType == 'input':
			self.outputVal = self.netActiv
		else:
			self.outputVal = sigmoid(self.netActiv)

	def backProp (self, nextVal, learningRate, nextWeight = None):
		'''
			calculates delta, updates weight and bias of layer  
		'''
		# calculate delta
		if self.layerType == 'output':
			desiredOutputVal = nextVal
			costDerivative = np.subtract(self.outputVal, desiredOutputVal)
			self.delta = np.multiply(costDerivative, sigmoidDerivative(self.netActiv))
		elif self.layerType == 'hidden':
			nextDelta = nextVal
			self.delta = np.multiply(np.dot(np.transpose(nextWeight), nextDelta), sigmoidDerivative(self.netActiv))
		# update wight
		weightPartialDerivative = np.dot(self.delta, np.transpose(self.inputVal))
		self.weight = np.subtract(self.weight, np.multiply(learningRate, weightPartialDerivative))
		# update bias
		biasPartialDerivative = self.delta
		self.bias = np.subtract(self.bias, np.multiply(learningRate, biasPartialDerivative))

def sigmoid (x):
	'''
		sigmoid function y = 1 / (1 + exp(-x))
	'''
	y = x.clip(min=0)
	return y

def sigmoidDerivative (x):
	'''
		y' = sigmoid(x) * (1 - sigmoid(x))
	'''
	y = sigmoid(x)
	y[y>0] = 1
	return y