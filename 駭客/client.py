import socket
from my_protocol import int_to_nbyte, nbyte_to_int

#開啟一個socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#連向伺服器
clientSocket.connect((socket.gethostname(), 1234,))
clientSocket.send(int_to_nbyte(5201314))
# fp = open('client.py', 'rb')
# while True:
#     #一次讀取16bytes
#     data = fp.read(16)
#     if not data:
#         break
#
#     clientSocket.send(data)


#傳送bytes型別的字串
#clientSocket.send(open(filename).read().encode('utf8'))

#接收伺服器端傳來的資料
#data = clientSocket.recv(1024)

#print("receive:",data)

#關閉socket
clientSocket.close()