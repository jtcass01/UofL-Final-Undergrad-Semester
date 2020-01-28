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
