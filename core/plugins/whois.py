#!/usr/bin/env python		
#coding:utf-8

"""
whois信息查询
"""

import socket
import urlparse
import sys
import logging

sys.path.append('../../')
#from core.config import output

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


def whois_request(domain, server, port=43):
	"""发送whois请求
	
	:param str domain: 需要查询的主域名(非子域名)
	:param str server: whois服务器
	:param int port: 端口，默认43
	:return: socket响应内容

	Desc: 
		whois查询的原理就是通过请求对应的whois服务器的43端口，获取其响应信息
	"""
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((server,port)) #连接whois服务器
	sock.send(("%s\r\n" % domain).encode('utf-8')) #发送domain信息
	buff = b""
	while True:
		data = sock.recv(1024)
		if len(data) == 0:
			break 
		buff += data 

	return buff.decode("utf-8")


def whois(domain):
	"""whois信息查询
	"""
	whois_info = ""
	domain = fixdomain(domain)
	r = domain.rindex('.')
	netaddr = domain[r:] #分离出后缀
	for data in infolist:
		if data[0] == netaddr:
			logging.info("whois domain:%s" % str(data))
			whois_info =  whois_request(domain,data[1])

	return whois_info


def fixdomain(domain):
	tt = urlparse.urlparse(domain)
	new_domain = tt.netloc+tt.path
	if 'www' in new_domain:
		new_domain = new_domain[4:]
	#print new_domain
	return new_domain

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	print whois('www.blogsir.com.cn')
	print whois_request("blogsir.com.cn","whois.cnnic.cn")
