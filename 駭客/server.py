import socket
print("helloworld")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind參數是一個tuple 放主機名，埠號
serverSocket.bind((socket.gethostname(), 1234, ))

serverSocket.listen(5)

conn, addr = serverSocket.accept()
print('connect from', addr)

data = conn.recv(1024)

conn.send(data)

conn.close()

serverSocket.close()