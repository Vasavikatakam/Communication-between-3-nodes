from bluetooth import *
import time

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

#print "dharani"


client_socket.connect(("B4:6D:83:68:D5:F2", 11))

"""txt=raw_input()
while True:
	client_socket.send(txt)
	txt=raw_input()
	if(txt=='-1'):
		break;

print "Finished"

client_socket.close()"""

try:
	select=client_socket.recv(1024)
	print(select)
	if(select=='1'):
		txt=client_socket.recv(1024)
		print(txt)
		print "Data received successfully!!! "	
	
	elif(select=='2'):
		filename=client_socket.recv(1024)
		print('file you received\n')
		print(filename)
		print("\n")	
		fp = open(filename,'w')
		while True:
	    		strng = client_socket.recv(512)
	    		if not strng:
			   break
			fp.write(strng)
		fp.close()
		print "Data received successfully!!"			
	  
except:
	print "Data Received successfully"
        client_socket.close()

	
