from services.bugclassification_base import BugClassificationBase
from config import settings
import subprocess
import json
import os


class PMDService(BugClassificationBase):
    def __init__(self, pmd_config_path):
        super().__init__()
        self.COMMAND = f"pmd check -f json -R {pmd_config_path} -d FILE_PATH"
        self.ENV_COMMAND = f"export PATH=$PATH:{settings.PMD_PATH}"

    def classify(self, file_path):
        try:
            command = self.COMMAND.replace("FILE_PATH", file_path)
            response = self.run_command(command)
            response = json.loads(response)
            return response
        except Exception as e:
            print("Error in PMDService: ", e)
            return "ERROR"

    def run_command(self, command):
        try:
            # Set the new PATH value
            new_path = os.environ.get("PATH", "") + ":" + settings.PMD_PATH
            os.environ["PATH"] = new_path
            output = subprocess.check_output(command, shell=True, executable="/bin/bash", env=os.environ)
            return output
        except subprocess.CalledProcessError as e:
            return e.output
