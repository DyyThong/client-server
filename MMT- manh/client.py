import socket
import time
server_addr = "169.254.39.134"
server_port = 8000

udp_port = 7000
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind((server_addr,udp_port))

import time
unit_id = -1
#lay du lieu tu computer 
def data_computer():
    data_1 = "hello 0"
    data_2 = "hello 1"
    return data_1,data_2

def client_send():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    tcp_socket.connect((server_addr,server_port))
    data_id = str(unit_id)
    data_port = str(udp_port)
    data_list = [data_id,data_port]
    data_list = str(data_list)
    tcp_socket.send(data_list.encode())
    tcp_socket.close()

    data_, address_ = udp_socket.recvfrom(4096)
    data_ = data_.decode()
    print(data_)
    data_ = eval(data_)
    print(data_[0] + " " + data_[1]+" " + data_[2])
    udp_socket.close()
    server_port_ = int(data_[1])
    time_delay = int(data_[2])
    while True:
        data_1,data_2 = data_computer()
        data_list_2 = [str(data_[0]),str(data_1),str(data_2)]
        data_2 = str(data_list_2)
        tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        tcp_socket.connect((server_addr,server_port_))
        tcp_socket.send(data_2.encode())
        tcp_socket.close()
        time.sleep(time_delay)
        






if(__name__ == "__main__"):
    client_send()
