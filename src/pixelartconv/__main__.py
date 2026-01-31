import sys
import argparse
import logging
from pathlib import Path

import pixelartconv


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(
        description="Convert images to pixel art with a limited color palette.",
        epilog=pixelartconv.HELP_STRING,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("file_name", type=str, help="Name of file(s) or their relative path.")
    parser.add_argument("height", type=int, nargs="?", default=64, help="Target height of the resulting image.")
    parser.add_argument("width", type=int, nargs="?", default=None, help="Target width of the resulting image.")
    parser.add_argument(
        "-c",
        "--colors",
        type=int,
        default=6,
        help="Amount of colors in case the palette has to be generated (default: 6).",
    )

    # file_name = sys.argv[1]
    # height = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    # width = int(sys.argv[3]) if len(sys.argv) > 3 else None  # else... will be calculated when image is loaded

    args = parser.parse_args()
    dims = (args.width, args.height)

    try:
        pixelartconv.convert(args.file_name, dims, palette_size=args.colors)
    except (ValueError, FileNotFoundError) as e:
        logging.error(f"{type(e)}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
