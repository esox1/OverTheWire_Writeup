import socket
import sys

#create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#then we bind() which is used to associate the socket with the server address, in this cas e the address is localhost and the port number is 30002
#Bind socket to port

server_address = ('localhost', 30002)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#after connection established lets try to send data
try:
   for i in range(0000,9999)
       print ("UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ "+ i)

