#**************************#
#* Jacob T. Cassady      * #
#* CECS 590-01           * #
#* Assignment 1          * #
#************************* #

import numpy as np
import matplotlib.pyplot as plt

from perceptron import Perceptron
from NeuralNetwork import NeuralNetwork

if __name__ == "__main__":
    print("Given the input {1,1} compute the predicted output of the network step by step and calculate the error if the target output is 0.")
    input_array = np.array([1, 1]).reshape((2, 1))
    weights = np.array([[0.8, 0.4, 0.3],
                        [0.2, 0.9, 0.5]]).reshape((3, 2))
    bias = np.array([0, 0, 0]).reshape((3, 1))
    hidden_layer = Perceptron(number_of_neurons=3, input_size=2, Weights=weights, bias=bias)
    hidden_layer_output = hidden_layer.classify(input_array)

    print("hidden_layer_output", hidden_layer_output.shape)
    print(hidden_layer_output)

    weights = np.array([0.3, 0.5, 0.9]).reshape((1, 3))
    bias = np.array([0]).reshape((1, 1))
    output_layer = Perceptron(number_of_neurons=1, input_size=3, Weights=weights, bias=bias)
    output = output_layer.classify(hidden_layer_output)
    print("output", output.shape)
    print(output)

    def error(expected, actual):
        return (expected - actual)**2

    print("error", error(output, 0))

    print("Compute step by step 2 training epochs using Back-Propagation algorithm.")
    neural_network = NeuralNetwork([2, 3, 1])
    neural_network.parameters['W1'] = np.array([[0.8, 0.4, 0.3], [0.2, 0.9, 0.5]]).reshape((3, 2))
    neural_network.parameters['W2'] = np.array([0.3, 0.5, 0.9]).reshape((1, 3))
    neural_network.train(input_array, np.array([0]), number_of_epochs=10)
