import numpy as np
import matplotlib.pyplot as plt

from activation_functions import tanh, sigmoid, hardtanh
from perceptron import Perceptron

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

if __name__ == "__main__":
#    question_1()
#    question_2()
    question_3()
