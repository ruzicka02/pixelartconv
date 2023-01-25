import sys

import logic, file_management

if len(sys.argv) not in [2, 4]:
    print("""Invalid syntax, please use one of the following:
    python paconv [file_name]
    python paconv [file_name] [width] [height]

For more info, type:
    python paconv --help""")
    sys.exit(1)

file_name = sys.argv[1]
dims = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 2 else (16, 16)

if file_name == "--help":
    print("""PAConv - Pixel Art Converter
Created by Simon Ruzicka, 2023

First of all, make sure that the `img` directory contains:
  - source image [filename].png
  - list of colors [filename].txt
  
The list of colors must have the following format:

#00ff00
#ff00ff
...

Then, launch the script using:
    python paconv [file_name]
    python paconv [file_name] [width] [height]
    
if target width/height is not selected, the file will be 16 x 16 by default.
Resulting image will be generated in the root directory as `result.png`.""")
    sys.exit(1)

if file_name[0] == '-':
    print("""Unknown command option.
    
For more info, type:
    python paconv --help""")
    sys.exit(1)

img = file_management.load_image(file_name, dims)
colors = file_management.load_colors(file_name)

if img is None or colors is None:
    print("""One of the files were not found/opened correctly.

For more info, type:
    python paconv --help""")
    sys.exit(1)

res = logic.convert_img(img, colors)
file_management.save_image(res, False)

print("Conversion was successful.")
