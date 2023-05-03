from services.bugclassification_base import BugClassificationBase
from config import settings
import requests
import json


class InferService(BugClassificationBase):
    def __init__(self):
        self.url = settings.INFER_URL

    def classify(self, buggged_code):
        files = {"file": buggged_code}
        try:
            response = requests.post(self.url, files=files)
            response = json.loads(response.content)
            return response["bug_type"]
        except Exception as e:
            print("Error in InferService: ", e)
            return "ERROR"
