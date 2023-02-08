import sys
from pathlib import Path

import pixelartconv.script

more_info = "For more info, type:\n    python -m pixelartconv --help"

if len(sys.argv) not in [2, 3, 4]:
    print("""Invalid syntax, please use one of the following:
    python -m pixelartconv [file_name]
    python -m pixelartconv [file_name] [width] [height]
    """)
    print(more_info)
    sys.exit(1)

file_name = sys.argv[1]
height = int(sys.argv[2]) if len(sys.argv) > 2 else 16
width = int(sys.argv[3]) if len(sys.argv) > 3 else None  # else... will be calculated when image is loaded
dims = (width, height)

if file_name == "--help":
    path = (Path(__file__).parent / "help.txt").resolve()
    with open(path) as f:
        print(f.read())
    sys.exit(2)

if file_name[0] == '-':
    print("Unknown command option.")
    print(more_info)
    sys.exit(1)

try:
    duration = pixelartconv.script.convert(file_name, dims)
except (ValueError, FileNotFoundError):  # correct exit code when issues encountered
    sys.exit(1)
