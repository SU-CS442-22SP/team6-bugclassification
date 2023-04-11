import openai
from server.bugclassification_base import BugClassificationBase
from server.config import settings

openai.api_key = settings.CHATGPT_KEY


class ChatGPTService(BugClassificationBase):
    def __init__(self):
        self.messages = self._start_chat()

    def _start_chat(self):
        messages = [{"role": "user", "content": settings.CHATGPT_START_MESSAGE}]
        return messages

    def classify(self, buggged_code):
        self.messages.append({"role": "user", "content": buggged_code})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        return chat.choices[0].message.content
