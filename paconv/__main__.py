import sys
from pathlib import Path
from time import time

import paconv.logic, paconv.file_management

more_info = "For more info, type:\n    python paconv --help"

if len(sys.argv) not in [2, 4]:
    print("""Invalid syntax, please use one of the following:
    python paconv [file_name]
    python paconv [file_name] [width] [height]
    """)
    print(more_info)
    sys.exit(1)

file_name = sys.argv[1]
dims = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 2 else (16, 16)

if file_name == "--help":
    path = (Path(__file__).parent / "help.txt").resolve()
    with open(path) as f:
        print(f.read())
    sys.exit(2)

if file_name[0] == '-':
    print("Unknown command option.")
    print(more_info)
    sys.exit(1)

start_time = time()

print(f"Searched path is: {(Path() / 'img').resolve()}")

img = paconv.file_management.load_image(file_name, dims)
colors = paconv.file_management.load_colors(file_name)

if img is None or colors is None:
    print("One of the files were not found/opened correctly.")
    print(more_info)

    sys.exit(1)

res = paconv.logic.convert_img(img, colors)
path = paconv.file_management.save_image(res, False)

print(f"Conversion was successful.\nImage saved to {path}")
print(f"Duration: {time() - start_time:.2f} s")