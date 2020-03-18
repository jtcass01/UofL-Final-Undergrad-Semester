import h5py
import math
import os
import sklearn
import random
import numpy as np

from keras.applications import VGG16
from keras import layers, models

def load_dataset(relative_directory_path):
    """
    Created By: Jacob Taylor Cassady
    Last Updated: 2/7/2018
    Objective: Load in practice data from example tensorflow model.

    Arguments:
    None

    Returns:
    train_set_x_orig -- A NumPy array of (currently) 1080 training images of shape (64,64,3).  Total nparray shape of (1080,64,64,3)
    train_set_y_orig -- A NumPy array of (currently) 1080 training targets.  Total nparray shape of (1, 1080) [After reshape]
    test_set_x_orig -- A NumPy array of (currently) 200 test images of shape (64,64,3).  Total nparray shape of (120,64,64,3)
    test_set_y_orig -- A NumPy array of (currently) 200 test targets.  Total nparray shape of (1,120) [After reshape]
    classes -- A NumPy array of (currently) 6 classes. (0-5)
    """

    train_dataset = h5py.File(relative_directory_path + 'train_signs.h5', 'r')
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])

    test_dataset = h5py.File(relative_directory_path + 'test_signs.h5', 'r')
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])

    classes = np.array(test_dataset['list_classes'][:])

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y

def random_mini_batches(X, Y, mini_batch_size = 64):
    """
    Created By: Jacob Taylor Cassady
    Last Updated: 2/8/2018
    Objective: Creates a list of random minibatches from (X, Y)

    Arguments:
    X -- input data, of shape (input size, number of examples)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples)
    mini_batch_size - size of the mini-batches, integer

    Returns:
    mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """

    m = X.shape[1]                  # number of training examples
    mini_batches = []

    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))
    shuffled_X = X[:, permutation]
    shuffled_Y = Y[:, permutation].reshape((Y.shape[0],m))

    # Step 2: Partition (shuffled_X, shuffled_Y). Minus the end case.
    num_complete_minibatches = math.floor(m/mini_batch_size) # number of mini batches of size mini_batch_size in your partitionning
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[:, k * mini_batch_size : k * mini_batch_size + mini_batch_size]
        mini_batch_Y = shuffled_Y[:, k * mini_batch_size : k * mini_batch_size + mini_batch_size]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    # Handling the end case (last mini-batch < mini_batch_size)
    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[:, num_complete_minibatches * mini_batch_size : m]
        mini_batch_Y = shuffled_Y[:, num_complete_minibatches * mini_batch_size : m]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches

def prepare_data():
    relative_directory_path = ".." + os.path.sep + "data" + os.path.sep
    print("\nLoading data from relative directory path:", relative_directory_path)
    X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset(relative_directory_path)

    # Normalize image vectors
    X_train = X_train_orig/255.
    X_test = X_test_orig/255.

    # Convert training and test labels to one hot matrices
    Y_train = convert_to_one_hot(Y_train_orig, 6).T
    Y_test = convert_to_one_hot(Y_test_orig, 6).T

    # Split test set into test and valdiation sets
    test_set = np.array(list(zip(X_test, Y_test)))
    random.shuffle(test_set)
    new_test_set = test_set[:60, :]
    validation_set = test_set[-60:, :]

    X_test = new_test_set[:, 0]
    Y_test = new_test_set[:, 1]

    X_validation = validation_set[:, 0]
    Y_validation = validation_set[:, 1]

    return X_train, Y_train, X_test, Y_test, X_validation, Y_validation

if __name__ == "__main__":
    # Retrieve data
    X_train, Y_train, X_test, Y_test, X_validation, Y_validation = prepare_data()

    # Train Model
    model = models.Sequential()
    conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(64, 64, 3))
    conv_base.trainable = False
    model.add(conv_base)
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    model.fit(X_train, Y_train, epochs=20, batch_size=32, validation_data=(X_validation, Y_validation))

    # Evaluate Model
    predictions = model.evaluate(X_test, Y_test)
    print("Test Loss = " + str(predictions[0]))
    print("Test accuracy = " + str(predictions[1]))
