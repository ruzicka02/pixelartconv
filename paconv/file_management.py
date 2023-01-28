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

    image = ImageOps.fit(image, dims, method=Image.BICUBIC)
    image = np.asarray(image)

    # remove alpha channel/transparency
    if image.shape[2] == 4:
        image = image[:, :, :3]

    assert image.shape == (*dims, 3)

    return image


def load_image(name: str, dims: tuple):
    """
    Loads a PNG image from the `img` directory, performs various operations
    and returns it as an array. In case something goes wrong, returns None.

    :param str name: File name.
    :param tuple dims: Pair of target image dimensions (width, height).
    :return: numpy.ndarray or None
    """
    name += ".png"
    path = Path(__file__).parent.parent
    path = (path / 'img' / name).resolve()
    try:
        image = image_prepare(path, dims)
        return image
    except (FileNotFoundError, UnidentifiedImageError, ValueError, AssertionError):
        return None


def save_image(data: np.ndarray, show: bool = False, name: str = "export"):
    path = Path(__file__).parent.parent
    path = (path / (name + ".png")).resolve()

    image = Image.fromarray(np.uint8(data)).convert('RGB')
    image.save(path)

    path = (path.parent / (name + "_scaled.png")).resolve()
    factor = round(512 / data.shape[0])  # type 'int'
    if factor > 1:
        image = ImageOps.scale(image, factor, resample=Image.NEAREST)
        image.save(path)

    if show:
        image.show()


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
        return None

    with open(path, 'r') as file:
        lines = [line.rstrip().lstrip('#') for line in file]

    color_codes = [tuple(int(ln[i:i + 2], 16) for i in (0, 2, 4)) for ln in lines]
    return color_codes
