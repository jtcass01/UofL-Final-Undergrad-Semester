import numpy as np

from activation_functions import sigmoid

class Perceptron(object):
    def __init__(self, number_of_neurons, input_size, Weights=None, bias=None, transfer_function=sigmoid):
        if Weights is None:
            self.Weights = np.random.rand(number_of_neurons, input_size)
        else:
            self.Weights = Weights
        if bias is None:
            self.bias = np.random.rand(number_of_neurons, 1)
        else:
            self.bias = bias
        self.activation_function = sigmoid

    def classify(self, prototype):
        net_input = self.Weights.dot(prototype) + self.bias
        return self.activation_function(net_input)[0]
