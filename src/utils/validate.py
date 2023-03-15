import os
import sys


def validate_input_params(
    source_folder_path, output_folder_path, sync_interval, log_file_path
):
    """Checks if the paths given are indeed valid directories"""

    if not os.path.isdir(source_folder_path):
        print("Source folderpath is invalid")
        sys.exit()

    if not os.path.isdir(output_folder_path):
        print("Output folder path is invalid")
        sys.exit()

    if not os.path.isfile(log_file_path):
        print("Log file path is invalid")
        sys.exit()
