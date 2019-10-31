from PIL import Image


def get_img_pixel(path):
    image = Image.open(path, 'r')
    w, h = image.size
    data = image.getdata()
    print(data)
    return data, w, h


def save_img(output_data, w, h, path):
    output_image = Image.new("RGB", (w, h))
    output_image.putdata(output_data)
    output_image.save(path, format="png")

