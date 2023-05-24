import pytest
import openai
from unittest.mock import MagicMock, patch
from services import ChatGPTService
from config import settings


@pytest.fixture
def chatgpt_service():
    return ChatGPTService()


def test_start_chat(chatgpt_service):
    messages = chatgpt_service._start_chat()
    assert len(messages) == 1
    assert messages[0]["role"] == "system"
    assert messages[0]["content"] == settings.CHATGPT_START_MESSAGE


def test_classify_success(chatgpt_service):
    file_path = "test_file.txt"
    buggged_code = "print('Hello, World!')"
    expected_response = "Bug classification result"

    # Mocking openai.ChatCompletion.create method
    with patch("openai.ChatCompletion.create") as mock_create:
        mock_create.return_value = {
            "choices": [
                {
                    "message": {
                        "content": expected_response
                    }
                }
            ]
        }

        # Mocking the file read
        with patch("builtins.open", MagicMock(return_value=MagicMock(read=MagicMock(return_value=buggged_code)))):

            result = chatgpt_service.classify(file_path)

    assert result == expected_response



def test_classify_exception(chatgpt_service):
    file_path = "test_file.txt"
    expected_response = "ERROR"

    # Mocking openai.ChatCompletion.create method to raise an exception
    with patch("openai.ChatCompletion.create") as mock_create:
        mock_create.side_effect = Exception("Some error")

        # Mocking the file read
        with patch("builtins.open", MagicMock(return_value=MagicMock(read=MagicMock(return_value="")))):

            result = chatgpt_service.classify(file_path)

    assert result == expected_response
    mock_create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=chatgpt_service.messages
    )