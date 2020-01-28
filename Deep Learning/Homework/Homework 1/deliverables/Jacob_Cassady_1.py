#**************************#
#* Jacob T. Cassady      * #
#* CECS 590-01           * #
#* Assignment 1          * #
#************************* #

import numpy as np
import matplotlib.pyplot as plt

from activation_functions import tanh, sigmoid, hardtanh


if __name__ == "__main__":
    """
        Show that the tanh function is a re-scaled sigmoid function with both
        horizontal and vertical streching, as well as vertical translation:
            tanh(𝑣) = 2𝑠𝑖𝑔𝑚𝑜𝑖𝑑(2𝑣) − 1
    """
    print("1. Show that the tanh function is a re-scaled sigmoid function with both horizontal and vertical streching, as well as vertical translation:")
    print("tanh(v) = 2*sigmoid(2v) − 1")

    input_array = np.linspace(-4, 4, 8000)

    sigmoid_output = sigmoid(input_array)[0]
    tanh_output = tanh(input_array)[0]

    plt.plot(input_array, sigmoid_output, label="sigmoid")
    plt.plot(input_array, tanh_output, label="tanh")
    plt.title("Question 1")
    plt.xlabel("input")
    plt.ylabel("function output")
    plt.legend()
    plt.show()
