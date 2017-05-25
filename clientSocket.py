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

class Request:
	def __init__(self, src, intms, seq, dest, payload, client=None):
		self.packet = {
			"src": 		src,
			"dest":		dest,
			"time":		time.time()
			"seq":		seq
			"payload":	payload
		}
		self.dest = dest
		self.intms = intms
		self.c = client

	def packetstr(self):
		return json.dumps(packet)

	def get_intm(self):
		self.intm = None
		if not ping(self.dest):
			for host in self.intms:
				if ping(host):
					self.intm = host
					break
		self.packet["intm"] = self.intm

	def send_packet(self):
		if not self.client:
			self.c = socket.socket()
			self.c.connect((self.dest,PORT))
			self.c.send(self.packetstr())
			self.c.close()
		else:
			self.c.send(self.packetstr())

	def run():
		self.get_intm()
		self.send_packet()



def mk_packet(src, intm, dest, seq, payload):
	packet = {}
	packet["src"] = src
	packet["int"] = intm
	packet["dest"] = dest
	packet["time"] = datetime.datetime.now()
	packet["seq"] = seq
	packet["payload"] = payload
	return json.dumps(packet)

def send_packet(src, intm, dest, seq, payload, c = None)
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
INTMS = ['intermediary']
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
	c = socket.socket()
	c.connect((DEST,PORT))
	src = socket.gethostname()
	while True:
		r = Request(src, INTMS, seq, DEST, rand_str(64), c)
		r.run()
		seq += 1
		log("seq: %d" % seq, debug)
		time.sleep(numpy.random.exponential(2))










