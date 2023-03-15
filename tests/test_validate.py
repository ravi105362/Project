from src.utils.validate import validate_input_params


def test_validate_method_incorrect_parameters(caplog):
    result = validate_input_params(
        source_folder_path="xyz",
        output_folder_path="xyz",
        sync_interval=2.3,
        log_file_path="xyz",
    )
    assert result is False


def test_validate_method_correct_parameters(caplog):
    result = validate_input_params(
        source_folder_path="sourceFolder",
        output_folder_path="outputFolder",
        sync_interval=2,
        log_file_path="src/logs/log.log",
    )
    assert result is True
