import pytest
from unittest.mock import MagicMock, patch
from services import InferService
import subprocess
import os


@pytest.fixture
def infer_service():
    return InferService()


def test_classify_success(infer_service):
    file_path = "test_file.java"
    expected_response = b"Infer classification result"

    # Mocking subprocess.check_output method
    with patch("subprocess.check_output") as mock_check_output:
        mock_check_output.return_value = expected_response

        result = infer_service.classify(file_path)

 


def test_classify_exception(infer_service):
    file_path = "test_file.java"
    expected_response = "ERROR"

    # Mocking subprocess.check_output method to raise an exception
    with patch("subprocess.check_output") as mock_check_output:
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "infer", "ERROR")

        result = infer_service.classify(file_path)

    assert result == expected_response
    mock_check_output.assert_called_once_with(
        infer_service.COMMAND.replace("FILE_PATH", file_path),
        shell=True,
        executable="/bin/bash",
        env=os.environ
    )
