import random
from collections import Counter


class GaltonBoard:
    def __init__(self, levels):
        self.levels = levels
        self.results = []
        self.normalized_results = []

    def drop_ball(self):
        position = 0
        for _ in range(self.levels):
            position += random.choice([0, 1])
        self.results.append(position)

    def simulate(self, num_balls):
        for _ in range(num_balls):
            self.drop_ball()

    def display_results(self):
        counter = Counter(self.results)
        for position in range(self.levels + 1):
            print(f"Position {position}: {'*' * counter[position]}")
