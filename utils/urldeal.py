#!/usr/bin/env python		
#coding:utf-8

import urlparse
import socket


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f')
parser.add_argument('-o')
arg = parser.parse_args()
#print arg

file = arg.f
output = arg.o

# file = "/mnt/hgfs/F/sublime/src/项目1/url2.dic"

def host_to_ip(url):
	try:
		ip = socket.gethostbyname(url)
		return ip
	except:
		print 'error'

def dnsoutput(url):
	if len(url.split('.')) == 2:
		return url
	return url.strip('www.')



with open(file) as f:
	for i in f:
		i = i.strip()
		if not i.startswith('http://') and not i.startswith('https://'):
			i = 'http://'+i 

		#print i
		url = urlparse.urlparse(i)
		#print url
		if output == 'ip':
			print host_to_ip(url.netloc)
		if output == 'url':
			print url.scheme + '://' + url.netloc
		if output == 'dns':
			print dnsoutput(url.netloc)


		