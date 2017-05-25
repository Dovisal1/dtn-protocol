#!/usr/bin/python

#Server Socket
import socket
import thread
import clientSocket.py


#server is listening
def initializeServer(port):
	s = socket.socket()
	#socket.setblocking(0)
	hostname = socket.gethostname()
	s.bind((hostname,port))
	s.listen(5)
	while True :
		c, addr = s.accept()
		spawn_thread(c,addr)

		print 'Got connection from ' , addr

def handle_connection(connection,address):
	thread = threading.Thread(target = handle_req())


def receive_connection(connection,address):
	packet = connection.recv()
	packetDict = json.loads(packet)
	src = packetDict["src"]
	dest = packetDict["dest"]
	seq = packetDict["seq"]
	payload = packetDict["payload"]
	if packetDict["intm"]:
		handle_req(src, [], dest, seq, payload)


def spawn_thread(connection,address):
	thread = threading.Thread(target = receive_connection, args = (connection,address))
	thread.daemon = True
	thread.start()


PORT = 8080

if __name__ == "__main__":
	initializeServer(PORT)



