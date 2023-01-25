"""
IO functions for the script.
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageOps, UnidentifiedImageError


def image_prepare(path: Path, dims: tuple) -> np.ndarray:
    """
    Opens the image and does various basic operations.
    """
    image = Image.open(path)

    # cannot upscale image
    assert image.size[0] >= dims[0] and image.size[1] >= dims[1]

    image = ImageOps.fit(image, dims)
    image = np.asarray(image)

    assert image.shape == (*dims, 3)

    return image


def load_image(name: str, dims: tuple = (10, 10), percent_filled: float = 0.7):
    """
    Loads a PNG image from the `img` directory, performs various operations
    and returns it as an array. In case something goes wrong, returns None.

    :return: numpy.ndarray or None
    """
    name += ".png"
    path = Path(__file__).parent.parent
    path = (path / 'img' / name).resolve()
    try:
        image = image_prepare(path, dims)
        return image
    except (FileNotFoundError, UnidentifiedImageError, ValueError, AssertionError) as err:
        print(err)
        return None


def save_image(data: np.ndarray, name: str = "export"):
    name += ".png"
    path = Path(__file__).parent.parent
    path = (path / name).resolve()

    image = Image.fromarray(np.uint8(data)).convert('RGB')
    image.save(path)


def load_colors(name: str):
    """
    Loads color data from a text file in the `img` directory.

    :param str name: File name.
    :return: List of tuples (color codes, length 3) or None
    """

    name += ".txt"
    path = Path(__file__).parent.parent
    path = (path / 'img' / name).resolve()

    if not path.is_file():
        print("File not found - aborting operation")
        return None

    with open(path, 'r') as file:
        lines = [line.rstrip().lstrip('#') for line in file]

    color_codes = [tuple(int(ln[i:i + 2], 16) for i in (0, 2, 4)) for ln in lines]
    return color_codes
