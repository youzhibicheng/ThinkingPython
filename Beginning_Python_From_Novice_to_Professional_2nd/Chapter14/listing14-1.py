import socket

# a tiny server
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

#     |      listen(backlog)
#     |
#     |      Enable a server to accept connections.  The backlog argument must be at
#     |      least 0 (if it is lower, it is set to 0); it specifies the number of
#     |      unaccepted connections that the system will allow before refusing new
s.listen(5)

while True:
	# accept() -- accept a connection, returning new socket and client address
	# c is a socket
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    c.close()