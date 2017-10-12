#!/usr/bin/env python        
#coding:utf-8

import os
import sys
import Queue
import time
import requests
import threading
import download
from core.console import getTerminalSize
from core.config import output
from core.data import webdir_result,thread_mode


class Thread_func:
    def __init__(self,root,data,threadNum):
        self.root = root
        if not self.root:
            print 'not url'
        self.threadNum = threadNum
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        self.task = Queue.Queue()
        self.s_list = []
        self.downloader = download.Downloader()
        self.total_count = len(data)
        self.start_time = time.time()
        sizex, sizey = getTerminalSize()
        self.width = sizex 
        self.height = sizey
        for line in data:  
            #print line
            self.task.put(line.strip())
        self.remaining_count = self.task.qsize()
        self.work()

    def test_url(self):
        while True:
            try:
                path = '/'+self.fixpath(self.task.get(False))
                url = self.root+path
                res = self.downloader.get(url)
                #print url,res.status_code
                if res:
                    message = '[{0}] {1} - {2} - {3}'.format(
                        time.strftime('%H:%M:%S'),
                        res.status_code,
                        str(len(res.content)).rjust(6, ' '),
                        path
                    )
                    output.statusReport(path,res)
                    webdir_result.append(message)

                self.remaining_count = self.task.qsize()
                #print thread_mode
                if thread_mode == '0': #只是在多线程模式下才打印进度栏
                    if self.remaining_count:
                        self.printProgress()
            except Exception,e:
                self.remaining_count = self.task.qsize()
                break
    
    def work(self):
        threads = []
        for i in range(self.threadNum):
            t = threading.Thread(target=self.test_url)
            threads.append(t)
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join()

    def fixpath(self,path):
        if '%EXT%' in path:
            path = path.replace('%EXT%','php')
        if path.startswith('/'):  # path前统一不加/
            path = path[1:]
        return path

    def printProgress(self):
        msg = '%s total | %s remaining | scanned in %.2f seconds' % (
            self.total_count,self.remaining_count,time.time()-self.start_time)
        out = '\r' + ' ' * (self.width - len(msg)) + msg
        output.inLine(out)


if __name__ == '__main__':
    data = ['/','admin.php','index.php','index2.php']
    Thread_Func('http://218.76.35.74:20131/',data,10)
    #scan = webdir('http://218.76.35.74:20131/',50)

