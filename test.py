from collections import namedtuple


class GaltonBoardTest(namedtuple("GaltonBoardTest", ["levels", "num_balls"])):

    levels: int
    num_balls: int
