#! /usr/bin python
# -*- coding: utf-8 -*-

hosts = ['127.0.0.1']
ports = [22, 445, 80, 443, 3389]

for host in hosts:
	for port in ports:
		try:
			print "[+] Connecting to  "+host+"str(port)"
			s.connect(host, port)
			s.send('Primal Security \n')		
			banner = s.recv(1024)
			if banner:
				print "[+] Port "+str(port)+" open: "+banner
			s.close()
		except:
			pass
