#!/usr/bin/python

#Server Socket
import socket
#import clientSocket.py


#server is listening
def initializeServer(port):
	s = socket.socket();
	#socket.setblocking(0);
	hostname = socket.gethostname();
	s.bind((hostname,port));
	s.listen(5);
	while True :
		c, addr = s.accept();
		print 'Got connection from ' , addr;


def main():

	print "Waiting For Client";
	hostname = initializeServer(8080);
	packetReceived = s.recieve(1024);
	print packetReceived;
	if(packetReceived["intm"] == None):
		#mk_packet("", 0, "", "");
		print "Empty packet Recieved";
	else:
		print "delivered";
	print hostname;

if __name__ == "__main__":
	main();



