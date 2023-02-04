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

    # calculate result width if missing
    if dims[0] is None:
        dims = (round(dims[1] * image.size[0] / image.size[1]), dims[1])

    # cannot upscale image
    assert image.size[0] >= dims[0] and image.size[1] >= dims[1], \
        "Original image dimensions must be greater or equal to new dimensions."

    image = ImageOps.fit(image, dims, method=Image.BICUBIC)
    image = np.asarray(image)

    # remove alpha channel/transparency
    if image.shape[2] == 4:
        image = image[:, :, :3]

    # conversion to array "transposes" the image
    assert image.shape == (dims[1], dims[0], 3), "Issues encountered when converting image to matrix."

    return image


def load_image(name: str, dims: tuple):
    """
    Loads a PNG image from the current path, performs various operations
    and returns it as an array. In case something goes wrong, returns None.

    :param str name: File name.
    :param tuple dims: Pair of target image dimensions (width, height).
    :return: numpy.ndarray or None
    """
    name += ".png"
    path = (Path() / name).resolve()

    try:
        image = image_prepare(path, dims)
        return image
    except FileNotFoundError:
        print(f"File {name} not found.")
    except UnidentifiedImageError:
        print(f"File {name} seems to be problematic - check correct file formatting.")
    except (ValueError, AssertionError) as err:
        print(err)

    return None


def save_image(data: np.ndarray, show: bool = False, name: str = "export") -> Path:
    """
    Saves the given numpy array as an image with given name. Returns the path 
    to which file has been saved.

    :param np.ndarray data: Source image data.
    :param bool show: EXPERIMENTAL - Shows the image with built-in Pillow function when set as True.
    :param str name: File name.
    :return: Resulting file path.
    """
    path = (Path() / (name + ".png")).resolve()

    image = Image.fromarray(np.uint8(data)).convert('RGB')
    image.save(path)

    path = (path.parent / (name + "_scaled.png")).resolve()
    factor = round(512 / data.shape[0])  # type 'int'
    if factor > 1:
        image = ImageOps.scale(image, factor, resample=Image.NEAREST)
        image.save(path)

    if show:
        image.show()

    return path


def load_colors(name: str):
    """
    Loads color data from a text file in the current path.

    :param str name: File name.
    :return: List of tuples (color codes, length 3) or None
    """

    name += ".txt"
    path = (Path() / name).resolve()

    if not path.is_file():
        print(f"File {name} not found.")
        return None

    with open(path, 'r') as file:
        lines = [line.rstrip().lstrip('#') for line in file]

    color_codes = [tuple(int(ln[i:i + 2], 16) for i in (0, 2, 4)) for ln in lines]
    return color_codes
