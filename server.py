
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('torecv.jpg','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print (f'Got connection from {addr}')
    print ("Receiving...")
    l = c.recv(1024)
    while (l):
        print ("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    break
print ("Done Receiving")

c.shutdown(socket.SHUT_RDWR)                # Close the connection     
c.close()