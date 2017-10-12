#!/usr/bin/env python		
#coding:utf-8

import socket
import urlparse
from core.config import output

infolist = [
	('.cn.com', 'whois.centralnic.net', None),
	('.uk.net', 'whois.centralnic.net', None),
	('.uk.com', 'whois.centralnic.net', None),
	('.net', 'whois.verisign-grs.com', 'VERISIGN'),
	('.com', 'whois.verisign-grs.com', 'VERISIGN'),
	('.org', 'whois.pir.org', None),
	('.edu', 'whois.educause.edu', None),
	('.gov', 'whois.dotgov.gov', None),	
	('.kr', 'whois.kr', None),
	('.cn', 'whois.cnnic.cn', None),
	('.jp', 'whois.jprs.jp', None),
	('.edu.cn', 'whois.edu.cn', None),
	('.club', 'whois.club', None),
	('.me', 'whois.nic.me', None),
	('.name', 'whois.nic.name', None),
	('.cc', 'ccwhois.verisign-grs.com', 'VERISIGN'),
]


def whois_request(domain,server,port=43):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((server,port)) #连接whois服务器
	sock.send(("%s\r\n" % domain).encode('utf-8')) #发送domain信息
	buff = b""
	while True:
		data = sock.recv(1024)
		if len(data) == 0:
			break 
		buff += data 

	output.dataOut(buff.decode("utf-8")) 

#print whois_request("baidu.com","whois.verisign-grs.com")

def whois(domain):
	domain = fixdomain(domain)
	r = domain.rindex('.')
	netaddr = domain[r:] #分离出后缀
	for data in infolist:
		if data[0] == netaddr:
			return whois_request(domain,data[1])

	return ""


def fixdomain(domain):
	tt = urlparse.urlparse(domain)
	new_domain = tt.netloc+tt.path
	if 'www' in new_domain:
		new_domain = new_domain[4:]
	#print new_domain
	return new_domain

if __name__ == '__main__':
	print whois('www.blogsir.com.cn')
