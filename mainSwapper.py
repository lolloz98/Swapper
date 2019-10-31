import swapper
import converter
import imgGetSet

def menu():
    return int(input("################################################################\n"
                     "0- to swap a big pixel\n"
                     "1- to swap little row\n"
                     "2- to swap little column\n"
                     "3- to swap little square\n"
                     "4- to save and exit\n"))


def get_pos(big_pix_per_row, pix_number):
    print("Prompting for the pixel number: " + str(pix_number))
    r = int(input("pixel row = "))
    c = int(input("pixel col = "))
    return swapper.calc_pos_from_row_column(big_pix_per_row, r, c)


def save_and_view_img(big_pix_list, img_l, img_h, img_path, sol_path):
    converter.save_solution(big_pix_list, sol_path)
    pix_list = converter.get_pix_list(big_pix_list, img_l, img_h)
    imgGetSet.save_img(pix_list, img_l, img_h, img_path)

def main():
    print("Be careful: the images must end with .png and the text files with .txt !!!")
    input_path = input("type the path of the img you wanna modify (.png): ")
    output_path_img = input("type the path where you'll wanna store the img (.png): ")
    output_path_sol = input("type the path where you'll wanna store the solution (.txt): ")
    big_pix_dimen = int(input("type the dimen of one big pixel: "))

    img, w, h = imgGetSet.get_img_pixel(input_path)
    big_pix_list = converter.get_big_pix_list(img, big_pix_dimen, w, h)

    number_big_pix_per_row = int(converter.calculate_n_of_big_pix_per_row(
        int(converter.calculate_n_of_big_pix(img, big_pix_dimen)), int(h / big_pix_dimen)
    ))

    is_retrieving = int(input("if you want to retrieve permutation list (.txt) type 1. If not type 0\n"))
    if is_retrieving == 1:
        path = input("type the path of your file with permutation: ")
        converter.retrieve_permutation(big_pix_list, path)

    i = menu()
    while i != 4:
        if i == 0:
            pos1 = get_pos(number_big_pix_per_row, 1)
            pos2 = get_pos(number_big_pix_per_row, 2)
            swapper.single_swap(big_pix_list, pos1, pos2)
        elif i == 1:
            print("I need the value of the start big pixels from the left of the rows")
            pos1 = get_pos(number_big_pix_per_row, 1)
            pos2 = get_pos(number_big_pix_per_row, 2)
            row_l = int(input("number of big pixel to swap: "))
            swapper.little_row_swap(big_pix_list, number_big_pix_per_row, pos1, pos2, row_l)
        elif i == 2:
            print("I need the value of the start big pixels from the left of the columns")
            pos1 = get_pos(number_big_pix_per_row, 1)
            pos2 = get_pos(number_big_pix_per_row, 2)
            col_l = int(input("number of big pixel to swap: "))
            swapper.little_column_swap(big_pix_list, number_big_pix_per_row, pos1, pos2, col_l)
        elif i == 3:
            print("values of the pixel on the left up corner of the square")
            pos1 = get_pos(number_big_pix_per_row, 1)
            pos2 = get_pos(number_big_pix_per_row, 2)
            side = int(input("side of the square: "))
            swapper.little_square_swap(big_pix_list, number_big_pix_per_row, pos1, pos2, side)
        save_and_view_img(big_pix_list, w, h, output_path_img, output_path_sol)
        i = menu()


if __name__ == "__main__":
    main()
