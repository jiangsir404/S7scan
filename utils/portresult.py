#!/usr/bin/env python		
#coding:utf-8

import json
from pprint import pprint


file = "/mnt/hgfs/F/CTF/pentest/Exploit/S7scan/reports/ports1.json"

with open(file) as f:
	c = f.read()
	content = json.loads(c)
	cc = json.dumps(content)
	#pprint(content)
	ftp_21  = []
	mysql_3306 = []
	mongodb_27017 = []
	web_80 = []
	mssql_1433 = []
	ssh_22 = []
	web_8080 = []
	fastcgi_9000 = []
	telnet_23 = []
	for c in content:
		if '21:ftp' in c:
			ftp_21.append(c[0])
		if '80:web' in c:
			web_80.append(c[0])
		if '8080:web' in c:
			web_8080.append(c[0])
		if '3306:mysql' in c:
			mysql_3306.append(c[0])
		if '22:ssh' in c:
			ssh_22.append(c[0])
		if '1433:mssql' in c:
			mssql_1433.append(c[0])
		if '27017:mongodb' in c:
			mongodb_27017.append(c[0])
		if '23:telnet' in c:
			telnet_23.append(c[0])
		if '9000:fastcgi' in c:
			fastcgi_9000.append(c[0])

	print 'ftp:',ftp_21
	for ip in ftp_21:
		print ip

	print 'mysql:',mysql_3306
	for ip in mysql_3306:
		print ip
	print 'mongodb:',mongodb_27017
	for ip in mongodb_27017:
		print ip
	print 'web:',web_80
	for ip in web_80:
		print ip
	print 'web 8080:',web_8080
	for ip in web_8080:
		print ip	
	print 'mssql:',mssql_1433
	for ip in mssql_1433:
		print ip

	print 'ssh:',ssh_22
	for ip in ssh_22:
		print ip

	print 'telnet:',telnet_23
	for ip in telnet_23:
		print ip