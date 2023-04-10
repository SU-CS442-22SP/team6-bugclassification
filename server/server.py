import socket
import variables as gv


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((gv.IP_ADDRESS, gv.PORT))
    server_socket.listen()
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established!")
        client_socket.send(b"Welcome to the server!")
        client_socket.close()


if __name__ == "__main__":
    main()
