"""
Internal logic for converting images to given colors.
"""

import logging

import numpy as np
import cv2


def px_distance_raw(p1: np.ndarray, p2: np.ndarray) -> int:
    """
    Calculates distance between the given pixel colors.

    :param p1: First input pixel
    :param p2: Second input pixel
    :return: Square of Euclidean distance between pixel values.
    """
    assert len(p1) == len(p2) == 3

    # res = 0
    # for x, y in zip(p1, p2):
    #     res += (x - y) ** 2
    #
    # return res

    return sum([(x - y) ** 2 for x, y in zip(p1, p2)])


def px_distance_hue(p1: np.ndarray, p2: np.ndarray) -> int:
    """
    Calculates distance between the hue of given pixel colors. Considers the pixel difference
    and its average brightess in the calculation.

    :param p1: First input pixel
    :param p2: Second input pixel
    :return: Square of Euclidean distance between pixel difference and shade of gray.
    """
    assert len(p1) == len(p2) == 3

    diff = p1 - p2
    brightness_avg = sum(diff) / 3

    return px_distance_raw(diff, np.array([brightness_avg for _ in range(3)]))


def px_distance(p1: np.ndarray, p2: np.ndarray) -> int:
    """
    Calculates combined distance between given pixel colors. Considers both hue and absolute difference
    with given weight.

    :param p1: First input pixel.
    :param p2: Second input pixel.
    :param weight: Weight of hue in comparison.
    :return: Square of HSL lightness difference.
    """
    weight = 1.0

    assert len(p1) == len(p2) == 3
    hue = px_distance_hue(p1, p2)
    raw = px_distance_raw(p1, p2)

    return weight * hue + raw < 0


px_distance_array = np.vectorize(px_distance, otypes=[int], signature="(n),(n)->()")


def compare_px(p1: np.ndarray, p2: np.ndarray, ref: np.ndarray, weight: float = 1.0) -> bool:
    """
    Compares two pixels with a reference pixel. Considers both hue and absolute difference
    with given weight.
    :param p1: First input pixel
    :param p2: Second input pixel
    :param ref: Reference pixel
    :param weight: Weight of hue in comparison.
    :return: True if p1 is closer to ref than p2.
    """

    return px_distance(p1, ref) < px_distance(p2, ref)


def find_closest_match(color_ref: np.ndarray, colors: np.ndarray) -> tuple:
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
    img_lab = cv2.cvtColor(img.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)  # (height, width, 3)

    colors_arr: np.ndarray = np.array(colors)
    distances = []
    for color in colors_arr:
        color_lab = cv2.cvtColor(color.reshape(1, 1, 3).astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
        color_lab = color_lab * np.ones(img_lab.shape)  # copy the source image dimensions

        distances.append(np.sum((img_lab - color_lab) ** 2, axis=-1))  # Euclidean distances of LAB colors

    dist_array = np.array(distances)  # (height, width, colorcount)
    logging.debug(f"{dist_array.shape=}")

    indexes = np.argmin(dist_array, axis=0)  # (height, width)
    logging.debug(f"{indexes=}")
    logging.debug(f"{indexes.shape=}")

    res = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i, j] = colors_arr[indexes[i, j]]

    # img = img.copy()
    # i, j = 0, 0
    # for row in img:
    #     for px in row:
    #         new_color = find_closest_match(px, colors)
    #         img[i, j] = new_color
    #         j += 1
    #     j = 0
    #     i += 1

    return res
