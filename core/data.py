#!/usr/bin/env python		
#coding:utf-8

import os
import Queue
from output import CLIOutput
from colorprinter import ColorPrinter,print_random_text

'''
设置一些全局变量, 这样多个文件之间就不需要每次都传过来传过去了
queue:  加载script所需要的url队列
paths: 各种路径
output: 输出类
data: webdir搜需要的payloads数据
threads_num: 扫描线程
webdir_result,portscan_result,exploit_result: 三个plugin的返回结果
banners: logo
'''

def getpath(): # 初始化加载全局paths变量
	paths = {}
	ROOT_PATH = os.getcwd()
	CONFIG_PATH = ROOT_PATH+'/config.conf'
	DICT_PATH = ROOT_PATH + '/data/dict.txt'
	SCRIPT_PATH = ROOT_PATH+'/core/scripts/'
	REPORT_PATH = ROOT_PATH+'/reports/'
	paths.update({'ROOT_PATH':ROOT_PATH,'CONFIG_PATH':CONFIG_PATH,'DICT_PATH':DICT_PATH,'SCRIPT_PATH':SCRIPT_PATH,'REPORT_PATH':REPORT_PATH})
	return paths


def getdata():  # 获取字典的值
	filename = paths['DICT_PATH']
	data = []
	with open(filename) as f:
		for t in f:
			data.append(t.strip())
	return data

queue = Queue.Queue()
task = Queue.Queue() #
thread_mode = '0' #默认为0
output = CLIOutput()
colorprinter = ColorPrinter()
paths = getpath()
data = getdata()
threads_num = 10
webdir_result = [] #用于存储一些无法保存的扫描结果
portscan_result = []
exploit_result = []


banner_0 = r"""
	        _____                    
	   ____/__  /_____________ _____ 
	  / ___/ / / ___/ ___/ __ `/ __ \
	 (__  ) / (__  ) /__/ /_/ / / / /
	/____/ /_/____/\___/\__,_/_/ /_/ 
	{ s7scan渗透测试工具 by 七星 }
"""

banner_1 = r"""
 _____________________________
< s7scan渗透测试工具 by 七星 >
 -----------------------------
     \
      \
          oO)-.                       .-(Oo
         /__  _\                     /_  __\
         \  \(  |     ()~()         |  )/  /
          \__|\ |    (-___-)        | /|__/
          '  '--'    ==`-'==        '--'  '

"""

banner_2 = r"""
	 ______________________________
	< s7scan渗透测试工具 by 七星 >
	 ------------------------------
	  \
	   \   \
	        \ /\
	        ( )
	      .( o ).
"""


banner_3 = r"""
 _____________________________
< s7scan渗透测试工具 by 七星 >
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

"""

banner_4 = r"""
	 _____________________________
	< s7scan渗透测试工具 by 七星 >
	 -----------------------------
	   \
	    \
	        .--.
	       |o_o |
	       |:_/ |
	      //   \ \
	     (|     | )
	    /'\_   _/`\
	    \___)=(___/
"""

banners = [banner_0,banner_1,banner_2,banner_3,banner_4]

if __name__ == '__main__':
	print threads_num