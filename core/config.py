#!/usr/bin/env python		
#coding:utf-8
import ConfigParser
from data import queue,output,threads_num,paths,webdir_result,portscan_result,exploit_result

'''
解析config.conf的一些变量
'''

class ConfigFileParser:
	def __init__(self):
		pass

	def get_options(self,section,option):
		try:
			cf = ConfigParser.ConfigParser()
			cf.read(paths['CONFIG_PATH'])
			return cf.get(section=section,option=option)
		except:
			message = 'Missing essential options'
			output.error(message)

	def scanports(self):
		temp = self.get_options('port','scanports')
		return self.str_to_list(temp)

	def str_to_list(self,s):
		s = s.strip('{}\n').split(',')
		t = list()
		for i in s:
			x = tuple(i.split(':'))
			t.append(x)
		return t

	def webdir_mode(self):
		mode = self.get_options('webdir_mode','mode')
		return mode

	def threads_num(self):
		return self.get_options('threads_num','num')


if __name__ == '__main__':
	paths = {}
	paths['CONFIG_PATH'] = '/home/sublime/python/thread/tmgscanner/config.conf'
	cf  = ConfigFileParser(paths)
	print cf.scanports()

