import socket
import time
import psutil
from psutil._common import bytes2human
server_addr = socket.gethostname()
server_port = 8000

udp_port = 7000
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind((server_addr,udp_port))

import time
unit_id = -1
#lay du lieu tu computer 
def data_computer():
    data_1 = bytes2human(psutil.virtual_memory().total)
    data_2 = bytes2human(psutil.virtual_memory().available)
    data_3 = psutil.virtual_memory().percent
    data_4 = bytes2human(psutil.virtual_memory().used)
    data_5 = bytes2human(psutil.virtual_memory().free)
    data_6 = bytes2human(psutil.disk_usage('/').total)
    data_7 = bytes2human(psutil.disk_usage('/').used)
    data_8 = bytes2human(psutil.disk_usage('/').free)
    data_9 = bytes2human(psutil.disk_usage('/').percent)
    data_10 = psutil.sensors_battery().percent
    data_11 = psutil.sensors_battery().power_plugged
    #data_12 = psutil.sensors_temperatures(fahrenheit=False)
    return data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,data_11

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
    print(data_[0] + " " + data_[1]+ " " + data_[2])
    udp_socket.close()
    server_port_ = int(data_[1])
    time_delay = int(data_[2])
    while True:
        data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,data_11 = data_computer()
        data_list_2 = [str(data_[0]),str(data_1),str(data_2),str(data_3),str(data_4),str(data_5),str(data_6),str(data_7),str(data_8),str(data_9),str(data_10),str(data_11)]
        data_2 = str(data_list_2)
        tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        tcp_socket.connect((server_addr,server_port_))
        tcp_socket.send(data_2.encode())
        tcp_socket.close()
        time.sleep(time_delay)
        






if(__name__ == "__main__"):
    client_send()