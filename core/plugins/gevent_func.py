#!/usr/bin/env python        
#coding:utf-8

import os
import sys
import Queue
import time
import requests
import download
import gevent
from core.console import getTerminalSize
from core.config import output
from core.data import webdir_result,thread_mode
from gevent import monkey,pool
monkey.patch_all()


class Gevent_func:
    def __init__(self,root,data,threadNum):
        self.root = root
        self.threadNum = threadNum
        self.downloader = download.Downloader()
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20'
             }
        self.s_list = []
        self.links = []
        # self.total_count = len(data)
        # self.start_time = time.time()
        # sizex, sizey = getTerminalSize()
        # self.width = sizex 
        # self.height = sizey
        for line in data:  
            #print line
            self.links.append(line.strip())
        self.work()
    

    def test_url(self,path):
        path = '/'+self.fixpath(path)
        url = self.root+path
        res = self.downloader.get(url)
        #print url,res
        output.statusReport(path,res)

    
    def work(self):
        start = time.time()
        p = pool.Pool(self.threadNum)
        pools = []
        for link in self.links:
            pools.append(p.spawn(self.test_url,link))
        
        gevent.joinall(pools)
        print('[*] The DirScan is complete!')
        print 'use time:',time.time()-start

    def fixpath(self,path):
        if '%EXT%' in path:
            path = path.replace('%EXT%','php')
        if path.startswith('/'):
            path = path[1:]
        return path

    def printProgress(self):
        msg = '%s total | %s remaining | scanned in %.2f seconds' % (
            self.total_count,self.remaining_count,time.time()-self.start_time)
        out = '\r' + ' ' * (self.width - len(msg)) + msg
        output.inLine(out)

if __name__ == '__main__':
    scan = webdir('http://116.62.63.190:8080/ee00f46afe33f2ff/web6/',50)
    scan.work()
