#!/usr/bin/python

import socket;
import 

def mk_packet(src, intm, dest, payload):
	packet = {}
	packet["src"] = src
	packet["int"] = intm
	packet["dest"] = dest
	packet["payload"] = payload
	return json.dumps(packet)



def _init_:
	s - socket.socket();
	host = s.hostname();