#!/usr/bin/python

import os
import socket
import threading
import clientSocket
import logging
import json
import time

serverlog = os.path.join(os.path.expanduser("~"), "server.log")
FORMAT = '[%(levelname)s] (%(threadName)-10s) %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

file_handler = logging.FileHandler(serverlog)
file_handler.setFormatter(logging.Formatter(FORMAT))
logging.getLogger().addHandler(file_handler)

#server is listening
def initializeServer(server, port):
	server.bind(('localhost',port))
	logging.info('connected on %d' % port)
	server.listen(5)
	while True:
		logging.info('waiting...')
		conn, addr = server.accept()
		logging.info('connection recv')
		conn.settimeout(60)
		threading.Thread(target=receive_connection, args=(conn, addr)).start()


def receive_connection(conn, addr):
	packet = conn.recv(2048)
	logging.info(packet)
	packet_dict = json.loads(packet)
	src = packet_dict["src"]
	intm = packet_dict["intm"]
	dest = packet_dict["dest"]
	seq = packet_dict["seq"]
	payload = packet_dict["payload"]

	if packet_dict["intm"]:
		intms = clientSocket.INTMS
		intms.remove(intm)
		with clientSocket.Client(src, intms, seq, dest, payload) as c:
			c.run()

	conn.close()


PORT = 3333

if __name__ == "__main__":
	try:
		server = socket.socket()
		initializeServer(server, PORT)
	except KeyboardInterrupt:
		server.close()