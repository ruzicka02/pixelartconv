# PAConv - Pixel Art Converter

Python script to quickly convert your image into a "pixel art" style. Image is downscaled and its color palette is reduced to only handful given colors.

Created by Simon Ruzicka, 2023

## Usage

First of all, make sure that the following files exist:
  - source image `[file_name].png`
  - list of colors `[file_name].txt`

These files should be located in your current working directory. In case the files are in another directory, include their common path instead of `[file_name]` when launching the script. NOTE: Both files must be in one directory so that the script locates them both correctly.

The list of colors in RGB must have the following format:

```
#00ff00
#ff00ff
...
```

Then, launch the script using:
```
python -m paconv [file_name]
python -m paconv [file_name] [height]
python -m paconv [file_name] [height] [width]
```

The behavior of script is as follows:
1) The resulting image will be 16 px in height - width will be automatically calculated from the original image ratio.
2) The resulting image will have given height - width will be automatically calculated from the original image ratio.
3) The resulting image will have given height and width.

Resulting image will be generated in the same directory as source files, named as `result.png`. There will also be an upscaled version with height approximately equal to 512 pixels (so that the upscale factor is a whole number) named `result_scaled.png`. This generates only in case where this upscale would have an effect (when the factor is at least 2).
