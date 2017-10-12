#!/usr/bin/env python		
#coding:utf-8

import os
import sys
from core.controller import *

class Program:
	def __init__(self):
		self.controller = Controller() #启动控制器
		self.controller.main()


if __name__ == '__main__':
	main = Program()



