import variables as gv
import base64, os, sys, requests
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QScrollArea,
)
from models.chatgpt_response import ChatGPTResponse
from models.infer_response import InferResponse
from models.pmd_response import PMDResponse


import json

def prettify_json(json_str):
    try:
        parsed = json.loads(json_str)
        return json.dumps(parsed, indent=4).replace("\\n", "\n")
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {str(e)}"

sys.path.insert(0, os.path.abspath('..'))

class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bug Classifier")
        self.load_client_ui()

    def load_client_ui(self):
        uic.loadUi(gv.UI_PATH, self)
        self.select_button = self.findChild(QPushButton, "select_file_button")
        self.select_button.clicked.connect(self._pick_file)

        self.remove_button = self.findChild(QPushButton, "deselect_file_button")
        self.remove_button.clicked.connect(self._remove_picked_file)

        self.path_label = self.findChild(QLabel, "file_path_label")

        self.classify_button = self.findChild(QPushButton, "classify_button")
        self.classify_button.clicked.connect(self._classify)

        self.output_scrollarea = self.findChild(QScrollArea, "output_scrollArea")
        # FILL THE SCROLLAREA
        # Initialize content whose parent is scroll_area
        scrollarea_content = QWidget(self.output_scrollarea)
        # Put content in it
        self.output_scrollarea.setWidget(scrollarea_content)
        # Initialize a layout whose parent is the content in the scrollarea
        scroll_area_layout = QVBoxLayout(scrollarea_content)
        # Initialize a label whose parent is the content in the scrollarea
        self.output_label = QLabel(scrollarea_content)
        # Align it
        self.output_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # Allow it to have multiple lines
        self.output_label.setWordWrap(True)
        # Add the label inside the layout
        scroll_area_layout.addWidget(self.output_label)


    def _pick_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Choose', gv.BASE_DIR, "Java files (*.java)")[0]
        if file_path != '':
            self.path_label.setText(file_path)
            self.remove_button.setEnabled(True)
            self.classify_button.setEnabled(True)
            with open(file_path, "r") as f:
                self.read_content = f.read()
        else:
            self.read_content = ""


    def _remove_picked_file(self):
        self.path_label.setText("None selected")
        self.remove_button.setDisabled(True)
        self.classify_button.setDisabled(True)
        self.print_result("")


    def _classify(self):
        response = requests.post("http://45.32.158.114/analyze", files={'file': self.read_content})
        response_dict = response.json()
        infer_response = InferResponse(payload=response_dict)
        pmd_response = PMDResponse(payload=response_dict)
        chatgpt_response = ChatGPTResponse(payload=response_dict)
        self.print_result(f"{pmd_response.title}\n{pmd_response.content}\n\n{infer_response.title}\n{infer_response.content}\n\n{chatgpt_response.title}\n{chatgpt_response.content}")





    def print_result(self, result, append:bool=False):
        if append:
            self.output_label.setText('\n\n\n\n'.join([self.output_label.text(), result]))
        else:
            self.output_label.setText(result)