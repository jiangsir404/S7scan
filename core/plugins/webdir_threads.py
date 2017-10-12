#!/usr/bin/env python        
#coding:utf-8

import os
import sys
import Queue
import time
import requests
import threading
import colorprinter
from core.config import output


class webdir:
    def __init__(self,root,threadNum):
        self.root = root
        self.threadNum = threadNum
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        self.task = Queue.Queue()
        self.s_list = []
        #filename = os.path.join('/home/pytool/Scaner/w8ay/shiyanlouscan7/shiyanlouscan/data', "dir.txt")
        filename = '/home/pentest/dirsearch/db/dicc.txt'
        for line in open(filename):  
            self.task.put(line.strip())

        self.work()

    
    def checkdir(self,url):
        status_code = 0
        try:
            r = requests.get(url,headers=self.headers,timeout=10)
            return r
        except Exception,e:
            #print e
            pass

    def test_url(self):
        while True:
            try:
                path = self.task.get(False)
                if '%EXT%' in path:
                    path = path.replace('%EXT%','php')
                url = self.root+path
                #print url
                res = self.checkdir(url)
                output.statusReport(path,res)

            except Exception,e:
                break
                #print e
                
    
    def work(self):
        start = time.time()
        threads = []
        for i in range(self.threadNum):
            t = threading.Thread(target=self.test_url)
            #t = multiprocessing.Process(target=self.test_url)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()


    def output(self,status,path):
        if status in [200]:
            colorprint.print_green_text('[x]Status: '+str(status)+' - - '+path+'\n')
        if status in [400,403]:
            colorprint.print_blue_text('[x]Status: '+str(status)+' - - '+path+'\n')
        if status in [301,302,307]:
            colorprint.print_cyan_text('[x]Status: '+str(status)+' - - '+path+'\n')



if __name__ == '__main__':
    scan = webdir('http://www.cnblogs.com',50)
    #scan.output()
