"""
File: blur.py
Name: Annie Huang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    This function applies a blur effect to an image by averaging the RGB values
    of each pixel's nearest neighbors (including the pixel itself).

    :param img: SimpleImage (the original image to be blurred)
    :return: SimpleImage (the resulting blurred image)
    """

    new_img = SimpleImage.blank(img.width, img.height)  # Create a new blank image

    # Loop through every pixel of the original image
    for x in range(img.width):
        for y in range(img.height):
            new_r = 0  # Initialize variables to accumulate the total RGB values of neighboring pixels
            new_g = 0
            new_b = 0
            num = 0  # To count the number of valid neighboring pixels

            # Loop through the 3x3 grid of neighboring pixels (including the pixel itself)
            for i in range(-1, 2):  # (x-1, x, x+1)
                for j in range(-1, 2):  # (y-1, y, y+1)
                    pixel_x = x + i
                    pixel_y = y + j

                    # Check if the neighbor pixel is within the bounds of the image
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)  # Get the pixel from the original image
                            new_r += pixel.red  # Add the RGB values of the current neighbor pixel
                            new_g += pixel.green
                            new_b += pixel.blue
                            num += 1

            blur_img_pixel = new_img.get_pixel(x, y)  # Get the pixel in the new image at position (x, y)

            # Set the RGB values of the new pixel to the average of the neighbors' values
            blur_img_pixel.red = new_r // num
            blur_img_pixel.green = new_g // num
            blur_img_pixel.blue = new_b // num

    # Return the new blurred image
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


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
