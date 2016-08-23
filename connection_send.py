import socket   #for sockets
import sys  #for exit
import encryptor
import keys
import pickle

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'localhost'
port = 5003
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
#Send some data to remote server
p = keys.generateLargePrime(10)
#q = int(raw_input("Enter another prime number (Not one you entered above): "))
q = keys.generateLargePrime(10)
print "Generating your public/private keypairs now . . ."
public, private = encryptor.generate_keypair(p, q)
print "Your public key is ", public ," and your private key is ", private

message = "Hej med dig"

encrypted_msg = encryptor.encrypt(private, message)
print(encrypted_msg)
try :
    #Set the whole string
    s.sendall(pickle.dumps(public))

    s.sendall(''.join(map(lambda x: str(x), pickle.dumps(encrypted_msg))))
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()


print 'Message send successfully'