#! /usr/bin python
# -*- coding: utf-8 -*-

import socket

hosts = ['127.0.0.1', 'localhost']
ports = [20, 22, 80, 443, 3389]

for host in hosts:
	for port in ports:
	#for port in range(20, 443, 2):
		try:
			s = socket.socket()
			print "[+] Connecting to  "+host+":"+str(port)
			s.connect((host, port))
			s.send('Primal Security \n')		
			banner = s.recv(1024)
			if banner:
				print "[+] Port "+str(port)+" open: "+banner
			s.close()
		except:
			pass
