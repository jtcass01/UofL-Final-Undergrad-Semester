import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

from activation_functions import sigmoid

class NeuralNetwork(object):
    def __init__(self, layer_dimensions):
        self.parameters = NeuralNetwork.initialize_parameters(layer_dimensions)
        self.costs = []

    def train(self, X, Y, learning_rate = 0.0075, number_of_epochs = 30000):
        for epoch in range(1, number_of_epochs):
            # Complete forward propagation
            final_activation, caches = NeuralNetwork.propagate_forward(X, self.parameters)

            # Compute error
            self.costs.append(self.compute_cost(final_activation, Y))

    def compute_cost(self, activation, target):
        return mean_squared_error(activation, target)

    @staticmethod
    def propagate_forward(X, parameters):
        caches = []
        activations = X
        number_of_layers = len(parameters) // 2

        for layer in range(1, number_of_layers):
            previous_activations = activations
            activations, cache = NeuralNetwork.propagate_forward_layer(previous_activations, parameters['W' + str(layer)], parameters['b' + str(layer)])
            caches.append(cache)

        final_activation, cache = NeuralNetwork.propagate_forward_layer(activations, parameters['W' + str(layer)], parameters['b' + str(layer)])
        caches.append(cache)

        assert(final_activation.shape == (1, X.shape[1]))

        return final_activation, caches

    @staticmethod
    def propagate_forward_layer(previous_activations, Weights, bias):
        Z = Weights.dot(previous_activations) + bias

        assert (Z.shape == (Weights.shape[0], previous_activations.shape[1]))
        linear_cache = (activations, Weights, bias)

        activations, activation_cache = sigmoid(Z)
        assert (activations.shape == (Weights.shape[0], previous_activations.shape[1]))
        cache = linear_cache, activation_cache

        return activations, cache

    @staticmethod
    def initialize_parameters(layer_dimensions):
        parameters = {}
        layers = len(layer_dims)

        for layer in range(1, layers):
            parameters['W' + str(layer)] = np.random.randn(layer_dimensions[layer], layer_dimensions[layer - 1]) * 0.01
            parameters['b' + str(layer)] = np.zeros((layer_dimensions[layer], 1))

            assert (parameters['W' + str(layer)].shape == (layer_dimensions[layer], layer_dimensions[layer - 1]))
            assert (parameters['b' + str(layer)].shape == (layer_dimensions[layer], 1))

        return parameters
