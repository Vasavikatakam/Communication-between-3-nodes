import socket               
import time 
# next create a socket object
server_socket = socket.socket()         
print "Socket successfully created"
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345             
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
server_socket.bind(('', port))        
print "socket binded to %s" %(port)
 
# put the socket into listening mode
server_socket.listen(5)     
print "socket is listening"  

while True:
	client_socket, address = server_socket.accept()
	print "Conencted to - ",address,"\n"
	print "please enter your choice:\n 1 for text\n 2 for textfiles and Multimedia\n" 
	select=raw_input()
	client_socket.send(select)
	if select=='-1':
		break
	elif select=='1':
		print "Please enter the text to be send\n"
		text=raw_input()
		client_socket.send(text)
		print 'Sending data to intermediate node'
	elif select=='2':
		print "Enter any file it can be text,image or video."
		file_name=raw_input()
		client_socket.send(file_name)
		time.sleep(1)
		print 'Sending data to intermediate node'
		img = open(file_name,'r')
		while True:
		    strng = img.readline(512)
		    if not strng:
			break
		    client_socket.send(strng)
		client_socket.send(' ')	
		img.close()
		print "Data sent successfully"

	

	client_socket.close()
	break	
