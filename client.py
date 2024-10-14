import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                 # Reserve a port for your service.

s.connect((host, port))

f = open('tosend.jpg','rb')
print ('Sending...')
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
s.send(l)
f.close()
print ("Done Sending")

s.shutdown(socket.SHUT_RDWR)
s.close()
