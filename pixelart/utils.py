"""
Utility functions for the script.
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

    return image


def load_image(name: str, dims: tuple = (10, 10), percent_filled: float = 0.7):
    """
    Loads a PNG image from the `saves/images` directory, performs various operations
    and returns it as an array. In case something goes wrong, returns None.
    """
    name += ".png"
    path = Path(__file__).parent.parent
    path = (path / 'img' / name).resolve()
    try:
        image = image_prepare(path, dims)
        return image
    except (FileNotFoundError, UnidentifiedImageError, ValueError, AssertionError):
        return None
