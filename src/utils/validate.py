import os


def validate_input_params(
    source_folder_path, output_folder_path, sync_interval, log_file_path
) -> bool:
    """Checks if the paths given are indeed valid directories"""
    result = True

    if not os.path.isdir(source_folder_path):
        print("Source folder path is invalid")
        result = False

    if not os.path.isdir(output_folder_path):
        print("Output folder path is invalid")
        result = False

    if not isinstance(sync_interval, int):
        print("Sync Interval is not integer value")
        result = False

    if not os.path.isfile(log_file_path):
        print("Log file path is invalid")
        result = False

    return result
