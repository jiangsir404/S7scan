#!/usr/bin/env python		
#coding:utf-8

import json
from pprint import pprint
import os

file = "/mnt/hgfs/F/sublime/src/bistu/bistu.json"


dirname = os.path.dirname(file)
print dirname
with open(file) as f:
	c = f.read()
	content = json.loads(c)
	cc = json.dumps(content)
	#pprint(content)
	ftp_21  = []
	mysql_3306 = []
	mongodb_27017 = []
	memcache_11211 = []
	redis_6379 = []
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
		if '11211:memcache' in c:
			memcache_11211.append(c[0])
		if '6379:redis' in c:
			redis_6379.append(c[0])


	f = open(dirname+'/ftp.txt','w')
	print 'ftp:',ftp_21
	for ip in ftp_21:
		print ip
		f.write(ip+"\n")
	f.close()

	f = open(dirname+'/mysql.txt','w')
	print 'mysql:',mysql_3306
	for ip in mysql_3306:
		print ip
		f.write(ip+"\n")
	f.close()

	f = open(dirname+'/mongodb.txt','w')
	print 'mongodb:',mongodb_27017
	for ip in mongodb_27017:
		print ip
		f.write(ip+"\n")
	f.close()

	f = open(dirname+'/web80.txt','w')
	print 'web:',web_80
	for ip in web_80:
		print ip
		f.write(ip+"\n")
	f.close()

	f = open(dirname+'/web8080.txt','w')
	print 'web 8080:',web_8080
	for ip in web_8080:
		print ip
		f.write(ip+"\n")

	f.close()

	f = open(dirname+'/mysql.txt','w')
	print 'mssql:',mssql_1433
	for ip in mssql_1433:
		print ip
		f.write(ip+"\n")

	f.close()

	f = open(dirname+'/ssh.txt','w')
	print 'ssh:',ssh_22
	for ip in ssh_22:
		print ip
		f.write(ip+"\n")

	f.close()

	f = open(dirname+'/telnet.txt','w')
	print 'telnet:',telnet_23
	for ip in telnet_23:
		print ip
		f.write(ip+"\n")
	f.close()

	f = open(dirname+'/redis.txt','w')
	print 'redis:',redis_6379
	for ip in redis_6379:
		print ip
		f.write(ip+"\n")
	f.close()

	f = open(dirname+'/memcache.txt','w')
	print 'memcache:',memcache_11211
	for ip in memcache_11211:
		print ip
		f.write(ip+"\n")
	f.close()