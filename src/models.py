from dataclasses import dataclass
import filecmp
import os
import shutil
import logging
from settings import LOGGER_FOLDER

logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(LOGGER_FOLDER),
    format="%(asctime)s :: %(levelname)s :: %(message)s",
)


@dataclass
class FolderSynchronization:
    source_folder_path: str
    output_folder_path: str

    def sync(self):
        try:
            self._sync_data(self.source_folder_path, self.output_folder_path)
        except Exception as exc:
            logging.error(f"Not able to sync {exc}")

    def _sync_data(self, source_folder_path, output_folder_path):
        """This method checks for the differences between two folders"""

        comparison = filecmp.dircmp(source_folder_path, output_folder_path)

        if comparison.common_dirs:
            for d in comparison.common_dirs:
                self._sync_data(
                    os.path.join(source_folder_path, d),
                    os.path.join(output_folder_path, d),
                )

        if comparison.left_only:
            self._copy(
                comparison.left_only, source_folder_path, output_folder_path
            )

        if comparison.right_only:
            self._delete(comparison.right_only, output_folder_path)

        source_newer = []
        output_newer = []
        if comparison.diff_files:
            for d in comparison.diff_files:
                source_modified = os.stat(
                    os.path.join(source_folder_path, d)
                ).st_mtime
                output_modified = os.stat(
                    os.path.join(output_folder_path, d)
                ).st_mtime
                if source_modified > output_modified:
                    source_newer.append(d)
                else:
                    output_newer.append(d)
                    source_newer.append(d)
        self._delete(output_newer, output_folder_path)
        self._copy(source_newer, source_folder_path, output_folder_path)

    def _copy(self, file_list, src, dest):
        """This method copies a list of files from a source node
        to a destination node"""

        for f in file_list:
            srcpath = os.path.join(src, os.path.basename(f))
            if os.path.isdir(srcpath):
                shutil.copytree(
                    srcpath, os.path.join(dest, os.path.basename(f))
                )
            else:
                shutil.copy2(srcpath, dest)
                print(
                    'Copied "'
                    + os.path.basename(srcpath)
                    + '" from "'
                    + os.path.dirname(srcpath)
                    + '" to "'
                    + dest
                    + '"'
                )
                logging.info(
                    'Copied "'
                    + os.path.basename(srcpath)
                    + '" from "'
                    + os.path.dirname(srcpath)
                    + '" to "'
                    + dest
                    + '"'
                )

    def _delete(self, file_list, src):
        """This methods deletes a list of files from a output
        folder path not in source folder"""

        for f in file_list:
            srcpath = os.path.join(src, os.path.basename(f))
            if os.path.isdir(srcpath):
                shutil.rmtree(srcpath)
            else:
                os.remove(srcpath)
                print(
                    'Deleted "'
                    + os.path.basename(srcpath)
                    + '" from "'
                    + os.path.dirname(srcpath)
                    + '"'
                )
                logging.info(
                    'Deleted "'
                    + os.path.basename(srcpath)
                    + '" from "'
                    + os.path.dirname(srcpath)
                    + '"'
                )
