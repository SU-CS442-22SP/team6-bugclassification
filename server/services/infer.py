from services.bugclassification_base import BugClassificationBase
import subprocess
import os


class InferService(BugClassificationBase):
    def __init__(self):
        super().__init__()
        self.COMMAND = "infer run --results-dir inferlogs -- javac FILE_PATH"

    def classify(self, file_path):
        try:
            command = self.COMMAND.replace("FILE_PATH", file_path)
            response = self.run_command(command)
            return response
        except Exception as e:
            print("Error in PMDService: ", e)
            return "ERROR"

    def run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, executable="/bin/bash", env=os.environ)
            return output
        except subprocess.CalledProcessError as e:
            return e.output
