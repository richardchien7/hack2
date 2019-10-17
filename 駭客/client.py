import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((socket.gethostname(), 1234,))

clientSocket.send(b'helloworld')

data = clientSocket.recv(1024)

print("receive:",data)

clientSocket.close()