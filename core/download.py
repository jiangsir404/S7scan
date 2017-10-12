#!/usr/bin/env python		
#coding:utf-8
import requests
import urlparse

class Downloader:
	def __init__(self,timeout=10):
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
		self.timeout = timeout

	def fixurl(self,url):
		if not url:
			return None
		if not url.startswith('http://') and not url.startswith('https://'):
			url = 'http://'+url 
		if not url.endswith('/'):
			url += '/'
		return url

	def get(self,url):
		url = self.fixurl(url)
		try:
			res = requests.get(url,headers=self.headers,timeout=self.timeout)
			return res 
		except:
			return None
		

	def head(self,url):
		url = self.fixurl(url)
		try:
			res = requests.head(url,headers=self.headers,timeout=self.timeout)
			return res 
		except:
			return None

	def post(self,url,data):
		url = self.fixurl(url)
		try:
			res = requests.post(url,data=data,headers=self.headers,timeout=self.timeout)
			return res 
		except:
			return None



if __name__ == '__main__':
	download = Downloader()
	print download.get('http://47.74.147.34:20011//admin.php')