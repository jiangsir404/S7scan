#!/usr/bin/env python		
#coding:utf-8


slist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def kaisa(flag):
	for offset in range(1, 27):
		s = ''
		for i in flag:  #两层if..else
			if i in slist:  #如果是可见字符，则移位，否则不动
				if (ord(i)+offset)>ord('z') and ord(i)<=ord('z') or (ord(i)+offset)>ord('Z') and ord(i)<=ord('Z'): # 注意优先级和<=
					s += chr(ord(i)+offset-26)
				else:
					s += chr(ord(i)+offset)
			else:
				s += i
		print offset,s.lower()
				
def kaisa2(flag):  #没有回移，自动去掉大于127,小于30的部分
	for offset in range(127):
		s = ''
		for i in flag:
			temp = (ord(i)+offset)%127 
			if 32 < temp < 127:
				s += chr(temp)
				feel = 1
			else:
				feel = 0
				break
		if feel == 1:
			print offset,s



if __name__ == '__main__':
	kaisa("""QEBEFKQFPCFSB""")
	#kaisa2("""UJ>Kxqefpfpklqbjlgfz""")