from bugclassification_base import BugClassificationBase
from config import settings
import requests


class InferService(BugClassificationBase):
    def _init_(self):
        self.url = settings.INFER_URL

    def classify(self, buggged_code):
        files = {"file": buggged_code}
        response = requests.post(self.url, files=files)
        return response