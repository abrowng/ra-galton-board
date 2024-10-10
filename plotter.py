import matplotlib.pyplot as plt
from collections import Counter

import numpy as np
from scipy.stats import norm


class GaltonBoardPlotter:

    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def plot_results(self, results, levels):
        counter = Counter(results)
        positions = list(range(levels + 1))
        counts = [counter[p] for p in positions]

        self.ax.bar(positions, counts, label="Galton Board Results")
        self.ax.set_xlabel("Position")
        self.ax.set_ylabel("Number of Balls")
        self.ax.set_title("Galton Board Results")
        self.ax.legend()

    def plot_normal_distribution(self, results):
        mean = np.mean(results)
        std_dev = np.std(results)

        x = np.linspace(min(results), max(results), 100)
        p = norm.pdf(x, mean, std_dev) * len(results)

        self.ax.plot(x, p, 'r-', label='Normal Distribution')
        self.ax.set_xlabel('Position')
        self.ax.set_ylabel('Density')
        self.ax.set_title('Normal Distribution')
        self.ax.legend()

    def show(self):
        plt.show()
