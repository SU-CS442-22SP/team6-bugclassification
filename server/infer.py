from server.bugclassification_base import BugClassificationBase
from server.config import settings
import requests


class InferService(BugClassificationBase):
    def __init__(self):
        self.url = settings.INFER_URL

    def classify(self, buggged_code):
        files = {"file": buggged_code}
        response = requests.post(self.url, files=files)
        return response
