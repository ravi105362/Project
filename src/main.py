import argparse
from models import FolderSynchronization
from utils.validate import validate_input_params
from utils.threads import RepeatedTimer
import sys
import os

if __name__ == "__main__":
    """
    Main function called upon invocation
    """

    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        "-s", "--source_folder", help="your source folder path"
    )
    argParser.add_argument(
        "-o", "--output_folder", help="your output folder path"
    )
    argParser.add_argument(
        "-i",
        "--sync_interval",
        type=int,
        help="Synchronization interval in seconds",
    )
    argParser.add_argument("-l", "--log_file_path", help="your log file path")

    args = argParser.parse_args()
    result = validate_input_params(
        source_folder_path=args.source_folder,
        output_folder_path=args.output_folder,
        sync_interval=args.sync_interval,
        log_file_path=args.log_file_path,
    )
    if result is False:
        sys.exit()

    sync_obj = FolderSynchronization(
        source_folder_path=args.source_folder,
        output_folder_path=args.output_folder,
    )

    os.environ["LOGGER_FOLDER"] = args.log_file_path
    repeat_call = RepeatedTimer(args.sync_interval, sync_obj.sync)
