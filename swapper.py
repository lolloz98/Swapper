import math


def calc_pos_from_row_column(big_pix_per_row, row, column):
    return big_pix_per_row * row + column


def get_row_col_from_pos(pix_per_row, pos):
    return math.floor(pos / pix_per_row), pos % pix_per_row


def single_swap(list_big_pix, pos1, pos2):
    tmp = list_big_pix[pos1]
    list_big_pix[pos1] = list_big_pix[pos2]
    list_big_pix[pos2] = tmp


def little_column_swap(list_big_pix, n_big_pix_per_row, start_pos1, start_pos2, n_big_pix):
    pos1 = start_pos1
    pos2 = start_pos2
    for i in range(n_big_pix):
        single_swap(list_big_pix, pos1, pos2)
        r1, c1 = get_row_col_from_pos(n_big_pix_per_row, pos1)
        r2, c2 = get_row_col_from_pos(n_big_pix_per_row, pos2)
        r1 += 1
        r2 += 1
        pos1 = calc_pos_from_row_column(n_big_pix_per_row, r1, c1)
        pos2 = calc_pos_from_row_column(n_big_pix_per_row, r2, c2)


def little_row_swap(list_big_pix, n_big_pix_per_row, start_pos1, start_pos2, n_big_pix):
    pos1 = start_pos1
    pos2 = start_pos2
    for i in range(n_big_pix):
        single_swap(list_big_pix, pos1, pos2)
        r1, c1 = get_row_col_from_pos(n_big_pix_per_row, pos1)
        r2, c2 = get_row_col_from_pos(n_big_pix_per_row, pos2)
        c1 += 1
        c2 += 1
        pos1 = calc_pos_from_row_column(n_big_pix_per_row, r1, c1)
        pos2 = calc_pos_from_row_column(n_big_pix_per_row, r2, c2)


def little_square_swap(list_big_pix, n_big_pix_per_row, start_pos1, start_pos2, side_l):
    pos1 = start_pos1
    pos2 = start_pos2
    for i in range(side_l):
        little_row_swap(list_big_pix, n_big_pix_per_row, pos1, pos2, side_l)
        r1, c1 = get_row_col_from_pos(n_big_pix_per_row, pos1)
        r2, c2 = get_row_col_from_pos(n_big_pix_per_row, pos2)
        r1 += 1
        r2 += 1
        pos1 = calc_pos_from_row_column(n_big_pix_per_row, r1, c1)
        pos2 = calc_pos_from_row_column(n_big_pix_per_row, r2, c2)