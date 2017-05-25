#!/usr/bin/python

import os
import socket
import thread
import threading
import clientSocket
import json


serverlog = os.path.join(os.path.expanduser("~"), "server.log")
logfile = open(serverlog, 'a')
debug = True

def log(msg,debug=True):
	logfile.write(msg)
	if debug:
		print(msg)

#server is listening
def initializeServer(port):
	server = socket.socket()
	#socket.setblocking(0)
	server.bind(('',port))
	server.listen(5)
	while True:
		c, addr = server.accept()
		spawn_thread(c, addr)


def receive_connection(conn, addr):
	packet = conn.recv(2048)
	packet_dict = json.loads(packet)
	src = packet_dict["src"]
	intm = packet_dict["intm"]
	dest = packet_dict["dest"]
	seq = packet_dict["seq"]
	payload = packet_dict["payload"]

	log(packet + "\n", debug)

	if packet_dict["intm"]:
		intms = clientSocket.INTMS
		intms.remove(intm)
		with clientSocket.Client(src, intms, seq, dest, payload) as c:
			c.run()

	conn.close()


def spawn_thread(conn, addr):
	thread = threading.Thread(target=receive_connection, args=(conn, addr))
	thread.daemon = True
	thread.start()


PORT = 8080

if __name__ == "__main__":
	initializeServer(PORT)



