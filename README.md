# PAConv - Pixel Art Converter

Python script to quickly convert your image into a "pixel art" style. Image is downscaled and its color palette is reduced to only handful given colors.

Created by Simon Ruzicka, 2023

## Usage

First of all, make sure that the `img` directory contains:
  - source image [filename].png
  - list of colors [filename].txt

The list of colors in RGB must have the following format:

```
#00ff00
#ff00ff
...
```

Then, launch the script using:
```
    python paconv [file_name]
    python paconv [file_name] [width] [height]
```

if target width/height is not selected, the file will be 16 x 16 by default. Resulting image will be generated in the root directory as `result.png`. There will also be an upscaled version to 512 x 512 named `result_scaled.png`.

