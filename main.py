from galton_board import GaltonBoard
from plotter import GaltonBoardPlotter


if __name__ == "__main__":
    board = GaltonBoard(10)
    board.simulate(1000)
    board.display_results()
    board.normalize_results()

    plotter = GaltonBoardPlotter()
    plotter.plot_results(board.results, 10)
    plotter.plot_normal_distribution(board.results)

    plotter.show()