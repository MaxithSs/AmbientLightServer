import platform

import PIL.ImageFilter
from PIL import Image


def get_current_wallpaper():
    current_os = platform.system().lower()
    if current_os == "linux":
        image = Image.open('/usr/share/backgrounds/brad-huchteman-stone-mountain.jpg')
        image.show()

        rgb_img = image.convert('RGB')
        r, g, b = rgb_img.getpixel((600, 471))
        print(r, g, b)
        print(rgb2hex(r, g, b))

        blur_image = image.filter(PIL.ImageFilter.GaussianBlur(100))
        blur_image.show()
    elif current_os == "windows":
        print("hello world")


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
