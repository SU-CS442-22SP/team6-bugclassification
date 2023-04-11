import variables as gv
import base64, requests
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
        self.classify_button.clicked.connect(self._send_to_server)

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
                self._send_to_server(f)
                self.read_content = f.read()
        else:
            self.read_content = ""


    def _remove_picked_file(self):
        self.path_label.setText("None selected")
        self.remove_button.setDisabled(True)
        self.classify_button.setDisabled(True)
        self.print_result("")


    def _send_to_server(self, f):
        files = {'file': f}
        response = requests.post("http://192.168.0.103:8000/infer", files=files)
        self.output = response.content.decode("utf-8")
        self.print_result(self.output.replace("\\n", '\n'))


    def print_result(self, result):
        self.output_label.setText(result)