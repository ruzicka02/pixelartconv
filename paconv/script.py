from pathlib import Path
from time import time

from . import file_management
from . import logic


def convert(file_name: str, dims: tuple) -> float:
    """
    Converts an image to a pixel-art style.

    :param file_name: Name of file(s) or their relative path.
    :param dims: Target size of the resulting image.
    :return: Time duration of conversion (seconds).
    :raise FileNotFoundError: Image not found on given path.
    :raise ValueError: File with this name was found but was invalid.
    """
    start_time = time()

    print(f"Searched path is: {(Path().absolute() / Path(file_name)).parent.resolve()}")

    try:
        img = file_management.load_image(file_name, dims)
        colors = file_management.load_colors(file_name)
    except (ValueError, FileNotFoundError) as err:
        print(err)
        print("For more info, type:\n    python -m paconv --help")
        raise

    res = logic.convert_img(img, colors)
    path = file_management.save_image(res, False)

    duration = time() - start_time

    print(f"Conversion was successful.\nImage saved to {path}")
    print(f"Duration: {duration:.2f} s")

    return duration
