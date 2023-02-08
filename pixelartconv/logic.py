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


def px_distance_hue(p1: tuple, p2: tuple) -> int:
    """
    Calculates distance between the hue of given pixel colors. Considers the pixel difference
    and its average brightess in the calculation.

    :param p1: First input pixel
    :param p2: Second input pixel
    :return: Square of Euclidean distance between pixel difference and shade of gray.
    """
    assert len(p1) == len(p2) == 3

    diff = tuple([val1 - val2 for val1, val2 in zip(p1, p2)])
    brightness_avg = sum(diff) / 3

    return px_distance(diff, tuple([brightness_avg for _ in range(3)]))


def px_distance_lightness(p1: tuple, p2: tuple) -> int:
    """
    Calculates distance between the lightness of given pixel colors. This function is currently not used.

    :param p1: First input pixel
    :param p2: Second input pixel
    :return: Square of HSL lightness difference.
    """
    assert len(p1) == len(p2) == 3

    return ((max(p1) + min(p1) - max(p2) - min(p2)) / 2) ** 2


def compare_px(p1: tuple, p2: tuple, ref: tuple, weight: float = 1.) -> bool:
    """
    Compares two pixels with a reference pixel. Considers both hue and absolute difference
    with given weight.
    :param p1: First input pixel
    :param p2: Second input pixel
    :param ref: Reference pixel
    :param weight: Weight of hue in comparison.
    :return: True if p1 is closer to ref than p2.
    """
    hue_diff = px_distance_hue(p1, ref) - px_distance_hue(p2, ref)
    px_diff = px_distance(p1, ref) - px_distance(p2, ref)

    return weight * hue_diff + px_diff < 0


def find_closest_match(color_ref: tuple, colors: list[tuple]) -> tuple:
    """
    Finds the color in given list that has minimal distance to the given pixel.

    :param color_ref: Given pixel color to complare with.
    :param colors: List of available colors.
    :return: Color from ``colors`` that matches ``px`` the best.
    """
    closest_match = colors[0]

    for color in colors:
        if compare_px(color, closest_match, color_ref):
            closest_match = color

    return closest_match


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
