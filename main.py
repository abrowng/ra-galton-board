from galton_board import GaltonBoard
from plotter import GaltonBoardPlotter
from test import GaltonBoardTest


TESTS_MATRIX = [
    GaltonBoardTest(5, 1000),
    GaltonBoardTest(10, 1000),
    GaltonBoardTest(50, 1000),
    GaltonBoardTest(500, 1000),
]


if __name__ == "__main__":
    for test in TESTS_MATRIX:
        board = GaltonBoard(test.levels)
        board.simulate(test.num_balls)

        plotter = GaltonBoardPlotter()
        plotter.plot_results(board.results, test.levels)
        plotter.plot_normal_distribution(board.results)
        plotter.plot_binomial_distribution(test.levels, test.num_balls)

        plotter.show()
