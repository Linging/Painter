import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

class Paiter():
    """docstring for Paiter."""
    def __init__(self, p_kind,
                dir = None,
                shadow = True,
                colorful = 'favorite',):
        self.colorful = colorful
        self.shadow = shadow
        self.p_kind = p_kind

        sns.set(style="white", palette="muted", color_codes=True)
        if not dir:
            self.data = self.random_data()
        else:
            # automaticly read all valid files.
            pass

    def random_data(self, times = 5):
        return pd.DataFrame([self.random_feature() + np.random.randint(5) for i in range(times)])

    def random_feature(self, length = 500):
        x = np.arange(length)
        y = np.log(x + 1) + np.random.standard_normal(length)
        return y

    def paiter(self, gamma=0.6):
        if self.p_kind == 'line':
            self._plot_line(gamma)

    def _plot_line(self, gamma=1):
        mean = np.mean(self.data, axis=0)
        for i in range(1,len(mean)):
            mean[i] = mean[i] * gamma + mean[i-1] * (1 - gamma)
        plt.plot(mean)
        if self.shadow:
            std = np.std(self.data, axis=0)
            plt.fill_between(np.arange(len(mean)), mean-std, mean+std, alpha=0.4)
        plt.show()
