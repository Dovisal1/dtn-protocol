#!/usr/bin/python

import os
import socket
import json
import time
import numpy
import random
import string
import logging

clientlog = os.path.join(os.path.expanduser("~"), "client.log")
FORMAT = '[%(levelname)s] (%(threadName)-10s) %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

file_handler = logging.FileHandler(clientlog)
file_handler.setFormatter(logging.Formatter(FORMAT))
logging.getLogger().addHandler(file_handler)

rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])

class Client:
	def __init__(self, src, intm, seq, dest, payload):
		self.packet = {
			"src": 		src,
			"dest":		dest,
			"time":		time.time(),
			"seq":		seq,
			"payload":	payload
		}
		self.dest = dest
		self.intm = intm
		self.client = None

	def __enter__(self):
		return self

	def packetstr(self):
		return json.dumps(self.packet)

	def establish_conn(self):
		self.client = socket.socket()

		self.client.settimeout(2)

		try:
			self.client.connect((self.dest, PORT))
			self.intm = None
		except socket.error:
			try:
				self.client.connect((self.intm, PORT))
			except:
				self.client.close()
				self.client = None
		finally:
			self.packet["intm"] = self.intm


	def send_packet(self):
		self.client.send(self.packetstr())

	def run(self):
		self.establish_conn()
		if self.client:
			self.send_packet()
			self.client.shutdown(1)

	def __exit__(self, exc_type, exc_value, traceback):
		if self.client:
			self.client.close()



def mk_packet(src, intm, dest, seq, payload):
	packet = {}
	packet["src"] = src
	packet["int"] = intm
	packet["dest"] = dest
	packet["time"] = datetime.datetime.now()
	packet["seq"] = seq
	packet["payload"] = payload
	return json.dumps(packet)

def send_packet(src, intm, dest, seq, payload, c = None):
	if not c:
		c = socket.socket()
	c.connect((dest, port))
	c.send(mk_packet(src, intm, dest, seq, payload))


def ping(host):
	status = os.system("ping -c1 -w1 " + host)
	return status == 0

def mk_path(dest, intms):
	path = [dest]
	if not ping(dest):
		for host in intms:
			if ping(host):
				path.append(host)
				break
	return path

def handle_req(src, intms, dest, seq, payload):
	path = mk_path(dest, intms)
	if len(path) == 1:
		send_packet(src, None, dest, seq, payload)
	else:
		intm = path[1]
		send_packet(src, intm, dest, seq, payload)

DEST = 'localhost'
INTM = 'intermediary'
PORT = 3333

def main(dest):
	seq = 1
	src = socket.gethostname()
	while True:
		with Client(src, INTM, seq, DEST, rand_str(64)) as c:
			c.run()
		logging.info("seq: %d" % seq)
		seq += 1
		time.sleep(numpy.random.exponential(0.08))


if __name__ == "__main__":
	main(DEST)