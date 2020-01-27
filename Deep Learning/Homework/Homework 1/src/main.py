import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import make_regression, make_blobs, make_checkerboard
from keras import models, layers

from activation_functions import tanh, sigmoid, hardtanh
from perceptron import Perceptron
from NeuralNetwork import NeuralNetwork
from utilities import gen_classification_symbolic

def question_1():
    """
        Show that the tanh function is a re-scaled sigmoid function with both
        horizontal and vertical streching, as well as vertical translation:
            tanh(𝑣) = 2𝑠𝑖𝑔𝑚𝑜𝑖𝑑(2𝑣) − 1
    """
    print("1. Show that the tanh function is a re-scaled sigmoid function with both horizontal and vertical streching, as well as vertical translation:")
    print("tanh(v) = 2*sigmoid(2v) − 1")

    input_array = np.linspace(-4, 4, 8000)

    sigmoid_output = sigmoid(input_array)
    tanh_output = tanh(input_array)

    plt.plot(input_array, sigmoid_output, label="sigmoid")
    plt.plot(input_array, tanh_output, label="tanh")
    plt.title("Question 1")
    plt.xlabel("input")
    plt.ylabel("function output")
    plt.legend()
    plt.show()

def question_2():
    """
        2. Show the following properties of the sigmoid and tanh activation functions:
            a. Sigmoid: Φ(−v) = 1 − Φ(v)
            b. Tanh activation: Φ(−v) = −Φ(v)
            c. Hard tanh activation: Φ(−v) = −Φ(v)
    """
    print("2. Show the following properties of the sigmoid and tanh activation functions:")
    input_array = np.linspace(-4, 4, 8000)

    print("\ta. Sigmoid: Φ(−v) = 1 − Φ(v)")
    left_side = sigmoid(-input_array)
    right_side = 1 - sigmoid(input_array)
    plt.title("a. Sigmoid: Φ(−v) = 1 − Φ(v)")
    plt.plot(input_array, left_side, label="left_side")
    plt.plot(input_array, right_side, label="right_side")
    plt.xlim(-4, 4)
    plt.legend()
    plt.show()

    print("\tb. Tanh activation: Φ(−v) = −Φ(v)")
    left_side = tanh(-input_array)
    right_side = -1 * tanh(input_array)
    plt.title("b. Tanh activation: Φ(−v) = −Φ(v)")
    plt.plot(input_array, left_side, label="left_side")
    plt.plot(input_array, right_side, label="right_side")
    plt.xlim(-4, 4)
    plt.legend()
    plt.show()

    print("\tc. Hard tanh activation: Φ(−v) = −Φ(v)")
    left_side = hardtanh(-input_array)
    right_side = -1 * hardtanh(input_array)
    plt.title("c. Hard tanh activation: Φ(−v) = −Φ(v)")
    plt.plot(input_array, left_side, label="left_side")
    plt.plot(input_array, right_side, label="right_side")
    plt.xlim(-4, 4)
    plt.legend()
    plt.show()

def question_3():
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

    neural_network = NeuralNetwork([2, 3, 1])
    neural_network.parameters['W1'] = np.array([[0.8, 0.4, 0.3], [0.2, 0.9, 0.5]]).reshape((3, 2))
    neural_network.parameters['W2'] = np.array([0.3, 0.5, 0.9]).reshape((1, 3))
    neural_network.train(input_array, np.array([0]), number_of_epochs=10)

def plot_decision_boundary(X, y, model, steps=1000, cmap='RdBu'):
    cmap = plt.get_cmap(cmap)

    # Define region of interest by data limits
    xmin, xmax = X[:,0].min() - 1, X[:,0].max() + 1
    ymin, ymax = X[:,1].min() - 1, X[:,1].max() + 1
    steps = 1000
    x_span = np.linspace(xmin, xmax, steps)
    y_span = np.linspace(ymin, ymax, steps)
    xx, yy = np.meshgrid(x_span, y_span)

    # Make predictions across region of interest
    labels = model.predict(np.c_[xx.ravel(), yy.ravel()])

    # Plot decision boundary in region of interest
    z = labels.reshape(xx.shape)

    fig, ax = plt.subplots()
    ax.contourf(xx, yy, z, cmap=cmap, alpha=0.5)

    # Get predicted labels on training data and plot
    train_labels = model.predict(X)
    ax.scatter(X[:,0], X[:,1], c=y, cmap=cmap, lw=0)

    plt.show()

    return fig, ax

def question_4():
    variance = 0.08
    mu = 0
    sigma = variance**0.5


    """
    centers = [[0.25, 0.75], [0.75, 0.75], [0.75, 0.25]]
    center = [[0.25, 0.25]]
    area_2, _ = make_blobs(n_samples=100, centers=centers, cluster_std=sigma)
    area_2_targets = np.array([0]*len(area_2))
    area_1, _ = make_blobs(n_samples=100, centers=center, cluster_std=sigma)
    area_1_targets = np.array([1]*len(area_1))


    n_clusters = (2, 2)
    data, rows, columns = make_checkerboard(shape=(200, 200), n_clusters=n_clusters, noise=sigma, shuffle=False)
    print("data", data)

    x = gen_classification_symbolic(m="sin(x1)+cos(x2)", n_samples=200, flip_y=sigma)
    df = pd.DataFrame(x)
    print(x)

    plt.scatter(area_1[:, 0], area_1[:, 1], label='area_1')
    plt.scatter(area_2[:, 0], area_2[:, 1], label='area_2')
    plt.legend()
    plt.show()

    features = np.concatenate((area_1, area_2), axis = 0).reshape(2, -1)
    targets = np.concatenate((area_1_targets, area_2_targets), axis = 0).reshape(1, -1)

    print("features", features.T)
    print("targets", targets.T)
    """

    bottom_left = np.random.multivariate_normal(mean=[0.25, 0.25], cov=[[variance, 0], [0, variance]], size=100)
    bottom_right = np.random.multivariate_normal(mean=[0.25, 0.75], cov=[[variance, 0], [0, variance]], size=100)
    top_right = np.random.multivariate_normal(mean=[0.75, 0.75], cov=[[variance, 0], [0, variance]], size=100)
    top_left = np.random.multivariate_normal(mean=[0.75, 0.25], cov=[[variance, 0], [0, variance]], size=100)

    area_1 = bottom_left
    area_1_targets = [0] * len(area_1)
    area_2 = np.concatenate((bottom_right, top_right, top_left), axis=0)
    area_2_targets = [1] * len(area_2)

    plt.scatter(area_1[:, 0], area_1[:, 1], label="area_1")
    plt.scatter(area_2[:, 0], area_2[:, 1], label="area_2")
    plt.legend()
    plt.show()

    features = np.concatenate((area_1, area_2),axis=0)
    targets = np.concatenate((area_1_targets, area_2_targets), axis=0)

    model = models.Sequential()
    model.add(layers.Dense(4, activation='relu', input_shape=(2,)))
    model.add(layers.Dense(2, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(features, targets, epochs=100, batch_size=32, verbose=1)

    plot_decision_boundary(features, targets, model)

    """

    grid = np.stack((features[0,:],features[1,:]))
    grid = grid.T.reshape(-1,2)
    outs = model.predict(grid)
    y1 = outs.T[0].reshape(features[0,:].shape[0],features[0,:].shape[0])
    plt.contourf(features[0,:],features[1,:],y1)
    plt.show()
    """



if __name__ == "__main__":
#    question_1()
#    question_2()
    question_4()
