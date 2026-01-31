import sys
from pathlib import Path

import pixelartconv

MORE_INFO = "For more info, type:\n    python -m pixelartconv --help"


def main():
    if len(sys.argv) not in [2, 3, 4]:
        print("""Invalid syntax, please use one of the following:
        python -m pixelartconv [file_name]
        python -m pixelartconv [file_name] [width] [height]
        """)
        print(MORE_INFO)
        sys.exit(1)

    file_name = sys.argv[1]
    height = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    width = int(sys.argv[3]) if len(sys.argv) > 3 else None  # else... will be calculated when image is loaded
    dims = (width, height)

    if "--help" in sys.argv or "-h" in sys.argv:
        path = (Path(__file__).parent / "help.txt").resolve()
        with open(path) as f:
            print(f.read())
        sys.exit(2)

    if file_name[0] == "-":
        print("Unknown command option.")
        print(MORE_INFO)
        sys.exit(1)

    try:
        pixelartconv.convert(file_name, dims)
    except (ValueError, FileNotFoundError):  # correct exit code when issues encountered
        sys.exit(1)


if __name__ == "__main__":
    main()
