import socket   
import sys            
from bluetooth import *
import time
# Create a socket object
client_socket= socket.socket()         
 
# Define the port on which you want to connect
port = 12345     
 
# connect to the server on local computer
client_socket.connect(('192.168.43.181', port))

while True:
	select=client_socket.recv(1024)
	if select=='-1':
		break;
	if(select=='1'):
		txt=client_socket.recv(512)
		print "data received Successfully"			
		break
	if(select=='2'):
		filename=client_socket.recv(1024)
		print(filename)
		fp = open(filename,'w')
			
		while True:
		    strng = client_socket.recv(512)
		    if not strng:
		        break
		    fp.write(strng)
		    			        
		fp.close()	
		print "Data Received successfully"
		break



print 'Data successfully received via wifi and forwarding it to the destination node via bluetooth'
server_socket=BluetoothSocket( RFCOMM )

server_socket.bind(("", 11))
server_socket.listen(5)

#client_socket, address = server_socket.accept()

   #while True:
	#data = client_socket.recv(1024)
	#print data

#print "Conencted to - ",address,"\n"

try:
	while (1):
		client_socket, address = server_socket.accept()
		if(select=='1'):
			client_socket.send('1')
			client_socket.send(txt)
			print('data sent successfully!!')
			break
		elif(select=='2'):
			client_socket.send('2')
			client_socket.send(filename)				
			time.sleep(1)			
			img = open(filename,'r')
			while True:
		    		strng = img.readline(512)
		    		if not strng:
					break
		    		client_socket.send(strng)
			client_socket.send(' ')
			img.close()
			print('data sent successfully!!')	
			break

except:
	print('data sent successfully!!')
	
	client_socket.close()
	server_socket.close()





