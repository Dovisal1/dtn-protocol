#!/usr/bin/python

import os
import socket
import json
import datetime
import time

rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])

def mk_packet(src, intm, dest, seq, payload):
	packet = {}
	packet["src"] = src
	packet["int"] = intm
	packet["dest"] = dest
	packet["time"] = datetime.datetime.now()
	packet["seq"] = 
	packet["payload"] = payload
	return json.dumps(packet)

def send_packet(src, intm, dest, seq, payload, c = None)
	if not c:
		c = socket.socket()
	c.connect((dest, port))
	c.send(mk_packet(src, intm, dest, seq, payload))


def ping(host):
	status = os.system("ping -c3 -t1 " + host)
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

def main(dest):
	seq = 1
	c = socket.socket()
	while True:
		handle_req(socket.gethostname(), INTMS, DEST, seq, rand_str(1024))
		seq += 1
		time.sleep(2)









