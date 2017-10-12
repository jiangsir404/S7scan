#!/usr/bin/env python		
#coding:utf-8

import nmap
from pprint import pprint
from core.config import output

class Subnet:
	def __init__(self,mask):
		self.mask = self.MaskFix(mask)
		self.run()

	def run(self):
		nm = nmap.PortScanner()
		info = nm.scan(hosts=self.mask,arguments="-sP")
		#pprint(info)
		nmap_info = info['nmap']
		command_line = nmap_info['command_line']

		scan = info['scan']
		output.dataOut('[*] commond: %s'%command_line) 
		for ip in scan:
			hoststate = scan[ip]['status']['state']
			mes = "%s is up"%ip
			output.dataOut(mes)
		


	def MaskFix(self,Mask):
		if 'http://' in Mask or 'https://' in Mask:
			Mask = Mask.replace('http://','').replace('https://','')
		
		if '/' in Mask:
			return Mask 
		else:
			return Mask+'/24'

if __name__ == '__main__':
	Subnet('211.82.99.1/24')