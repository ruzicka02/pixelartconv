import sys
import argparse
from pathlib import Path

import pixelartconv


def main():
    path = (Path(__file__).parent / "help.txt").resolve()
    with open(path) as f:
        help_text = f.read()

    parser = argparse.ArgumentParser(
        description="Convert images to pixel art with a limited color palette.",
        epilog=help_text,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("file_name", type=str, help="Name of file(s) or their relative path.")
    parser.add_argument("height", type=int, nargs="?", default=64, help="Target height of the resulting image.")
    parser.add_argument("width", type=int, nargs="?", default=None, help="Target width of the resulting image.")

    # file_name = sys.argv[1]
    # height = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    # width = int(sys.argv[3]) if len(sys.argv) > 3 else None  # else... will be calculated when image is loaded

    args = parser.parse_args()
    dims = (args.width, args.height)

    try:
        pixelartconv.convert(args.file_name, dims)
    except (ValueError, FileNotFoundError):  # correct exit code when issues encountered
        sys.exit(1)


if __name__ == "__main__":
    main()
