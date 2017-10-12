#!/usr/bin/env python		
#coding:utf-8

import nmap 
from pprint import pprint


netadr = '211.82.99.0/31'
def fileScanport():
	nm = nmap.PortScanner()
	info = nm.scan(hosts=netadr,arguments='-p 1-1000')
	nmap_info = info['nmap']
	command_line = nmap_info['command_line']
	scaninfo = nmap_info['scaninfo']
	scan = info['scan']
	# output.dataOut('[*] commond: %s'%command_line) 
	# output.dataOut('[*] scaninfo:'+str(scaninfo)+'\n') 
	print command_line,scaninfo 
	pprint(scan) 

fileScanport()