import socket
server_addr = socket.gethostname()
tcp_port = 8000
udp_port = 5000

time_delay = int(input("pls choose time delay: "))

tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

#bind

tcp_socket.bind((server_addr,tcp_port))
tcp_socket.listen(5)

#handle data
def handl_data(content):

    #print("unit ID: " + str(content[0]) +"\n"+ "Disk Usage: " + content[1] + "\n" + "RAM Usage:" + content[2] + "\n" + "Battery: " + content[3] + "\n" + "Power Plugged: " + content[4])
    print("Time: " + content[12])
    print("MEMORY")
    print("------")
    print("Total: " + content[1] + "|" + "Available: " + content[2] + "|" + "Percent: " + content[3] + "|" + "Used: " + content[4] + "|" + "Free: " + content[5])
    print("------")
    print("DISK")
    print("Total: " + content[6] + "|" + "Used: " + content[7] + "|" + "Free: " + content[8] + "|" + "Percent: " + content[9])
    print("------")
    print("BATTERY")
    print("Percent: " + content[10] + "|" + "Power Plugged: " + content[11])
    print("------")

    print("end")
    print("\n")
def udp_send_data(client_addr,client_port,unit_id):
    print("call")
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind((server_addr,udp_port))
    ID = str(unit_id)
    port_data = str(tcp_port)
    time_delay_ = str(time_delay)
    list_data = [ID, port_data, time_delay_]
    list_data = str(list_data)
    udp_socket.sendto(list_data.encode(),(client_addr,client_port))
    udp_socket.close()
    
    

    


def connect_():
    unit_id = 0
    while True:
        conn,addr = tcp_socket.accept()
        print("connected to " + addr[0] + " " + str(addr[1]))
        content = conn.recv(4096).decode()
        content = eval(content)
        content[0] = int(content[0])
        if content[0] == -1:
            content[1] = int(content[1])
            udp_send_data(addr[0], content[1],unit_id)
            unit_id = unit_id + 1
        else:
            handl_data(content)
        conn.close()

if(__name__ == "__main__"):
    connect_()