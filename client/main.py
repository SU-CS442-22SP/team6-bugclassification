import socket, sys
import variables as gv
from PyQt5.QtWidgets import QApplication
from client import Client


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Client()
    window.show()
    sys.exit(app.exec())