from collections import Counter, OrderedDict

import numpy as np
from scipy.stats import norm, binom


class MeanSquareErrorCalculator:
    def __init__(self, results, levels, num_balls):
        self.results = results
        self.levels = levels
        self.num_balls = num_balls

        self.counter = Counter(self.results)
        self.sorted_counter = OrderedDict(sorted(self.counter.items(), key=lambda x: x[0]))

    def calculate_mse_normal(self, mean, std_dev):
        p = norm.pdf(list(self.sorted_counter.keys()), mean, std_dev) * self.num_balls

        diff = np.array(list(self.sorted_counter.values())) - p
        squared_diff = diff ** 2
        mse = np.mean(squared_diff)
        return mse

    def calculate_mse_binomial(self):
        binom_pmf = binom.pmf(list(self.sorted_counter.keys()), self.levels, 0.5) * self.num_balls

        diff = np.array(list(self.sorted_counter.values())) - binom_pmf
        squared_diff = diff ** 2
        mse = np.mean(squared_diff)
        return np.sqrt(mse)
