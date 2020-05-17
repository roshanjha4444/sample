import sys
import os
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values
p
    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    # Your code goes here
    red_difference = red - pixel.red
    green_difference = green - pixel.green
    blue_difference = blue - pixel.blue
    dist = (red_difference ** 2 + green_difference ** 2 + blue_difference ** 2)
    return int(dist)


def get_best_pixel(pixel1, pixel2, pixel3):
    """
    Given three pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        three pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel(green_pixel, blue_pixel, blue_pixel)
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel(green_pixel, green_pixel, blue_pixel)
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel(red_pixel, red_pixel, red_pixel)
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    # Your code goes here
    red = (pixel1.red + pixel2.red + pixel3.red) // 3
    green = (pixel1.green + pixel2.green + pixel3.green) // 3
    blue = (pixel1.blue + pixel2.blue + pixel3.blue) // 3

    dist1 = get_pixel_dist(pixel1, red, green, blue)
    dist2 = get_pixel_dist(pixel2, red, green, blue)
    dist3 = get_pixel_dist(pixel3, red, green, blue)
    dist = [dist1, dist2, dist3]
    if min(dist) == dist1:
        return pixel1
    if min(dist) == dist2:
        return pixel2
    if min(dist) == dist3:
        return pixel3
1

def create_ghost(image1, image2, image3):
    """
    Given three image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        three images to be processed
    Returns:
        a new Ghost solution image
    """
    # Your code goes here
    ghost = SimpleImage.blank(image1.width, image1.height)
    for x in range(ghost.width):
        for y in range(ghost.height):
            pixel1 = image1.get_pixel(x, y)
            pixel2 = image2.get_pixel(x, y)
            pixel3 = image3.get_pixel(x, y)
            ghost.set_pixel(x, y, get_best_pixel(pixel1, pixel2, pixel3))
    return ghost


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpeg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images[0], images[1], images[2])
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()