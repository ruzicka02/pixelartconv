# PAConv - Pixel Art Converter

Python script to quickly convert your image into a "pixel art" style. Image is downscaled and its color palette is reduced to only handful given colors.

Created by Simon Ruzicka, 2023

## Usage

First of all, make sure that the following files exist:
  - source image [filename].png
  - list of colors [filename].txt

These files should be located in a subdirectory named `img`. **TODO** include files in your current working directory

The list of colors in RGB must have the following format:

```
#00ff00
#ff00ff
...
```

Then, launch the script using:
```
python -m paconv [file_name]
python -m paconv [file_name] [width] [height]
```

if target width/height is not selected, the file will be 16 x 16 by default. Resulting image will be generated in the same directory as source files, named as `result.png`. There will also be an upscaled version with height approximately equal to 512 pixels (so that the upscale factor is a whole number) named `result_scaled.png`. This generates only in case where this upscale would have an effect (when the factor is at least 2).
