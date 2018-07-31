import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

class Painter():
    """docstring for Paiter."""
    def __init__(self, category='line',
                dir = None,
                colorful = 'favorite',):
        self.colorful = colorful
        self.category = category
        self.color_mark = 0

        sns.set(style="white", color_codes=True)
        if not dir:
            self.data = self.random_data()
        else:
            # automaticly read all valid files.
            pass
        if self.colorful == 'favorite':
            colors = ["blue","orange","violet","green","red"]
            shadow_colors = ["light blue","light orange","light violet","light green","baby pink"]
            self.color_palette = sns.xkcd_palette(colors)
            self.shadow_color = sns.xkcd_palette(shadow_colors)

    def random_data(self, times = 5):
        return pd.DataFrame([self.random_feature() + np.random.randint(5) for i in range(times)])

    def random_feature(self, length = 500):
        x = np.arange(length)
        y = np.log(x + 1) + np.random.standard_normal(length)
        return y

    def colorful_world(self, pair=True):
        k = self.color_mark
        self.color_mark += 1
        if self.color_mark >= len(self.color_palette):self.color_mark -= len(self.color_palette)
        if pair:
            return self.color_palette[k], self.shadow_color[k]
        else:
            return self.color_palette[k]

    def painte(self, gamma=0.6):
        with self.color_palette:
            if self.category == 'line':
                self._plot_line(gamma)
                self.data -= 3
                self._plot_line(gamma)
                self.data -= 3
                self._plot_line(gamma)
                self.data -= 3
                plt.savefig("./example.jpg")


    def _plot_line(self, gamma, shadow=True):
        mean = np.mean(self.data, axis=0)
        c, sc = self.colorful_world()
        for i in range(1,len(mean)):
            mean[i] = mean[i] * gamma + mean[i-1] * (1 - gamma)
        plt.plot(mean, color=c)
        if shadow:
            std = np.std(self.data, axis=0)
            for i in range(1,len(std)):
                std[i] = std[i] * gamma + std[i-1] * (1 - gamma)
            plt.fill_between(np.arange(len(mean)), mean-std, mean+std, facecolor=sc, alpha=0.4)

p = Painter()
p.painte()
