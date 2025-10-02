"""
File: blur.py
Name: Annie Huang
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage
    :return: SimpleImage, the blurred image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            blur_img_pixel = new_img.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y + 1)
                p3 = img.get_pixel(x + 1, y)
                p4 = img.get_pixel(x + 1, y + 1)
                avg_red = (p1.red+p2.red+p3.red+p4.red)//4
                avg_blue = (p1.blue+p2.blue+p3.blue+p4.blue)//4
                avg_green = (p1.green+p2.green+p3.green+p4.green)//4

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y + 1)
                p3 = img.get_pixel(x - 1, y)
                p4 = img.get_pixel(x - 1, y + 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red) // 4
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4
                avg_green = (p1.green + p2.green + p3.green + p4.green) // 4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y - 1)
                p3 = img.get_pixel(x + 1, y)
                p4 = img.get_pixel(x + 1, y - 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red) // 4
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4
                avg_green = (p1.green + p2.green + p3.green + p4.green) // 4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y - 1)
                p3 = img.get_pixel(x - 1, y)
                p4 = img.get_pixel(x - 1, y - 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red) // 4
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4
                avg_green = (p1.green + p2.green + p3.green + p4.green) // 4

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y + 1)
                p3 = img.get_pixel(x - 1, y)
                p4 = img.get_pixel(x + 1, y + 1)
                p5 = img.get_pixel(x + 1, y)
                p6 = img.get_pixel(x - 1, y + 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
                avg_green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x + 1, y)
                p3 = img.get_pixel(x - 1, y)
                p4 = img.get_pixel(x, y - 1)
                p5 = img.get_pixel(x + 1, y)
                p6 = img.get_pixel(x + 1, y - 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
                avg_green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y + 1)
                p3 = img.get_pixel(x, y - 1)
                p4 = img.get_pixel(x + 1, y + 1)
                p5 = img.get_pixel(x + 1, y)
                p6 = img.get_pixel(x + 1, y - 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
                avg_green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x, y + 1)
                p3 = img.get_pixel(x, y - 1)
                p4 = img.get_pixel(x - 1, y + 1)
                p5 = img.get_pixel(x - 1, y)
                p6 = img.get_pixel(x - 1, y - 1)
                avg_red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                avg_blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
                avg_green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6

            else:
                # Inner pixels.
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x - 1, y - 1)
                p3 = img.get_pixel(x - 1, y)
                p4 = img.get_pixel(x + 1, y)
                p5 = img.get_pixel(x, y - 1)
                p6 = img.get_pixel(x + 1, y - 1)
                p7 = img.get_pixel(x - 1, y + 1)
                p8 = img.get_pixel(x, y + 1)
                p9 = img.get_pixel(x + 1, y + 1)
                avg_red = (p1.red+p2.red+p3.red+p4.red+p5.red+p6.red+p7.red+p8.red+p9.red)//9
                avg_green = (p1.green+p2.green+p3.green+p4.green+p5.green+p6.green+p7.green+p8.green+p9.green)//9
                avg_blue = (p1.blue+p2.blue+p3.blue+p4.blue+p5.blue+p6.blue+p7.blue+p8.blue+p9.blue)//9
            blur_img_pixel.red = avg_red
            blur_img_pixel.green = avg_green
            blur_img_pixel.blue = avg_blue
    return new_img


def main():
    """
    This file blurs the image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
