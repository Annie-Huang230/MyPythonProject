"""
File: mirror_lake.py
Name: Annie Huang
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(original_mt):
    """
    :param original_mt: SimpleImage, the original image
    :return: SimpleImage, the reflected image
    """
    reflect_img = SimpleImage.blank(original_mt.width, original_mt.height*2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            colored_pixel = original_mt.get_pixel(x, y)
            blank_pixel_upper = reflect_img.get_pixel(x, y)
            blank_pixel_upper.red = colored_pixel.red
            blank_pixel_upper.green = colored_pixel.green
            blank_pixel_upper.blue = colored_pixel.blue

            blank_pixel_lower = reflect_img.get_pixel(x, reflect_img.height-1-y)
            blank_pixel_lower.red = colored_pixel.red
            blank_pixel_lower.green = colored_pixel.green
            blank_pixel_lower.blue = colored_pixel.blue
    return reflect_img


def main():
    """
    This file makes a mirrored image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = reflect(original_mt)
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
