import matplotlib.pyplot as plt
from collections import Counter

import numpy as np
from scipy.stats import norm, binom


class GaltonBoardPlotter:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.first_non_zero_i = 0
        self.last_non_zero_i = 0

    def plot_results(self, results, levels):
        counter = Counter(results)
        positions = list(range(levels + 1))
        counts = []
        for i, p in enumerate(positions):
            count = counter[p]
            counts.append(count)
            if self.first_non_zero_i <= 0 < count:
                self.first_non_zero_i = i
            if count > 0:
                self.last_non_zero_i = i

        if self.last_non_zero_i == 0:
            self.last_non_zero_i = len(positions)

        self.ax.bar(
            positions[self.first_non_zero_i:self.last_non_zero_i],
            counts[self.first_non_zero_i:self.last_non_zero_i],
            label="Galton Board Results",
        )
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

    def plot_binomial_distribution(self, levels, num_balls):
        positions = list(range(levels + 1))
        binom_pmf = binom.pmf(positions, levels, 0.5) * num_balls

        if self.last_non_zero_i == 0:
            self.last_non_zero_i = len(positions)

        self.ax.bar(
            positions[self.first_non_zero_i:self.last_non_zero_i],
            binom_pmf[self.first_non_zero_i:self.last_non_zero_i],
            alpha=0.4,                            # Make it transparent to see the board results
            label='Binomial Distribution',
            color='g',
        )
        self.ax.set_xlabel('Position')
        self.ax.set_ylabel('Probability')
        self.ax.set_title('Binomial Distribution')
        self.ax.legend()

    def show(self):
        plt.show()
