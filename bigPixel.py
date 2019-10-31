from enum import Enum


# todo test if everything works here


class BigPixel(object):
    min_dists = [-1, -1, -1, -1]
    better_matches_bp_n = [-1, -1, -1, -1]
    mat_of_pixels = []

    def __init__(self, list_of_pix, number, dimension):
        # list_of_pix: there is a matrix which is ordered writing the rows one after another
        self.list_of_pix = list_of_pix
        self.number = number
        self.dimension = dimension
        self.min_dists = [-1, -1, -1, -1]
        self.better_matches_bp_n = [-1, -1, -1, -1]
        self.used = False
        self.dists = [[]]
        self.real_dists = [[]]
        self.initial_bp_matrix = [[]]


class Directions(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


def inverse_dir_val(direction_val):
    if direction_val == Directions.UP.value:
        return Directions.DOWN.value
    if direction_val == Directions.DOWN.value:
        return Directions.UP.value
    if direction_val == Directions.RIGHT.value:
        return Directions.LEFT.value
    if direction_val == Directions.LEFT.value:
        return Directions.RIGHT.value
