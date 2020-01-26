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
            self.costs.append(NeuralNetwork.compute_cost(final_activation, Y))

            # Complete backward propagation
            gradients = NeuralNetwork.propagate_backward(final_activation, Y, caches)

            self.parameters = NeuralNetwork.update_parameters(self.parameters, gradients, learning_rate)

            if epoch % 10:
                print(self.costs[len(self.costs)-1], 'cost @ epoch: ', epoch)

        plt.plot(np.squeeze(self.costs))
        plt.ylabel('cost')
        plt.xlabel('iterations')
        plt.title('Learning rate =' + str(learning_rate))
        plt.show()

        NeuralNetwork.plot_decision_boundary(lambda x: self.predict(x.T), X, Y)

    def predict(self, X):
        """
        Used for plotting decision boundary.
        Arguments:
        parameters -- python dictionary containing your parameters
        X -- input data of size (m, K)
        Returns
        predictions -- vector of predictions of our model (red: 0 / blue: 1)
        """

        # Predict using forward propagation and a classification threshold of 0.5
        a3, cache = NeuralNetwork.propagate_forward(X, self.parameters)
        predictions = (a3 > 0.5)

        return predictions

    @staticmethod
    def compute_cost(activation, target):
        return mean_squared_error(activation, target)

    @staticmethod
    def plot_decision_boundary(model, X, y):
        # Set min and max values and give it some padding
        x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
        y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
        h = 0.01
        # Generate a grid of points with distance h between them
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        # Predict the function value for the whole grid
        Z = model(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        # Plot the contour and training examples
        plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
        plt.ylabel('x2')
        plt.xlabel('x1')
        plt.title("Decision boundary plot")
        plt.scatter(X[0, :], X[1, :], cmap=plt.cm.Spectral)
        plt.show()

    @staticmethod
    def update_parameters(parameters, gradients, learning_rate):
        # Calculate number of layers
        number_of_layers = len(parameters) // 2

        # Perform update for each parameter.
        for layer in range(1, number_of_layers+1):
            parameters['W' + str(layer)] = parameters['W' + str(layer)] - learning_rate * gradients['dW' + str(layer)]
            parameters['b' + str(layer)] = parameters['b' + str(layer)] - learning_rate * gradients['db' + str(layer)]

        return parameters

    @staticmethod
    def propagate_forward(X, parameters):
        caches = []
        activations = X
        number_of_layers = len(parameters) // 2

        for layer in range(1, number_of_layers):
            previous_activations = activations
            activations, cache = NeuralNetwork.linear_activation_forward(previous_activations, parameters['W' + str(layer)], parameters['b' + str(layer)])
            caches.append(cache)

        final_activation, cache = NeuralNetwork.linear_activation_forward(activations, parameters['W' + str(number_of_layers)], parameters['b' + str(number_of_layers)])
        caches.append(cache)

        assert(final_activation.shape == (1, X.shape[1]))

        return final_activation, caches

    @staticmethod
    def linear_activation_forward(previous_activations, Weights, bias):
        Z, linear_cache = NeuralNetwork.linear_propagation_forward(previous_activations, Weights, bias)
        activations, activation_cache = sigmoid(Z)

        assert (activations.shape == (Weights.shape[0], previous_activations.shape[1]))

        cache = (linear_cache, activation_cache)

        return activations, cache

    @staticmethod
    def linear_propagation_forward(activations, Weights, bias):
#        print("activations", activations, activations.shape)
#        print("Weights", Weights, Weights.shape)
        Z = Weights.dot(activations) + bias

        assert (Z.shape == (Weights.shape[0], activations.shape[1]))

        cache = (activations, Weights, bias)

        return Z, cache


    @staticmethod
    def initialize_parameters(layer_dimensions):
        parameters = {}
        layers = len(layer_dimensions)

        for layer in range(1, layers):
            parameters['W' + str(layer)] = np.random.randn(layer_dimensions[layer], layer_dimensions[layer - 1]) * 0.01
            parameters['b' + str(layer)] = np.zeros((layer_dimensions[layer], 1))

            assert (parameters['W' + str(layer)].shape == (layer_dimensions[layer], layer_dimensions[layer - 1]))
            assert (parameters['b' + str(layer)].shape == (layer_dimensions[layer], 1))

        return parameters

    @staticmethod
    def propagate_backward(final_activation, Y, caches):
        gradients = {}

        number_of_layers = len(caches)
        columns = final_activation.shape[1]
        Y = Y.reshape(final_activation.shape)

        # Calculate the gradient of the final loss function
        d_final_activation = -1 * (np.divide(Y, final_activation) - np.divide(1 - Y, 1 - final_activation))

        # Calculate the gradients for the final layer
        current_cache = NeuralNetwork.linear_activation_backward(d_final_activation, caches[number_of_layers-1])
        gradients["dA" + str(number_of_layers)], gradients["dW" + str(number_of_layers)], gradients['db' + str(number_of_layers)] = current_cache

        for layer in reversed(range(number_of_layers - 1)):
            current_cache = NeuralNetwork.linear_activation_backward(gradients['dA' + str(layer + 2)], caches[layer])
            gradients["dA" + str(layer+1)], gradients["dW" + str(layer+1)], gradients['db' + str(layer+1)] = current_cache

        return gradients

    @staticmethod
    def linear_activation_backward(dA, cache):
        linear_cache, activation_cache = cache

        dZ = NeuralNetwork.calculate_sigmoid_derivative(dA, activation_cache)
        dA_prev, dW, db = NeuralNetwork.linear_backward_propagation(dZ, linear_cache)

        return dA_prev, dW, db

    @staticmethod
    def calculate_sigmoid_derivative(dA, cache):
        Z = cache
        s = 1 / (1 + np.exp(-Z))
        dZ = dA * s * (1 - s)

        assert (dZ.shape == Z.shape)

        return dZ

    @staticmethod
    def linear_backward_propagation(dZ, cache):
        previous_activation, Weights, bias = cache
        columns = previous_activation.shape[1]

        dW = 1 / columns * dZ.dot(previous_activation.T)
        db = 1 / columns * np.sum(dZ, axis=1, keepdims=True)
        d_previous_activation = Weights.T.dot(dZ)

        assert (d_previous_activation.shape == previous_activation.shape)
        assert (dW.shape == Weights.shape)
        assert (db.shape == bias.shape)

        return d_previous_activation, dW, db
