import socket, sys
import variables as gv

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QScrollArea,
)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((gv.IP_ADDRESS, gv.PORT))
    client_socket.send(b"Hello from the client!")
    response = client_socket.recv(1024)
    print(response.decode("utf-8"))
    client_socket.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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


    def _pick_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose', gv.BASE_DIR,"Java files (*.java)")[0]
        if fname != '':
            self.path_label.setText(fname)
            self.remove_button.setEnabled(True)
            self.classify_button.setEnabled(True)


    def _remove_picked_file(self):
        self.path_label.setText("None selected")
        self.remove_button.setDisabled(True)
        self.classify_button.setDisabled(True)


    def _send_to_server(self):
        pass


    def print_result(self, result):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()