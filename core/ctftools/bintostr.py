#!/usr/bin/env python        
#coding:utf-8

import re
import argparse

flag = '110011011011001100001110011111110111010111011000010101110101010110011011101011101110110111011110011111101'


def bintostr(text):
    text = text.replace(' ','')
    text2 = re.findall(r'.{7}',text)
    text = re.findall(r'.{8}',text)
    s = map(lambda x:chr(int(x,2)),text) #批量二进制转十进制
    s2 = map(lambda x:chr(int(x,2)),text2)
    flag = ''.join(s)
    print 'split_by_7:',''.join(s2)
    print 'split_by_8:',
    return flag.encode('base64')

def asciitostr(text):
    if ' ' in text:
        text = text.split(' ')
    elif ',' in text:
        text = text.split(',')
    elif '&' in text:
        text = text.replace('&','')
        text = text.split(';')
        text.remove('')
        #print text
    s = map(int,text)
    s = map(chr,s)
    flag = ''.join(s)
    return flag

def hextostr(text):
    text = text.replace(' ','')
    text = re.findall(r'.{2}',text)
    #print text
    s = map(lambda x:chr(int(x,16)),text)
    #print s
    flag = ''.join(s)
    return flag
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b",help=u"二进制转字符")
    parser.add_argument("-a",help=u"ascii转字符串")
    parser.add_argument("-x",help=u"十六进制转字符")
    argv = parser.parse_args()
    #print argv
    if argv.b:
        res = bintostr(argv.b)
    elif argv.a:
        res = asciitostr(argv.a)
    elif argv.x:
        res = hextostr(argv.x)
    # res = bintostr(flag)
    # res = asciitostr(flag)
    # res = hextostr(flag)
    print res
