"""
- Create a simple model for binary classification.

- To the provided dataset apply:

﻿﻿﻿﻿﻿﻿﻿﻿  - Random Under-sampling
  - Random Over-Sampling
  - Under-sampling: Tomek links
  - Under-sampling: Cluster Centroids
  - Over-sampling: SMOTE
  - Over-sampling->Under-sampling: SMOTE-Tomek

Requirements (Grading Criteria):
-  For each of the cases produce a confusion matrix to evaluate the performance of the model (one model for all the cases) and compare the results obtained by the different techniques in one graph.
- Please take into account that each of the techniques should be applied to the original data, is not a sequential process.

- Use 80% of the data to train 20% for testing
- Briefly describe in the comparison of the techniques why you obtained the difference in the performance and why you believe your best model was the best.
Please send a ipynb file using with your name for the name of the file!!!!!!!!!!!
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import itertools
from imblearn.combine import SMOTETomek
from imblearn.under_sampling import RandomUnderSampler, TomekLinks, ClusterCentroids
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras import models, layers

def load_data(relative_data_path):
    df = pd.read_csv(relative_data_path)

    target_count = df.target.value_counts()
    print(df.head())
    print('Class 0:', target_count[0])
    print('Class 1:', target_count[1])
    print('Proportion:', round(target_count[0] / target_count[1], 2), ': 1')

    feature_labels = df.columns[2:]
    return df[feature_labels].head(100000), df['target'].head(100000)

def build_simple_binary_classification_model():
    model = models.Sequential()
    model.add(layers.Dense(20))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer="adam", metrics=['accuracy'])
    return model

## Under sampling strategies
def random_under_sampling(X, y):
    return RandomUnderSampler().fit_sample(X, y)

def tomek_links(X, y):
    return TomekLinks(sampling_strategy='majority').fit_sample(X, y)

def cluster_centroids(X, y):
    return ClusterCentroids(sampling_strategy={0:10}).fit_sample(X, y)

## Over sampling strategies
def random_over_sampling(X, y):
    return RandomOverSampler().fit_sample(X, y)

def smote(X, y):
    return SMOTE(sampling_strategy='minority').fit_sample(X, y)

## Over-sampling followed by Under sampling
def smote_tomek(X, y):
    return SMOTETomek(sampling_strategy='auto').fit_sample(X, y)

def plot_confusion_matrix(cnf_matrix, classes=['0','1'], normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    if normalize:
        cnf_matrix = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix without normalization")

    print(cnf_matrix)

    plt.imshow(cnf_matrix, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cnf_matrix.max() / 2.
    for row_index, column_index in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
        plt.text(row_index, column_index, format(cnf_matrix[row_index, column_index], fmt),
                 horizontalalignment='center',
                 color='white' if cm[row_index, column_index] > thresh else 'black')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    relative_data_path = ".." + os.path.sep + "data" + os.path.sep + "data.csv"

    sampling_techniques = {
        'no_sampling': None,
        'random_under_sampling': random_over_sampling,
        'tomek_links': tomek_links,
        'cluster_centroids': cluster_centroids,
        'random_over_sampling': random_over_sampling,
        'smote': smote,
        'smote_tomek': smote_tomek,
    }

    for sampling_technique in sampling_techniques:
        # Load data
        X, y = load_data(relative_data_path)

        print("Applying sampling technique: " + sampling_technique)

        if sampling_technique != 'no_sampling':
            # Apply sampling technique to data
            X, y = sampling_techniques[sampling_technique](X, y)

        # Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Build model and fit to dataset
        model = build_simple_binary_classification_model()
        model.fit(X_train, y_train, epochs=25, batch_size=512)

        # Determine confusion matrix
        y_pred = model.predict(X_test)
        cnf_matrix = confusion_matrix(y_test, y_pred)
        plot_confusion_matrix(cnf_matrix, title=sampling_technique + " Confusion Matrix")
