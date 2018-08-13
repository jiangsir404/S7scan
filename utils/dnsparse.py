#!/usr/bin/env python		
#coding:utf-8

import urlparse

file = "/mnt/hgfs/F/sublime/src/项目1/url2.dic"

with open(file) as f:
	for i in f:
		print i.strip()
		url = urlparse.urlparse(i.strip())
		print url