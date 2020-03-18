import h5py
import math
import os
import sklearn
import random

import numpy as np
import matplotlib.pyplot as plt

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
    test = False

    random.shuffle(test_set)
    X_test = list([])
    Y_test = list([])
    X_validation = list([])
    Y_validation = list([])

    for feature, target in test_set:
        if test:
            X_test.append(feature)
            Y_test.append(target)
            test = False
        else:
            X_validation.append(feature)
            Y_validation.append(target)
            test = True

    return X_train, Y_train, np.array(X_test), np.array(Y_test), np.array(X_validation), np.array(Y_validation)

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
    model.add(layers.Dense(6, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    training_history = model.fit(X_train, Y_train, epochs=17, batch_size=32, validation_data=(X_validation, Y_validation))

    # Display Training history graphs
    history_dict = training_history.history
    training_loss_values = history_dict['loss']
    validation_loss_values = history_dict['val_loss']
    epochs = range(1, len(training_loss_values) + 1)
    plt.plot(epochs, training_loss_values, 'bo', label='Training loss')
    plt.plot(epochs, validation_loss_values, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

    # Evaluate Model On Test Data
    predictions = model.evaluate(X_test, Y_test)
    print("Test Loss = " + str(predictions[0]))
    print("Test accuracy = " + str(predictions[1]))
