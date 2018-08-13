#!/usr/bin/env python		
#coding:utf-8
import os

#  处理sqli注入结果的内容

file = "/mnt/hgfs/F/sublime/src/漏洞盒子/sqli.txt"

dirname = os.path.dirname(file)

wf = open(dirname+'/sqli_new.txt','w')

with open(file) as f:
	for i in f.readlines():
		url = i.split(']')[-1].strip()
		print url
		wf.write(url+"\n")

wf.close()