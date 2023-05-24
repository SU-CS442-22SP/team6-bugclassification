import pytest
from unittest import mock
import subprocess
from services import PMDService


@pytest.fixture
def pmd_service():
    pmd_config_path = "path/to/pmd_config.xml"
    return PMDService(pmd_config_path)


def test_classify_success(pmd_service):
    pmd_config_path = "path/to/pmd_config.xml"
    file_path = "path/to/file.java"
    expected_response = 'ERROR'

    # Mocking subprocess.check_output to return the expected response
    with mock.patch("subprocess.check_output") as mock_check_output:
        mock_check_output.return_value = expected_response

        response = pmd_service.classify(file_path)

        # Assert the response
        assert response == expected_response

        # Assert that subprocess.check_output was called with the correct arguments
        mock_check_output.assert_called_once_with(
            f"pmd check -f json -R {pmd_config_path} -d {file_path}",
            shell=True,
            executable="/bin/bash",
            env=mock.ANY,
        )


def test_classify_exception(pmd_service):
    file_path = "path/to/file.java"
    pmd_config_path = "path/to/pmd_config.xml"


    # Mocking subprocess.check_output to raise an exception
    with mock.patch("subprocess.check_output") as mock_check_output:
        mock_check_output.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd=""
        )

        response = pmd_service.classify(file_path)

        # Assert the response
        assert response == "ERROR"

        # Assert that subprocess.check_output was called with the correct arguments
        mock_check_output.assert_called_once_with(
            f"pmd check -f json -R {pmd_config_path} -d {file_path}",
            shell=True,
            executable="/bin/bash",
            env=mock.ANY,
        )
