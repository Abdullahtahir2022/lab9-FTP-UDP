import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


list1 = []
udp_host = socket.gethostname()
udp_port = 12345
FORMAT = "utf-8"			       
print ("UDP target IP:", udp_host)
print ("UDP target Port:", udp_port)

def get_list():
    sock.sendto("0X0000".encode(FORMAT),(udp_host,udp_port))
    msg1 = sock.recvfrom(1024)
    msg2 = sock.recvfrom(1024)
    msg3 = sock.recvfrom(1024)
    print(msg1[0].decode(FORMAT))
    print("Number of files: ",msg2[0].decode(FORMAT))
    print("Files Names",msg3[0].decode(FORMAT))

def download_file():
    String = input("Enter  file name: ")
    sock.sendto("0X0001".encode(FORMAT),(udp_host,udp_port))
    sock.sendto(String.encode(FORMAT),(udp_host,udp_port))
    packet_offset = sock.recvfrom(1024)
    File_name =   sock.recvfrom(1024)
    File_bytes =  sock.recvfrom(1024)
    count = int((int(File_bytes[0].decode(FORMAT))/100)+1)
    list = download_file2(count)
    file = open("Client_download/"+File_name[0].decode(FORMAT),"w")
    for element in list: 
        data = file.write(element+"\n")

def download_file2(count):
    for items in range(count):
        packet_offset = sock.recvfrom(1024)
        SYN = sock.recvfrom(1024)
        data = sock.recvfrom(1024)
        list1.append(data[0].decode(FORMAT))
    return list1

value = int(input("Enter 1 to get files_list or 2 to Download an individual file: "))
if value == 1:
    get_list()
else:
    download_file()

