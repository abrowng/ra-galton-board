import numpy as np

from error_calculation import MeanSquareErrorCalculator
from galton_board import GaltonBoard
from plotter import GaltonBoardPlotter
from test import GaltonBoardTest

TESTS_MATRIX = [
    # GaltonBoardTest(5, 1000),
    # GaltonBoardTest(10, 1000),
    # GaltonBoardTest(50, 1000),
    # GaltonBoardTest(100, 1000),
    # GaltonBoardTest(500, 1000),
    # GaltonBoardTest(1000, 1000),
    GaltonBoardTest(100, 50),
    GaltonBoardTest(100, 100),
    GaltonBoardTest(100, 500),
    GaltonBoardTest(100, 1000),
    GaltonBoardTest(100, 5000),
    GaltonBoardTest(100, 10000),
]

if __name__ == "__main__":

    print("Mean Square Error:")
    print("Normal Distribution \t\t |    Binomial Distribution")
    for test in TESTS_MATRIX:
        board = GaltonBoard(test.levels)
        board.simulate(test.num_balls)

        plotter = GaltonBoardPlotter()
        plotter.plot_results(board.results)
        plotter.plot_normal_distribution(
            test.num_balls,
            mean=(test.levels / 2),
            std_dev=np.sqrt(test.levels / 4),
        )
        plotter.plot_binomial_distribution(test.levels, test.num_balls)

        plotter.show()

        error_calculator = MeanSquareErrorCalculator(board.results, test.levels, test.num_balls)
        mse_normal = error_calculator.calculate_mse_normal(
            mean=(test.levels / 2),
            std_dev=np.sqrt(test.levels / 4),
        )
        mse_binomial = error_calculator.calculate_mse_binomial()
        print(f"      {mse_normal} \t\t |    {mse_binomial}")

    input("Press Enter to exit...")

