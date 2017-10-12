#!/usr/bin/env python        
#coding:utf-8

import random

class ColorPrinter:


    def print_black_text(self,content): #200
        message = "\033[0;30m%s\033[0m" % (content)
        print message

    def print_red_text(self,content): #200
        message = "\033[1;31m%s\033[0m" % (content)
        print message

    def print_green_text(self,content): #200
        message = "\033[1;32m%s\033[0m" % (content)
        print message

    def print_yello_text(self,content): #40x
        message = "\033[1;33m%s\033[0;m" % (content)
        print message

    def print_blue_text(self,content): #40x
        message = "\033[1;34m%s\033[0;m" % (content)
        print message

    def print_magenta_text(self,content): #30x
        message = "\033[1;35m%s\033[0;m" % (content)
        print message

    def print_cyan_text(self,content): #30x
        message = "\033[1;36m%s\033[0;m" % (content)
        print message

    def print_white_text(self,content): #30x
        message = "\033[1;37m%s\033[0;m" % (content)
        print message

    def print_reset_text(self,content): #30x
        message = "\033[1;38m%s\033[0;m" % (content)
        print message

def print_random_text(content):
    output = ColorPrinter()
    colors = {31:'red',32:'green',33:'yello',34:'blue',35:'magenta',36:'cyan',37:'white'}  #抛弃了黑色
    color =  colors[random.randint(31,37)]
   # print color
    getattr(output,'print_%s_text'%color)(content)

if __name__ == '__main__':
    print_random_text('hello')
    