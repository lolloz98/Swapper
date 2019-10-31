import math
from multipledispatch import dispatch
import bigPixel


def calculate_n_of_big_pix(pix_list_rgb, big_pix_dimen):
    n_pix = len(pix_list_rgb)
    n_big_pix = n_pix / (big_pix_dimen ** 2)
    if n_big_pix.is_integer():
        return n_big_pix
    else:
        raise Exception("calculate_n_of_big_pix: number of pixel is not divisible for big pix dimen.")


@dispatch(int, int)
def calculate_n_of_big_pix_per_row(n_big_pix, ratio_h_big_pix_dimen):
    return int(n_big_pix / ratio_h_big_pix_dimen)


def calculate_n_of_big_pix_per_col(n_big_pix, ratio_l_bp_dimen):
    return int(n_big_pix / ratio_l_bp_dimen)


@dispatch(object, int, int)
def calculate_n_of_big_pix_per_row(pix_list_rgb, big_pix_dimen, img_h):
    n_big_pix = calculate_n_of_big_pix(pix_list_rgb, big_pix_dimen)
    return int(calculate_n_of_big_pix_per_row(int(n_big_pix), int(img_h / big_pix_dimen)))


def get_big_pix_list(pix_list_rgb, big_pix_dimen, img_len, img_h):
    n_big_pix = int(calculate_n_of_big_pix(pix_list_rgb, big_pix_dimen))
    n_big_pix_per_row = int(calculate_n_of_big_pix_per_row(n_big_pix, int(img_h / big_pix_dimen)))
    big_pix_list = list()
    for j in range(n_big_pix_per_row):
        # with j we move on the rows of big pixels
        offset = j * big_pix_dimen * img_len
        for k in range(n_big_pix_per_row):
            # with k we move on the columns of big pixels
            a = list()
            offset_on_same_row = k * big_pix_dimen
            for i in range(big_pix_dimen ** 2):
                # with i we make the single big pixel
                # here we take the pixel for one big pix
                local_row_pos = i % big_pix_dimen
                # the new term allows me to change row in single big pix
                real_row_pos_first_big_pix = local_row_pos + (img_len * math.floor(i / big_pix_dimen))
                # the last two terms are needed to select the right big pixel
                i_pix = real_row_pos_first_big_pix + offset + offset_on_same_row
                a.append(pix_list_rgb[i_pix])
            assert len(a) == big_pix_dimen ** 2
            new_big_pix = bigPixel.BigPixel(a, j * n_big_pix_per_row + k, big_pix_dimen)
            big_pix_list.append(new_big_pix)
    return big_pix_list


def get_pix_list(big_pix_list, img_l, img_h):
    big_pix_dim = big_pix_list[0].dimension
    pix_list = list()
    for x in range(int(img_h / big_pix_dim)):
        offset_h = int(x * calculate_n_of_big_pix_per_row(len(big_pix_list), int(img_h / big_pix_dim)))
        for k in range(big_pix_dim):
            offset_h_local = int(k * big_pix_dim)
            for j in range(int(img_l / big_pix_dim)):
                for i in range(big_pix_dim):
                    pix_list.append(big_pix_list[j + offset_h].list_of_pix[i + offset_h_local])
    return pix_list


def retrieve_permutation(big_pix_list, path):
    f = open(path, "r")
    txt = f.read()
    tmp = ""
    k = 0
    for i in txt:
        if i == " ":
            if tmp.isdecimal():
                big_pix_list[k].number = int(tmp)
                k += 1
            tmp = ""
        else:
            tmp += str(i)
    if tmp.isdecimal():
        big_pix_list[k].number = int(tmp)
    f.close()


def print_solution(big_pix_list):
    for i in big_pix_list:
        print(str(i.number) + " ")


def save_solution(big_pix_list, path):
    f = open(path, "w")
    for i in big_pix_list:
        f.write(str(i.number) + " ")
    f.close()


def list_to_matrix(list_, row_l):
    mat = list()
    assert (len(list_) / row_l).is_integer()
    h = int(len(list_) / row_l)

    for i in range(h):
        mat.append(list())
        offset = i * row_l
        for j in range(row_l):
            mat[i].append(list_[j + offset])
    return mat


def matrix_to_list(matrix):
    list_ = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            list_.append(matrix[i][j])
    return list_
