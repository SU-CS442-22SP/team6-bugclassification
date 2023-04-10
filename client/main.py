import socket, sys
import variables as gv
from PyQt5.QtWidgets import QApplication
from .client import Client


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((gv.IP_ADDRESS, gv.PORT))
    client_socket.send(b"Hello from the client!")
    response = client_socket.recv(1024)
    print(response.decode("utf-8"))
    client_socket.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Client()
    window.show()
    sys.exit(app.exec())