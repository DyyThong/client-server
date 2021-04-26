import socket

#for tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("", 50000)) 
s.listen(1)

while True: 
    komm, addr = s.accept() 
    data = komm.recv(1024)

s.close()


#for udp
sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sudp.bind(("", 50000)) 
while True: 
    daten, addr = sudp.recvfrom(1024)
    s.sendto(daten, addr)

s.close()