import socket

IP_ADDRESS = "192.168.0.103"
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))
client_socket.send(b"Hello from the client!")
response = client_socket.recv(1024)
print(response.decode("utf-8"))
client_socket.close()
