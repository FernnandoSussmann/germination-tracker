import glob
import argparse
import logging

from PIL import Image


def make_gif(
    source_folder,
    destination_folder,
    filename,
    images_format,
    duration,
    loops,
):
    try:
        frames = [Image.open(image) for image in sorted(glob.glob(f"{source_folder}/*.{images_format}"))]
        frame_one = frames[0]
        frame_one.save(
            f"{destination_folder}/{filename}.gif",
            format="gif",
            append_images=frames,
            save_all=True,
            duration=duration,
            loop=loops,
        )
    except Exception as e:
        logging.fatal(f"Unmapped exception: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Plant Germination GIF Creation",
        description="An utility based on web example to create a GIF using images that Germination Tracker took",
    )
    parser.add_argument(
        "-sf",
        "--source_folder",
        dest="source_folder",
        action="store",
        type=str,
        nargs="?",
        help="source folder with the images to create this GIF",
    )
    parser.add_argument(
        "-df",
        "--destination_folder",
        dest="destination_folder",
        action="store",
        type=str,
        nargs="?",
        help="destination folder to save this new GIF",
    )
    parser.add_argument(
        "-fn",
        "--filename",
        dest="filename",
        action="store",
        type=str,
        nargs="?",
        help="name new GIF will have",
    )
    parser.add_argument(
        "-imf",
        "--images_format",
        dest="images_format",
        action="store",
        type=str,
        nargs="?",
        help="source images format without '.'.\nExample: JPG, PNG, etc...",
    )
    parser.add_argument(
        "-d",
        "--duration",
        dest="duration",
        action="store",
        type=int,
        default=250,
        nargs="?",
        help="images duration in GIF in ms",
    )
    parser.add_argument(
        "-lps",
        "--loops",
        dest="loops",
        action="store",
        type=int,
        default=0,
        nargs="?",
        help="number of loops GIF should have. 0 means it loops forever",
    )
    args = parser.parse_args()
    make_gif(
        source_folder=args.source_folder,
        destination_folder=args.destination_folder,
        filename=args.filename,
        images_format=args.images_format,
        duration=args.duration,
        loops=args.loops,
    )
