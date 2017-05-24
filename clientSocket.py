#!/usr/bin/python

import os
import socket
import json
import datetime

def mk_packet(src, intm, dest, payload):
	packet = {}
	packet["src"] = src
	packet["int"] = intm
	packet["dest"] = dest
	packet["time"] = datetime.datetime.now()
	packet["payload"] = payload
	return json.dumps(packet)

def send_packet(packet)
	client = socket.socket()
	c.connect((packet["dest"], port))
	c.send(mk_packet(packet))


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

def 

def main():







