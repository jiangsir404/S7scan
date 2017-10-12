#!/usr/bin/env python        
#coding:utf-8

import os
import sys
import Queue
import time
import requests
import threading
import multiprocessing


root = 'http://web.jarvisoj.com:32798/'
headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
     'Referer': 'http://www.shiyanlou.com',
     'Cookie': 'whoami=w8ay',
     }
s_list = []
task = multiprocessing.Queue()
mgr = multiprocessing.Manager()
data = mgr.list()
#filename = os.path.join('/home/pytool/Scaner/w8ay/shiyanlouscan7/shiyanlouscan/data', "dir.txt")
filename = '/home/pytool/dirsearch-master/db/dicc.txt'
for line in open(filename):  
    data.append(line.strip())

def checkdir(url):
    status_code = 0
    try:
        r = requests.head(url,headers=headers,timeout=3)
        status_code = r.status_code
        return status_code
    except:
        status_code = 404
    return status_code

def test_url(path):
    #print threading.currentThread().name
    #print os.getpid()
    if '%EXT%' in path:
        path = path.replace('%EXT%','php')
    url = root+path
    #print url
    s_code = checkdir(url)
    if s_code != 404:
        s_list.append(url)
        print "Testing: %s status:%s"%(path,s_code)


def work():
    start = time.time()
    p = multiprocessing.Pool(50)
    p.map_async(test_url,data)
    p.close()
    p.join()
    print('All subprocesses done.')

    print('[*] The DirScan is complete!')
    print 'use time:',time.time()-start

def output():
    if len(s_list):
        print "[*] status = 200 dir:"
        for url in s_list:
            print url



if __name__ == '__main__':
    work()
    output()