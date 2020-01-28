#**************************#
#* Jacob T. Cassady      * #
#* CECS 590-01           * #
#* Assignment 1          * #
#************************* #

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles
from keras import models, layers

def plot_decision_boundary(X, y, model, title, steps=1000, cmap='RdBu', output_shape=(0, 1)):
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
    ax.set_xlim(output_shape)
    ax.set_ylim(output_shape)
    ax.set_title(title)

    plt.show()

    return fig, ax


def generate_circle_data(mu, std_dev, radius=2):
    x = np.random.normal(loc=mu, scale=std_dev, size=100)
    y = (radius**2 - x**2)**0.5

    return np.array(list(zip(x, y)))

def question_4_a():
    variance = 0.08
    mu = 0
    sigma = variance**0.5

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

    random_indices = np.arange(features.shape[0])
    np.random.shuffle(random_indices)
    features = features[random_indices]
    targets = targets[random_indices]

    model = models.Sequential()
    model.add(layers.Dense(4, activation='relu', input_shape=(2,)))
    model.add(layers.Dense(2, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(features, targets, epochs=200, batch_size=32, verbose=1)

    plot_decision_boundary(features, targets, model, title="4a")

def question_4_b():
    variance = 0.08
    area_1 = np.random.multivariate_normal(mean=[0, 0], cov=[[variance, 0], [0, variance]], size=100)
    area_2, targets = make_circles(n_samples=100, noise=variance)
    plt.scatter(area_1[:, 0], area_1[:, 1], label="area_1")
    plt.scatter(area_2[:, 0], area_2[:, 1], label="area_2")
    plt.show()

    area_1_targets = [0] * len(area_1)
    area_2_targets = [1] * len(area_2)

    features = np.concatenate((area_1, area_2),axis=0)
    targets = np.concatenate((area_1_targets, area_2_targets), axis=0)

    model = models.Sequential()
    model.add(layers.Dense(4, activation='relu', input_shape=(2,)))
    model.add(layers.Dense(2, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(features, targets, epochs=200, batch_size=32, verbose=1)

    plot_decision_boundary(features, targets, model, title="4b", output_shape=(-0.25, 0.9))

if __name__ == "__main__":
    question_4_a()
    question_4_b()
