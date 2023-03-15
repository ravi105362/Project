import argparse
from models import FolderSynchronization
from utils.validate import validate_input_params
from utils.threads import RepeatedTimer
import os

if __name__ == "__main__":
    """
    Main function called upon invocation
    """

    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        "-s", "--source_folder", help="your source folder name"
    )
    argParser.add_argument(
        "-o", "--output_folder", help="your output folder name"
    )
    argParser.add_argument(
        "-i",
        "--sync_interval",
        type=int,
        help="Synchronization interval in seconds",
    )
    argParser.add_argument("-l", "--log_file_path", help="your log file path")

    args = argParser.parse_args()
    validate_input_params(
        source_folder_path=args.source_folder,
        output_folder_path=args.output_folder,
        sync_interval=args.sync_interval,
        log_file_path=args.log_file_path,
    )

    sync_obj = FolderSynchronization(
        source_folder_path=args.source_folder,
        output_folder_path=args.output_folder,
        sync_interval=args.sync_interval,
    )

    os.environ["LOGGER_FOLDER"] = args.log_file_path
    repeat_call = RepeatedTimer(args.sync_interval, sync_obj.sync)
