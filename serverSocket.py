#!/usr/bin/python

#Server Socket
import socket

def _init_:
	s = socket.socket();
	hostname = s.gethostname();
	port = 8080;
	s.bind(hostname,port);
	s.listen(5);
	while True :
		c, addr = s.accept();
		print 'Got connection from ' , addr;
		c.send("ACK");
		c.close();




