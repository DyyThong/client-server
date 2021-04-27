import socket
localIP = "169.254.39.134"
TCP_Port = 8000
UDP_Port = 5000
bufferSize = 1024
msfFromServer = "Hello UDP Client"

#create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
TCPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#Bind to address and ip
UDPServerSocket.bind((localIP, UDP_Port)) #udp protocol de gui du lieu
TCPServerSocket.bind((localIP, TCP_Port)) #socket nhan dang ky
TCPServerSocket.listen(5)
list_port = [1999,2000,2001,2002,2003] # port nhan du lieu gui ve cho client
#listen for incoming datagrams
i = 0
while(True):
        print("server up and listening")
        clienConnection,clientAddr =  TCPServerSocket.accept() 
        print("connected to "+ clientAddr[0]+" " + str(clientAddr[1]))
        conten1 = clienConnection.recv(1024).decode()
        conten1 = int(conten1)#udp port cua lient
        address = (clientAddr[0],conten1)
        print(address)
        port = str(list_port[i])
        port_ = list_port[i]
        i = i + 1

        if i > 4 :
                i = 0
        
        new_Tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0) #socket nhan du lieu
        new_Tcpsocket.bind((localIP,port_))
        print("new tcp server up and listening")
        UDPServerSocket.sendto(port.encode(), address)
        new_Tcpsocket.listen(1)
        connection, address = new_Tcpsocket.accept()
        content2 = connection.recv(1024).decode()
        print(content2)
        new_Tcpsocket.close()
UDPServerSocket.close()
TCPServerSocket.close()       


