import socket



SERVER_ADDRESS = "169.254.39.134"

tcpPORT = 8000


udpPORT = 7000
udp_soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_soc.bind((SERVER_ADDRESS,7000))

def createClient():
    tcp_soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    tcp_soc.connect((SERVER_ADDRESS,tcpPORT))
    udp_port_ = str(udpPORT)
    tcp_soc.send(udp_port_.encode())
    tcp_soc.close()   
    content1 = udp_soc.recvfrom(1024)
    print(content1)
    port_new = int(content1[0])
    new_tcpSoc = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    new_tcpSoc.connect((SERVER_ADDRESS,port_new))
    content2 = "client say hello server"
    new_tcpSoc.send(content2.encode())
    new_tcpSoc.close()

if(__name__ == "__main__"):
    createClient()