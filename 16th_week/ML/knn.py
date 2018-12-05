import numpy as np
from collections import Counter


def kNN_classify(X_train, y_train, X_predict, k=5, p=2):
    '''kNN分类器'''
    assert k > 0, 'k需要大于0'
    assert k <= y_train.shape[0], 'k需要小于或等于总的样本数'
    assert p > 0, 'p需要大于0'
    assert X_train.shape[0] == y_train.shape[0], \
        'X_train中样本数量需要与y_train的数量相同'
    assert X_train.shape[1] == X_predict.shape[1], \
        '预测的特征数量需要等于样本的特征数量'

    return np.array([_predict(X_train, y_train, x, k, p) for x in X_predict])


def _predict(X_train, y_train, x, k, p):
    distances = [distance(item, x, p=p) for item in X_train]
    nearest = np.argsort(distances)[:k]
    k_labels = y_train[nearest]

    return Counter(k_labels).most_common(1)[0][0]


def distance(a, b, p=2):
    '''计算距离'''
    return np.sum(np.abs(a - b) ** p) ** (1 / p)
