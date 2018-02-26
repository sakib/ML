import numpy as np
from collections import Counter
from scipy.spatial import distance

###Distance Metric : L2 ###
class KNearestNeighbor(object):
    """ a kNN classifier with L2 distance """

    def __init__(self):
        pass

    def train(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X, k):
        dists = self.compute_distances(X)
        return self.predict_labels(dists, k=k)

    def compute_distances(self, X):
        #dists = np.zeros((X.shape[0], self.X_train.shape[0])) # (406, 1627)
        #for i in range(X.shape[0]):
        #    print(i)
        #    for j in range(self.X_train.shape[0]):
        #        x, y = X.getrow(i).todense(), self.X_train.getrow(j).todense()
        #        dists[i][j] = distance.euclidean(x, y)
        from sklearn.metrics.pairwise import euclidean_distances # this is way faster
        dists = euclidean_distances(X, self.X_train)
        return dists

    def predict_labels(self, dists, k):
        y_pred = np.zeros((dists.shape[0]))
        for i in range(dists.shape[0]):
            top_k = sorted(list(enumerate(dists[i])), key=lambda x: x[1])[:k]
            y_pred[i], count = Counter([self.y_train[x[0]] for x in top_k]).most_common()[0]
        return y_pred
