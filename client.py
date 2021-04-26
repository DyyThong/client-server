import socket

hostname = 'localhost'

##Send by TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to an IP address with Port
client.connect((hostname, 50000))
#Send data
client.send() #Hien thuc lay data tu PC

## Get from UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Receive up to 4096 bytes from peer
from_server = sock.recv(4096)
#Close the socket connection, no more data transmission
response, serverAddress = sock.recv(1024)

s.close()