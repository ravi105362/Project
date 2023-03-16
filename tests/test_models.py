import os
from src.models import FolderSynchronization
import shutil


def test_folder_sync_if_source_has_new_file(tmp_path, caplog):
    # Arrange
    shutil.rmtree("source_Folder", ignore_errors=True)
    os.mkdir("source_Folder")

    file_name = os.path.join("source_Folder", "test.text")
    fp = open(file_name, "w")
    fp.close()

    shutil.rmtree("output_Folder", ignore_errors=True)
    os.mkdir("output_Folder")

    # Act
    folder_sync_obj = FolderSynchronization(
        source_folder_path=os.path.join(os.getcwd(), "source_Folder"),
        output_folder_path=os.path.join(os.getcwd(), "output_Folder"),
    )
    folder_sync_obj.sync()

    # Assert
    assert (
        os.path.isfile(
            os.path.join(os.getcwd(), "output_Folder") + "/test.text"
        )
        is True
    )


def test_folder_sync_if_replica_has_new_file(tmp_path, caplog):
    # Arrange
    shutil.rmtree("source_Folder", ignore_errors=True)
    os.mkdir("source_Folder")

    shutil.rmtree("output_Folder", ignore_errors=True)
    os.mkdir("output_Folder")
    file_name = os.path.join("output_Folder", "test.text")
    fp = open(file_name, "w")
    fp.close()

    # Act
    folder_sync_obj = FolderSynchronization(
        source_folder_path=os.path.join(os.getcwd(), "source_Folder"),
        output_folder_path=os.path.join(os.getcwd(), "output_Folder"),
    )
    folder_sync_obj.sync()

    # Assert
    assert (
        os.path.isfile(
            os.path.join(os.getcwd(), "output_Folder") + "/test.text"
        )
        is False
    )


def test_folder_sync_if_source_has_new_folder_and_file(tmp_path, caplog):
    # Arrange
    shutil.rmtree("source_Folder", ignore_errors=True)
    os.makedirs("source_Folder/new_Folder")
    file_name = os.path.join("source_Folder/new_Folder", "test.text")
    fp = open(file_name, "w")
    fp.close()

    shutil.rmtree("output_Folder", ignore_errors=True)
    os.mkdir("output_Folder")

    # Act
    folder_sync_obj = FolderSynchronization(
        source_folder_path=os.path.join(os.getcwd(), "source_Folder"),
        output_folder_path=os.path.join(os.getcwd(), "output_Folder"),
    )
    folder_sync_obj.sync()

    # Assert
    assert (
        os.path.isfile(
            os.path.join(os.getcwd(), "output_Folder/new_Folder") + "/test.text"
        )
        is True
    )


def test_folder_sync_if_replica_has_new_folder_and_file(tmp_path, caplog):
    # arrange
    shutil.rmtree("source_Folder", ignore_errors=True)
    os.mkdir("source_Folder")

    shutil.rmtree("output_Folder", ignore_errors=True)
    os.makedirs("output_Folder/new_Folder")
    file_name = os.path.join("output_Folder/new_Folder", "test.text")
    fp = open(file_name, "w")
    fp.close()

    # Act
    folder_sync_obj = FolderSynchronization(
        source_folder_path=os.path.join(os.getcwd(), "source_Folder"),
        output_folder_path=os.path.join(os.getcwd(), "output_Folder"),
    )
    folder_sync_obj.sync()

    # Assert
    assert (
        os.path.isfile(
            os.path.join(os.getcwd(), "output_Folder/new_Folder") + "/test.text"
        )
        is False
    )
