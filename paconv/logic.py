"""
Internal logic for converting images to given colors.
"""
import numpy as np


def px_distance(p1: tuple, p2: tuple) -> int:
    """
    Calculates distance between the given pixel colors.

    :param p1: First input pixel
    :param p2: Second input pixel
    :return: Square of Euclidean distance between pixels.
    """
    assert len(p1) == len(p2) == 3

    # res = 0
    # for x, y in zip(p1, p2):
    #     res += (x - y) ** 2
    #
    # return res

    return sum([(x - y) ** 2 for x, y in zip(p1, p2)])


def find_closest_match(px: tuple, colors: list[tuple]) -> tuple:
    """
    Finds the color in given list that has minimal distance to the given pixel.

    :param px: Given pixel to complare with.
    :param colors: List of available colors.
    :return: Color from ``colors`` that matches ``px`` the best.
    """
    min_dist = 3 * (256 ** 2)
    argmin_dist = None

    for c in colors:
        dist = px_distance(px, c)
        if dist < min_dist:
            min_dist, argmin_dist = dist, c

    return argmin_dist


def convert_img(img: np.ndarray, colors: list[tuple]) -> np.ndarray:
    """
    Finds the closest match for each pixel in the image. Returns a copy of the
    original image, where the pixels are replaced only with colors from the palette.

    :param img: Reference image.
    :param colors: Color palette.
    :return: Copy of image with only colors from palette.
    """

    img = img.copy()
    i, j = 0, 0
    for row in img:
        for px in row:
            new_color = find_closest_match(tuple(px), colors)
            img[i, j] = new_color
            j += 1
        j = 0
        i += 1

    return img
