#!/usr/bin/env python        
#coding:utf-8

import os
import sys
import Queue
import time
import requests
import multiprocessing
import gevent
from gevent import monkey,pool
monkey.patch_all()

#root = 'http://218.76.35.74:20131/'
root = sys.argv[-1]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    
def checkdir(url):
    try:
        r = requests.head(url,headers=headers,timeout=5)
        status_code = r.status_code
        return status_code
    except:
        status_code = 404
    return status_code

def test_url(path):
    if '%EXT%' in path:
        path = path.replace('%EXT%','php')
    url = root+path
    #print url
    s_code = checkdir(url)
    if s_code != 404:
        print "Testing: %s status:%s"%(path,s_code)

def work(links):
    p = pool.Pool(50)
    pools = []
    for link in links:
        pools.append(p.spawn(test_url,link))
    
    gevent.joinall(pools)



def main():
    filename = '/home/pentest/dirsearch/db/dicc.txt'
    #filename = os.path.join('/home/pytool/Scaner/w8ay/shiyanlouscan7/shiyanlouscan/data', "dir.txt")
    flag = 50
    paths = list()
    pools = []
    with open(filename) as f:
        for i in f:
            paths.append(i.strip())
        #print paths
        for i in range(0,len(paths),flag):
            data = paths[i:i+flag]
            #print len(data)
            p = multiprocessing.Process(target=work,args=(data,))
            pools.append(p)
            p.start()
        for p in pools:
            p.join()

if __name__ == '__main__':
    start = time.time()
    main()
    print 'use time:',time.time()-start
