#!/usr/bin/python

import os
import socket
import json
import time
import numpy

rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])

clientlog = os.path.join(os.path.expanduser("~"), "client.log")
logfile = open(clientlog, 'a')
debug = True

def log(msg, console=False):
	logfile.write(msg)
	if console:
		print(msg)

def ping(host):
	status = os.system("ping -c1 -w1 " + host)
	return status == 0

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
		self.client = client

	def __enter__(self):
		return self

	def packetstr(self):
		return json.dumps(self.packet)

	def establish_conn(self):
		self.client = socket.socket()

		self.client.settimeout(0.1)

		try:
			self.client.connect((dest, PORT))
			self.intm = None
		except socket.error:
			self.client.connect((self.intm, PORT))
		else:
			raise socket.error
		finally:
			self.packet["intm"] = self.intm


	def send_packet(self):
		self.client.send(self.packetstr())

	def run():
		try:
			self.establish_conn()
			self.send_packet()
		except socket.error:
			# log error, pass for now
			pass		

	def __exit__(self, exc_type, exc_value, traceback):
		self.client.shutdown()
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

DEST = 'server'
INTM = 'intermediary'
PORT = 8080

# def main(dest):
# 	seq = 1
# 	c = socket.socket()
# 	while True:
# 		handle_req(socket.gethostname(), INTMS, DEST, seq, rand_str(1024))
# 		seq += 1
# 		time.sleep(2)

def main(dest):
	seq = 1
	src = socket.gethostname()
	while True:
		with Client(src, INTM, seq, DEST, rand_str(64)) as c:
			c.run()
		seq += 1
		log("seq: %d" % seq, debug)
		time.sleep(numpy.random.exponential(3))


if __name__ == "__main__":
	main(DEST)