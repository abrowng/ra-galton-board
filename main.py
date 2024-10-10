import math

from galton_board import GaltonBoard
from plotter import GaltonBoardPlotter
from test import GaltonBoardTest

TESTS_MATRIX = [
    GaltonBoardTest(5, 1000),
    GaltonBoardTest(10, 1000),
    GaltonBoardTest(50, 1000),
    GaltonBoardTest(500, 1000),
    GaltonBoardTest(500, 5000),
    GaltonBoardTest(500, 10000),
]

if __name__ == "__main__":
    for test in TESTS_MATRIX:
        board = GaltonBoard(test.levels)
        board.simulate(test.num_balls)

        plotter = GaltonBoardPlotter()
        plotter.plot_results(board.results, test.levels)
        plotter.plot_normal_distribution(
            test.num_balls,
            mean=(test.levels / 2),
            std_dev=math.sqrt(test.levels / 4),
        )
        plotter.plot_binomial_distribution(test.levels, test.num_balls)

        plotter.show()
