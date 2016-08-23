import socket
import sys
import message
import keys
import pickle

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5003 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    data = conn.recv(1024)
    public_key = pickle.loads(data)
    reply = 'OK'
    print public_key
    if not public_key:
        break
     
    conn.sendall(reply)

    data = conn.recv(1024)
    msg = pickle.loads(data)

    print(msg)

    print(message.decrypt(public_key, msg))

conn.close()
s.close()