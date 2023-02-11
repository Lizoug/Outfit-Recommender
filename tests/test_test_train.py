import sys
import os
import numpy as np
path = os.getcwd()
sys.path.insert(1, path + "//backend")
import create_data


def test_train_test():
    # Test case 1
    images = np.array([np.zeros((100, 100, 3)), np.ones((100, 100, 3))])
    label_article = ['a', 'b']
    X_train, X_test, y_train, y_test = create_data.train_test(images, 'article')
    assert X_train.shape == (1, 100, 100, 3)
    assert y_train.shape == (1, 2)
    assert X_test.shape == (1, 100, 100, 3)
    assert y_test.shape == (1, 2)

    # Test case 2
    images = np.array([np.zeros((100,100,3)), np.ones((100,100,3))])
    label_color = ['red', 'blue']
    X_train, X_test, y_train, y_test = create_data.train_test(images, 'color')
    assert X_train.shape == (1, 100, 100, 3)
    assert y_train.shape == (1, 2)
    assert X_test.shape == (1, 100, 100, 3)
    assert y_test.shape == (1, 2)
