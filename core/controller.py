#!/usr/bin/env python		
#coding:utf-8

import os
import sys
import json
import argparse
import threading
import random
from prettytable import PrettyTable
from core.config import ConfigFileParser,webdir_result,portscan_result,exploit_result
from core.data import output,data,queue,output,threads_num,paths,banners,colorprinter,print_random_text,thread_mode
from core.exploit import loadScript,loadTargets
from core.plugins.thread_func import Thread_func
from core.plugins.process_func import speed
from core.plugins.gevent_func import Gevent_func
from core.plugins.portscan import PortScan
from core.plugins.subnet import Subnet
from core.plugins.whois import whois
from core.plugins.password import PasswdGenerator
from core.ctftools.bintostr import bintostr,asciitostr,hextostr
from core.ctftools.morse import morse
from core.ctftools.zhalan import zhalan
from core.ctftools.nbase64 import nbase64
from core.ctftools.kaisa import kaisa,kaisa2


class Controller():
	def __init__(self):
		self.script_objs = None
		self.outable = PrettyTable(["target", "result"])
		self.outable.align["target"] = "l"  
		self.outable.align["result"] = "l"
		self.outable.padding_width = 5
		self.cf  = ConfigFileParser()
		threads_num = self.cf.threads_num()
		print_random_text(banners[random.randint(0,4)])
		#colorprinter.print_blue_text(u'[-_-]不忘初心，一群走在安全路上的年轻人[-_-]')
	#目录扫描
	def webdir(self,args):
		output.dataOut('[*] 加载目录扫描插件...')
		#参数解析
		url = args.u
		outfile = args.o
		output.target(url)

		#配置文件解析
		mode = self.cf.webdir_mode()
		thread_mode = mode

		#调用扫描插件
		if mode == '0':
			Thread_func(url,data,threads_num)
		if mode =='1':
			Gevent_func(url,data,threads_num)
		if mode == '2':
			speed(Thread_func,url)

		if outfile:
			self.report(webdir_result,outfile)
	#端口扫描
	def portscan(self,args):
		output.dataOut('[*] 加载端口扫描插件...')
		#参数解析
		ip = args.t
		mask = args.m 
		port = args.p
		file = args.f
		outfile = args.o

		# 获取配置文件里的端口信息
		scanports = self.cf.scanports()
		
		#调用插件
		if ip:
			output.target(ip)
			ps = PortScan(ip=ip,ports=scanports)
		elif mask:
			if port:
				ps = PortScan(single_port=port,Mask=mask)
			else:
				output.warning('please input port')
		elif file:
			ps = PortScan(file=file,ports=scanports)

		if outfile:
			self.report(portscan_result,outfile)

	# C段扫描
	def subnet(self,args):
		output.dataOut('[*] 加载C段扫描插件...')
		#参数解析
		ip = args.t 
		if ip:
			Subnet(ip)
	#whois 信息查询
	def whois(self,args):
		output.dataOut('[*] 加载whois查询插件...')
		#参数解析
		domain = args.t 
		if domain:
			whois(domain)
	#社会工程学字典生成, 日期生成
	def passwd(self,args):
		fullname = args.fullname 
		nickname = args.nickname
		englishname = args.englishname
		partnername = args.partnername
		phone = args.phone 
		qq = args.qq
		keywords = args.keywords
		oldpasswd = args.oldpasswd
		keynumbers = args.keynumbers
		domain = args.domain
		startyear = args.startyear
		endyear = args.endyear 
		splitword = args.splitword

		if startyear and endyear:
			pg = PasswdGenerator(startyear=startyear,endyear=endyear,splitword=splitword)
			result = pg.birthday()
		else:
			#print '社会工程学字典生成'
			pg = PasswdGenerator(fullname=fullname,nickname=nickname,englishname=englishname,partnername=partnername,phone=phone,qq=qq,keywords=keywords,oldpasswd=oldpasswd,keynumbers=keynumbers,domain=domain)
			result = pg.generate()

		output.pocOut('[*] 生成字典大小:%s条数据'%str(result[-1])) 
		if args.o:
			with open(args.o,'w') as f:
				for i in result[0]:
					#print i
					f.write(str(i)+"\n")
		else:
			for i in result[0]:
				print i

	# 一些编码处理
	def crypto(self,args):
		output.dataOut('[*] 加载crypto插件...')
		#参数解析
		#print args
		if args.kaisa:
			kaisa(args.kaisa)
		elif args.kaisa2:
			kaisa2(args.kaisa2)
		elif args.morse:
			morse(args.morse)
		elif args.zhalan:
			zhalan(args.zhalan)
		elif args.nbase64:
			nbase64(args.nbase64)
		elif args.b2s:
			bintostr(args.b2s)
		elif args.a2s:
			asciitostr(args.a2s)
		elif args.h2s:
			hextostr(args.h2s)

			
	def Exploit(self,args):
		#self.isview = args.v #添加一个-v显示详细信息的参数
		# list所有的poc
		if args.list:
			files = []
			all_files = os.listdir(paths['SCRIPT_PATH'])
			#print all_files
			for file in all_files:
				if 'pyc' in file or '__init__.py' in file:
					pass 
				else:
					files.append(file)

			#print files	
			mes1 = '[*] Script Name（总共%s个POC)'%str(len(files)-1)
			output.dataOut(mes1)
			for file in files:
				if '__init__' not in file and 'pyc' not in file:
					output.dataOut('   '+file)

		# 查询文件名
		if args.q:
			keyword = args.q
			files = []
			all_files = os.listdir(paths['SCRIPT_PATH'])
			#print all_files
			for file in all_files:
				if 'pyc' in file or '__init__.py' in file:
					pass 
				else:
					files.append(file)
			mes = "[*] 查询关键字: %s"%keyword
			output.dataOut(mes)
			for file in files:
				if '__init__' not in file :
					if keyword in file:
						output.dataOut('   '+file)

		#加载poc文件
		if args.s:
			script_name = args.s
			if script_name.endswith('.py'):
				script_name = script_name[:-3]
			#print script_name
			output.pocOut('[*] 加载poc: %s.py ...\n'%script_name)
			script_path = paths['SCRIPT_PATH']+script_name
			self.script_objs = loadScript(script_name)
			#print self.script_obj.poc(1)

		if (args.s and not args.u) and (args.s and not args.m):
			output.error('请设置target目标')
			sys.exit()

		if args.a:
			if args.m:
				output.warning('please input single target')
				sys.exit()
			output.target(args.u)
			files = os.listdir(paths['SCRIPT_PATH'])
			for file in files:
				if file.endswith('.py') and '__init__' not in file and 'test' not in file:
					file = file.rstrip('.py')
					self.script_objs = loadScript(file)
					#print self.script_objs
					loadTargets(args)
					output.pocOut('\n[*] 加载poc: %s.py'%file)
					self.scan()
			#print exploit_result
			self.printtable()
			if args.o:
				outfile = args.o 
				self.report(exploit_result,outfile)
			sys.exit()
     
          

		#加载目标
		loadTargets(args)

		# 如果是单个url, 直接调用scan函数，没必要用多线程
		if args.u:  
			output.target(args.u)
			self.scan()
		else:
			self.run()
		self.printtable()
		if args.o:
			outfile = args.o 
			self.report(exploit_result,outfile)

	# 对单个目标的扫描
	def scan(self):
		while 1:
			try:
				url = queue.get(False)
				res = self.script_objs.poc(url)
				#print url,'res:',res,type(res)
				if res: # 如果失败返回False
					mes = 'Target %s is exploit...: \n%s'%(url,res)
					output.expOut(mes)
					#print 'url:',url,res
					exploit_result.append((url,res))
				elif res is False:
					output.expOut('Target %s fail'%url)
				else:
					#print res
					output.expOut('unknown')
			except:
				break

	# 基于多线程的扫描
	def run(self):
		threads = []
		for i in range(threads_num):
			t = threading.Thread(target=self.scan)
			#t.setDaemon(True)
			threads.append(t)
			t.start() 
		for t in threads:
			t.join()
			# if t.isAlive():
			# 	print 'this thread is timeout'

        # while 1:
        #     if queue.qsize() > 0:
        #         time.sleep(0.01)
        #     else:
        #         break
	# report 导出
	def report(self,result,outfile):
		content = json.dumps(result, sort_keys=True, indent=4)
		with open(paths['REPORT_PATH']+outfile,'a') as f:
			f.write(content)

	def printtable(self):
		if exploit_result:
			for result in exploit_result:
				self.outable.add_row(result)
			print self.outable

	def main(self):
		reload(sys)
		sys.setdefaultencoding("utf-8")
		'''
			exploit -s  -u 
			exploit -s -f 
			explit -l

			webdir -u (mode=0 thread, mode=1 gevent mode=2 thread+mulit)

			portscan -ip
			portscan -m -p 

		'''
		parser = argparse.ArgumentParser() #argparse会自动添加usage
		#产生一个子命令解析器
		subparser = parser.add_subparsers(title=u'子命令',description=u"使用 's7scan.py 子命令 -h' 获得子命令帮助")

		#使用子命令解析器去生成每一个子命令

		# exploit  漏洞利用
		exploit = subparser.add_parser("exploit",help=u"Exploit系统，可自行添加POC, 批量执行POC",description=u'example: python s7scan.py exploit -s test -m 127.0.0.1/30')
		exploit.add_argument('-s',help=u"加载POC, 提供test测试poc")
		exploit.add_argument('-a',help=u"加载所有的POC,对单个目标点进行测试",action="store_true")
		exploit.add_argument('-u',help=u"target url: 目标url")
		exploit.add_argument('-f',help=u"target file: 目标url文件")
		exploit.add_argument('-m',help=u"target mask: 目标网段,默认掩码为24")
		exploit.add_argument('-l','--list',help=u"列举所有的poc",default=False, action='store_true')  #store_true表示是布尔类型，不需要传值，只需要判断有无这个参数
		exploit.add_argument('-q',help=u"关键字搜索poc",default=False)
		exploit.add_argument('-o',help=u"导出json格式文件")
		exploit.set_defaults(func=self.Exploit)

		# webdir 目录扫描
		webdir = subparser.add_parser("webdir",help=u"敏感目录扫描",description=u"example:python s7scan.py webdir -u localhost")
		webdir.add_argument('-u',help="target url:目标url")
		webdir.add_argument('-o',help=u"导出json格式文件")
		webdir.set_defaults(func=self.webdir)

		# portscan 端口扫描
		portscan = subparser.add_parser("portscan",help=u"端口扫描",description=u"example:python s7scan.py portscan -t localhost")
		portscan.add_argument('-t',help=u"target ip 目标ip")
		portscan.add_argument('-m',help=u"mask(127.0.0.1/28 默认掩码为24)")
		portscan.add_argument('-p',help=u"port 目标端口",type=int)
		portscan.add_argument('-f',help=u"网段文件列表")
		portscan.add_argument('-o',help=u"导出json格式文件")
		portscan.set_defaults(func=self.portscan)

		#subnet　C段扫描
		subnet = subparser.add_parser("subnet",help=u"C段扫描",description=u"example:python s7scan.py subnet -t 211.82.99.1")
		subnet.add_argument('-t',help=u"target ip 目标ip")
		subnet.set_defaults(func=self.subnet)

		#subnet　C段扫描
		whois = subparser.add_parser("whois",help=u"whois查询",description=u"example:python s7scan.py whois -t blogsir.com.cn")
		whois.add_argument('-t',help=u"target domain")
		whois.set_defaults(func=self.whois)

		#passwd 社会工程学字典生成
		passwd = subparser.add_parser("passwd",help=u"社会工程学字典生成,日期生成",description=u"example:python s7scan.py passwd -fullname 'zhang san' 或者passwd -startyear 2000 -endyear 2017")
		passwd.add_argument('-fullname',help=u"名字字母全称,空格分隔,如zhang san feng")
		passwd.add_argument('-nickname',help=u"昵称")
		passwd.add_argument('-englishname',help=u"英文名")
		passwd.add_argument('-partnername',help=u"伴侣姓名字母全称")
		passwd.add_argument('-phone',help=u"手机号")
		passwd.add_argument('-qq',help=u"qq号")
		passwd.add_argument('-keywords',help=u"关键字,空格分隔")
		passwd.add_argument('-keynumbers',help=u"关键数字,空格分隔")
		passwd.add_argument('-oldpasswd',help=u"旧的密码")
		passwd.add_argument('-domain',help=u"域名")
		# 只生成日期
		passwd.add_argument('-startyear',help=u"生成日期的开始年份")
		passwd.add_argument('-endyear',help=u"生成日期的结束年份")
		passwd.add_argument('-splitword',help=u"分隔词,可以是/,-,默认为空",default="")
		passwd.add_argument('-o',help=u"到处txt字典")
		passwd.set_defaults(func=self.passwd)

		#crypto
		crypto = subparser.add_parser("crypto",help=u"一些解密的辅助工具",description=u"example:python s7scan.py crypto -t blogsir.com.cn")
		crypto.add_argument('-k','--kaisa',help=u"凯撒解密,只偏移英文大小写字母")
		crypto.add_argument('-k2','--kaisa2',help=u"凯撒移位,偏移整个ascii")
		crypto.add_argument('-m','--morse',help=u"摩斯解密")
		crypto.add_argument('-zl','--zhalan',help=u"栅栏解密")
		crypto.add_argument('-nb','--nbase64',help=u"自动识别多重base64解密")
		crypto.add_argument('-b2s',help=u"二进制转字符串,八位，七位分别解密")
		crypto.add_argument('-a2s',help=u"ascii转字符串,用空格或者逗号分隔")
		crypto.add_argument('-h2s',help=u"十六进制转字符串")
		crypto.set_defaults(func=self.crypto)

		args = parser.parse_args()
		args.func(args)
