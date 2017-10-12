#!/usr/bin/env python		
#coding:utf-8
import multiprocessing
import time
from core.data import data

def speed(func,url):
    result = []
    start = time.time()
    flag = 200
    payloads = list()
    pools = []
    for i in data:
        payloads.append(i)
        
    for i in range(0,len(payloads),flag):
        group_data = payloads[i:i+flag]
        #print len(group_data)
        #print group_data
        p = multiprocessing.Process(target=func,args=(url,group_data,10))
        pools.append(p)
        p.daemon = True
        p.start()
    for p in pools:
        p.join()
    print('[*] The DirScan is complete!')
    print 'use time:',time.time()-start