import numpy as np
from collections import Counter

class KNN(object):
    def __init__(self, n_neighbors):
        self.y_train = None
        self.x_train = None
        self.n_neighbors = n_neighbors

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        y_pred = [self._predict(x) for x in self.x_train]
        return np.array(y_pred)

    def _predict(self, x_test):
        distances = np.sqrt(np.sum((self.x_train - i)**2) for i in x_test)
        k_indices = distances.argsort()[:self.n_neighbors]
        labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(labels).most_common(1)
        return most_common[0][0]

