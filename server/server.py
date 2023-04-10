import socket

IP_ADDRESS = "0.0.0.0"
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, PORT))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")
    client_socket.send(b"Welcome to the server!")
    client_socket.close()
