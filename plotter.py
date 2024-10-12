import matplotlib.pyplot as plt
from collections import Counter

import numpy as np
from scipy.stats import norm, binom


class GaltonBoardPlotter:

    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def plot_results(self, results):
        counter = Counter(results)
        counts = list(counter.values())
        x = list(counter.keys())

        self.ax.bar(
            x,
            counts,
            label="Galton Board Results",
        )
        self.ax.set_xlabel("Position")
        self.ax.set_ylabel("Number of Balls")
        self.ax.set_title("Galton Board Results")
        self.ax.legend()

    def plot_normal_distribution(self, num_balls, mean=0, std_dev=0, results=None):
        if results is None and mean == 0 and std_dev == 0:
            print("Need one of (mean, std_dev) or results to plot")
            return

        if mean == 0 and std_dev == 0 and results is not None:
            mean = np.mean(results)
            std_dev = np.std(results)

        x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 500)
        p = norm.pdf(x, mean, std_dev) * num_balls

        self.ax.plot(x, p, 'r-', label='Normal Distribution')
        self.ax.set_xlabel('Position')
        self.ax.set_ylabel('Density')
        self.ax.set_title('Normal Distribution')
        self.ax.legend()

    def plot_binomial_distribution(self, levels, num_balls):
        positions = list(range(levels + 1))
        binom_pmf = binom.pmf(positions, levels, 0.5) * num_balls

        # Find the first and last large > 1 values so that the plot is centered
        first_non_zero_i = 0
        last_non_zero_i = 0
        for i, count in enumerate(binom_pmf):
            if count > 1:
                first_non_zero_i = i
                break
        for i, count in enumerate(binom_pmf[::-1]):
            if count > 1:
                last_non_zero_i = len(binom_pmf) - i
                break

        self.ax.bar(
            positions[first_non_zero_i:last_non_zero_i],
            binom_pmf[first_non_zero_i:last_non_zero_i],
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
