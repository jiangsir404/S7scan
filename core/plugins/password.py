#!/usr/bin/env python		
#coding:utf-8

import itertools
import time
import string

class PasswdGenerator:
	'''类变量
	'''
	_numList = ['123456', '123123', '123123123', '112233', '445566', '456456', '789789', '778899', '321321', '520', '1314', '5201314', '1314520', '147369', '147258', '258', '147', '456', '789', '147258369', '111222', '123', '1234', '12345', '1234567', '12345678', '123456789', '987654321', '87654321', '7654321', '654321', '54321', '4321', '321']
	_prefix = ['a','qq','Qq','qQ','zfb','aa','abc','qwe','woaini']
	_suffix = ['123','$$$','$#@','%$#','#$%','###']
	#和partner混合的常用前缀
	partnerPrefixList = ['520','5201314','1314','iloveu','iloveyou']
	#和domain,company组合的前缀列表
	domainPrefixList = ['admin','root','manager','system'] 

	def __init__(self,fullname="",nickname="",englishname="",partnername="",phone="",qq="",keywords="",oldpasswd="",keynumbers="",domain="",startyear="",endyear="",splitword=""):
		self.fullname = fullname 
		self.nickname = nickname 
		self.englishname = englishname
		self.partnername = partnername
		self.phone = phone 
		self.qq = qq 
		self.keywords = keywords
		self.keynumbers = keynumbers
		self.oldpasswd = oldpasswd
		self.domain = domain 
		self.startyear = startyear
		self.endyear = endyear 
		self.splitword = splitword


		self.fullNameList = []
		self.ShortNameList = []
		self.innerNumList = []
		self.prefixList = []
		self.suffixList = []
		self.mixedKeywordList = []

		self.result = []


	def product(self, listA, listB):
		if not listA and not listB:
			return []
		result = []
		for a,b in itertools.product(listA, listB):
			if len(a+b) > 5 and len(a+b) < 17:
				#print a,b
				result.append(a+b)
				result.append(a+"@"+b)

		return result

	
	def getNumList(self):
		pass

	def getFullNameList(self,fullname):
		if not fullname:
			return []
		else:
			result = []
			nameSplited = fullname.split() #用空格分割
			if len(nameSplited) == 1:
				result.append(nameSplited[0])
				result.append(nameSplited[0].title())
			elif len(nameSplited) == 2:
				result += ["".join(nameSplited),nameSplited[1]+nameSplited[0],nameSplited[0].title()+nameSplited[1].title()]
			else: #长度如果为3
				result += [nameSplited[0]+nameSplited[1]+nameSplited[2], nameSplited[1]+nameSplited[2]+nameSplited[0],nameSplited[0].title()+nameSplited[1].title(),nameSplited[2].title()]

			return result #+ [x.upper() for x in result]

	# 获取名字的简写 lj,ljs等
	def getShortNameList(self,fullname): 
		if not fullname:
			return []
		else:
			result = []
			func = lambda x:[x, x.title(), x[0].lower(), x[0].upper(), x.upper()]
			nameSplited = fullname.split()
			if len(nameSplited) == 1:
				result += func(nameSplited[0])
				#print result 
			elif len(nameSplited) == 2:
				shortName = nameSplited[0][0].lower() + nameSplited[1][0].lower()
				result += func(shortName)
				#print result
			else:
				shortName = nameSplited[0][0].lower() + nameSplited[1][0].lower() + nameSplited[2][0].lower()
				result += func(shortName)
				#print result
				shortNameRS = nameSplited[1][0].lower() + nameSplited[2][0].lower() + nameSplited[0][0].lower()
				shortNameR = nameSplited[1][0].lower() + nameSplited[2][0].lower() + nameSplited[0]
				result += [shortNameR,shortNameRS,shortNameRS.upper()]
				#print result
			return result

	# 添加一些年份，常用重复数字等
	def getInnerNumList(self):
		result = self._numList
		for i in range(10):
			result += [str(i)*x for x in range(1,10)] #字母和数字的乘法

		endyear = int(time.strftime("%Y"))
		result += [str(x) for x in range(2000,endyear+1)]

		if self.keynumbers:
			result += self.keynumbers.split()
		if self.oldpasswd:
			result.append(self.oldpasswd)

		return result

	# 生成各种类型的列表
	def ListHandle(self):
		self.fullNameList = self.getFullNameList(self.fullname)
		self.shortNameList = self.getShortNameList(self.fullname)
		self.innerNumList = self.getInnerNumList()
		self.prefixList = self._prefix +[x.upper() for x in self._prefix]
		self.suffixList = self._suffix + [x.upper() for x in self._suffix]


		# 所有全称，简称，英文名等
		self.mixedKeywordList += self.shortNameList
		self.mixedKeywordList += self.fullNameList

		if self.nickname:
			self.mixedKeywordList.append(self.nickname)
		if self.englishname:
			self.mixedKeywordList.append(self.englishname)
		if self.keywords:
			self.mixedKeywordList += self.keywords.split()

	def mixResult(self):
		#print 'mixedkeyword:',self.mixedKeywordList
		#print 'innerNumlist',self.innerNumList
		self.result += self.product(self.mixedKeywordList,self.innerNumList)
		self.result += self.product(self.mixedKeywordList,self.suffixList)

		if self.phone:
			self.result += self.product(self.prefixList+self.mixedKeywordList,[self.phone])
		if self.qq:
			self.result += self.product(self.prefixList+self.mixedKeywordList,[self.qq])
		if self.partnername:
			nameList = self.getShortNameList(self.partnername)
			nameList += self.getFullNameList(self.partnername)
			self.result += self.product(self.partnerPrefixList,nameList)

		if self.domain:
			self.result += self.product(self.domainPrefixList,[self.domain])

			
		return self.result

	def birthday(self): #八位数字 20170915 2017/09/15 2017-09-15
		date = []
		for year in range(int(self.startyear),int(self.endyear)+1):
			for month in range(1,13):
				for day in range(32):
					date.append(str(year)+self.splitword+str(month).zfill(2)+self.splitword+str(day).zfill(2))

		return date,len(date)


	def generate(self):
		self.ListHandle()
		self.mixResult()
		return self.result,len(self.result)

if __name__ == '__main__':
	pg = PasswdGenerator(fullname="bistu",partnername="zhang san")
	print pg.generate()
	# pg = PasswdGenerator(startyear="2000",endyear="2018",splitword="/")
	# pg.birthday()