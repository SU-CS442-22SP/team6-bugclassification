import openai
from services.bugclassification_base import BugClassificationBase
from config import settings

openai.api_key = settings.CHATGPT_KEY


class ChatGPTService(BugClassificationBase):
    def __init__(self):
        super().__init__()
        self.messages = self._start_chat()

    def _start_chat(self):
        messages = [
            {
                "role": "system",
                "content": settings.CHATGPT_START_MESSAGE,
            }
        ]
        return messages

    def classify(self, file_path):
        with open(file_path, "r") as f:
            buggged_code = f.read()
        try:
            self.messages.append({"role": "user", "content": buggged_code})
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=self.messages
            )
            return chat["choices"][0]["message"]["content"]
        except Exception as e:
            return "ERROR"
