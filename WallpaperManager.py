import PIL.ImageFilter
from PIL import Image


def get_current_wallpapers_color():
    # todo - method which gets current system background
    image = Image.open('/usr/share/backgrounds/joshua-coleman-something-yellow.jpg')
    blur_image = image.filter(PIL.ImageFilter.GaussianBlur(100))
    width, height = image.size

    rgb_img = blur_image.convert('RGB')

    steps = 100
    r, g, b = 0, 0, 0
    for x in range(0, width, steps):
        for y in range(0, height, steps):
            a, b, c = rgb_img.getpixel((x, y))
            r = r + a
            g = g + b
            b = b + c

    r = round(r / ((width * height) / steps) * 100)
    g = round(g / ((width * height) / steps) * 100)
    b = round(b / ((width * height) / steps) * 100)
    response = str(r) + " " + str(g) + " " + str(b)
    return response


def convert_rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
