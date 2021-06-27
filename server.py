import socket
import json
import os
import textwrap

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()		        
udp_port = 12345
FORMAT = "utf-8"			        
sock.bind((udp_host,udp_port))
arr= []
arr = os.listdir('Server_Files')


def send_list(addr):
	list = json.dumps(arr)
	sock.sendto("0X0010".encode(FORMAT),addr)
	sock.sendto(str(len(arr)).encode(FORMAT),addr)
	sock.sendto(list.encode(FORMAT),addr)

def Chunck_creater(data,x):
	while(True):
		list1 = textwrap.wrap(data, x)
		if(len(list1[0])<97):
			return list1
		x=x-1

def bytes(string,x):
	while(True):
		if(len(string)<x):
			string = "0"+string
		else:
			return string

def  send_specific_file_round2(counter,addr):
	for items in range(counter):
		sock.sendto("0X0012".encode("utf-8"),addr)
		string = bytes(str(items),2)
		sock.sendto(string.encode("utf-8"),addr)
		sock.sendto(list[items].encode("utf-8"),addr)

def send_specific_file_round1(addr):
	file_name = sock.recvfrom(1024)
	f_name = file_name[0].decode(FORMAT)
	if f_name in arr:
		file = open("Server_Files/"+f_name)
		data = file.read()
		data_bytes = len(data.encode("utf-8"))
		global list
		list = Chunck_creater(data,data_bytes)
		count = int((data_bytes/100)+1)
		sock.sendto("0X0011".encode("utf-8"),addr)
		sock.sendto(f_name.encode("utf-8"),addr)
		string = bytes(str(data_bytes),4)
		sock.sendto(string.encode("utf-8"),addr)
		send_specific_file_round2(count,addr)


while True:
	print("UDP server is lisening")
	msg = sock.recvfrom(1024)
	if(msg[0].decode(FORMAT) == "0X0000"):
		send_list(msg[1])
	if(msg[0].decode(FORMAT) == "0X0001"):
		send_specific_file_round1(msg[1])


	


	#sock.sendto("Hello udpie".encode("utf-8"),addr)