#!/usr/bin/env python		
#coding:utf-8

import time
import random

def poc(str):
	time.sleep(1)
	if random.randint(1,10) > 5:
		return True 
	return False

if __name__ == '__main__':
	print poc('1')