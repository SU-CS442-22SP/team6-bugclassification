from unittest.mock import patch
from services.chatgpt import ChatGPTService
from config import settings


def test_init():
    service = ChatGPTService()
    assert len(service.messages) == 1
    assert service.messages[0]["role"] == "system"
    assert (
        service.messages[0]["content"]
        == settings.CHATGPT_START_MESSAGE + "\n" + settings.BUGS_LIST
    )


@patch("openai.ChatCompletion.create")
def test_classify(mock_chatcompletion_create):
    buggged_code = "def add(a, b): return a - b"
    expected_classification = "You have an arithmetic error."

    mock_chatcompletion_create.return_value = {
        "choices": [{"message": {"content": expected_classification}}],
    }

    service = ChatGPTService()
    classification = service.classify(buggged_code)

    assert classification == expected_classification
    assert len(service.messages) == 2
    assert service.messages[-1]["role"] == "user"
    assert service.messages[-1]["content"] == buggged_code

    mock_chatcompletion_create.assert_called_once_with(
        model="gpt-3.5-turbo", messages=service.messages
    )
