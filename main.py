import argparse
from datetime import datetime
from germination_tracker.video_capture_administrator import VideoCaptureAdministrator


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Plant Germination Tracker",
        description="Configures a webcan or any alike hardware to take pictures in a scheduled time",
    )
    parser.add_argument(
        "--cam_index",
        dest="cam_index",
        action="store",
        type=int,
        nargs="?",
        help="index which your cam is associated",
    )
    parser.add_argument(
        "--destination_folder",
        dest="destination_folder",
        action="store",
        type=str,
        nargs="?",
        help="where file will be saved",
    )
    parser.add_argument(
        "--filename",
        dest="filename",
        action="store",
        type=str,
        nargs="?",
        help="filename to be saved without extension",
    )

    args = parser.parse_args()
    vca = VideoCaptureAdministrator(
        cam_index=args.cam_index,
        destination_folder=args.destination_folder,
        filename=f"{args.filename}_{datetime.now()}.png",
    )
    vca.capture()
    vca.save_picture()
