# PixelArtConv - Pixel Art Converter

Python script/package to quickly convert your image into a "pixel art" style. Image is downscaled and its color palette is reduced to only handful given colors.

Created by Simon Ruzicka, 2023

## Result Showcase

Original photo:

<img src="https://raw.githubusercontent.com/ruzicka02/paconv/master/img/seagull.png" width=512></img>

Generated pixel-art image - originally 128 px in height, with manually specified color palette:

<img src="https://raw.githubusercontent.com/ruzicka02/paconv/master/img/seagull_res128.png" width=512></img>

You can find more examples on the [GitHub project page](https://github.com/ruzicka02/pixelartconv) including the text color palettes.

## Installation

You can install this package with the following command:

```shell
pip install pixelartconv
```

Alternatively, you can download this repository and install it manually by yourself.

## Prerequisites

First of all, make sure that the source image named `[file_name].png` is located in your current working directory. In case the file is in another directory, include the relative path instead of `[file_name]` when launching the script. 

In addition, you can include a list of colors named `[file_name].txt`. In that case, the script parameter must be only the common name of the files - without any filename extension. Both files must be in one directory so that the script locates them both correctly.

The optional list of colors must have the following format (in RGB):

```
#00ff00
#ff00ff
...
```

## Usage

You can launch the script using the following commands:

```
python -m pixelartconv [file_name]
python -m pixelartconv [file_name] [height]
python -m pixelartconv [file_name] [height] [width]
```

The behavior of script is as follows:
1) The resulting image will be 64 px in height - width will be automatically calculated from the original image ratio.
2) The resulting image will have given height - width will be automatically calculated from the original image ratio.
3) The resulting image will have given height and width.

### Imported package

Additionally, you can import the package from your code/interactive shell and use the `convert` function with following interface:

```python
def convert(file_name: str, dims: tuple, palette_size: int = 6) -> float:
    """
    Converts an image to a pixel-art style.

    :param file_name: Name of file(s) or their relative path.
    :param dims: Target size of the resulting image.
    :param palette_size: Amount of colors in case the palette has to be generated.
    :return: Time duration of conversion (seconds).
    :raise FileNotFoundError: Image not found on given path.
    :raise ValueError: File with this name was found but was invalid.
    """
```

This will generate the image in the same way as if the script was launched. For example, the following snippet:

```python
import pixelartconv

pixelartconv.convert("test_image", (80, 120))
```

will result in the same generated image as the terminal command `python -m pixelartconv test_image 80 120`.

## Results

Resulting image will be generated in the same directory as source files, named as `result.png`. There will also be an upscaled version with height approximately equal to 512 pixels (so that the upscale factor is a whole number) named `result_scaled.png`. This generates only in case where this upscale would have an effect (when the factor is at least 2).
