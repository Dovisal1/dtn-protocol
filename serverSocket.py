#!/usr/bin/python

#Server Socket
import socket

def initialize(port):
	s = socket.socket();
	hostname = s.gethostname();
	s.bind(hostname,port);
	s.listen(5);
	while True :
		c, addr = s.accept();
		print 'Got connection from ' , addr;
		c.send("ACK");
		c.close();
	return hostname;
