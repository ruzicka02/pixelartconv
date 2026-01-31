HELP_STRING = """---

# PixelArtConv - Pixel Art Converter

Created by Simon Ruzicka, 2023

You can launch the script using one of the following commands:

```
python -m pixelartconv [file_name]
```
1) The resulting image will be 64 px in height - width will be automatically
calculated.

```
python -m pixelartconv [file_name] [height]
```
2) The resulting image will have given height - width will be automatically
calculated.

```
python -m pixelartconv [file_name] [height] [width]
```
3) The resulting image will have given height and width.

Resulting image will be generated in the current working directory, named as
result.png.  There will also be an upscaled version with height approximately
equal to 512 pixels (so that the upscale factor is a whole number) named
result_scaled.png.  This generates only in case where this upscale would have an
effect (when the factor is greater than 1 when rounded to integer).

## Color specification

You can include a list of colors by creating a `.txt` file with the same name as
the image.  In that case, this list will be used instead of the one that is
usually automatically generated.  Both files must be in one directory so that
the script locates them both correctly.

The optional list of colors must have the following format (in RGB):

```
#00ff00
#ff00ff
...
```"""
