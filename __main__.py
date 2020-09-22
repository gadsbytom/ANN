from sklearn.datasets import make_moons
from ann_feed_forward import feed_forward, sigmoid, tanh
from ann_backprop import backprop, epoch
from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":

    X, y = make_moons(n_samples=50, noise=0.2, random_state=42)
    plt.scatter(X[:, 0], X[:, 1], c=y)
    X.shape, y.shape

    # make the feed forward network
    X = np.hstack(
        [X, np.ones((X.shape[0], 1))]
    )  # adding an extra dimension for the bias

    initial_weights = np.random.randn(3, 2)
    initial_m_weights = np.random.randn(3, 1)

    out1, out2 = feed_forward(X, initial_weights, initial_m_weights)

    epoch_200_logloss, _, _ = epoch(
        X, y, 5000, initial_weights, initial_m_weights, 0.01, 0.01
    )

    plt.figure(figsize=(10, 10))
    plt.plot(epoch_200_logloss)
    plt.show()