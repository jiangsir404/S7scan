# s7scan

### 安装依赖

    pip install -r requirements.txt 

python-nmap 库需要有nmap环境，如果要使用端口批量扫描功能，请先安装nmap:`apt-get install namp`

#### Show site
具体效果可以看我博客导航页面上的两个视频文件

    http://blog.s7star.cn/

### Usage
```
usage: s7scan.py [-h] {exploit,webdir,portscan,subnet,whois,passwd,crypto} ...

optional arguments:
  -h, --help            show this help message and exit

子命令:
  使用 's7star.py 子命令 -h' 获得子命令帮助

  {exploit,webdir,portscan,subnet,whois,passwd,crypto}
    exploit             Exploit系统，可自行添加POC, 批量执行exp
    webdir              敏感信息扫描
    portscan            端口扫描
    subnet              C段扫描
    whois               whois查询
    passwd              社会工程学字典生成,日期生成
    crypto              一些解密的辅助工具
```


### 各个功能

#### exploit 

```
usage: s7scan.py exploit [-h] [-s S] [-a] [-u U] [-f F] [-m M] [-l] [-q Q]
                         [-o O]

example: python s7scan.py exploit -s test -m 127.0.0.1/30

optional arguments:
  -h, --help  show this help message and exit
  -s S        加载POC, 提供test测试poc
  -a          加载所有的POC,对单个目标点进行测试
  -u U        target url: 目标url
  -f F        target file: 目标url文件
  -m M        target mask: 目标网段,默认掩码为24
  -l, --list  列举所有的poc
  -q Q        关键字搜索poc
  -o O        导出json格式文件
```

#### webdir 
```
usage: python s7scan.py [-h] {exploit,webdir,portscan} ... webdir
       [-h] [-u U] [-o O]

example:python s7scan.py webdir -u localhost

optional arguments:
  -h, --help  show this help message and exit
  -u U        target url:目标url
  -o O        导出json格式文件
```


#### portscan 
```
usage: python s7scan.py [-h] {exploit,webdir,portscan} ... portscan
       [-h] [-t T] [-m M] [-p P] [-o O]

example:python s7scan.py portscan -t localhost

optional arguments:
  -h, --help  show this help message and exit
  -t T        target ip 目标ip
  -m M        mask(127.0.0.1/28 默认掩码为24)
  -p P        port 目标端口
  -o O        导出json格式文件
```

#### subnet
```
usage: s7scan.py subnet [-h] [-t T]

example:python s7scan.py subnet -t 211.82.99.1

optional arguments:
  -h, --help  show this help message and exit
  -t T        target ip 目标ip

```

#### whois

```
usage: s7scan.py whois [-h] [-t T]

example:python s7scan.py whois -t blogsir.com.cn

optional arguments:
  -h, --help  show this help message and exit
  -t T        target domain
```

#### passwd 
```
example:python s7scan.py passwd -fullname 'zhang san' 或者passwd -startyear 2000
-endyear 2017

optional arguments:
  -h, --help            show this help message and exit
  -fullname FULLNAME    名字字母全称,空格分隔,如zhang san feng
  -nickname NICKNAME    昵称
  -englishname ENGLISHNAME
                        英文名
  -partnername PARTNERNAME
                        伴侣姓名字母全称
  -phone PHONE          手机号
  -qq QQ                qq号
  -keywords KEYWORDS    关键字,空格分隔
  -keynumbers KEYNUMBERS
                        关键数字,空格分隔
  -oldpasswd OLDPASSWD  旧的密码
  -domain DOMAIN        域名
  -startyear STARTYEAR  生成日期的开始年份
  -endyear ENDYEAR      生成日期的结束年份
  -splitword SPLITWORD  分隔词,可以是/,-,默认为空
  -o O                  到处txt字典
```

#### crypto

```
usage: s7scan.py crypto [-h] [-k KAISA] [-k2 KAISA2] [-m MORSE] [-zl ZHALAN]
                        [-nb NBASE64] [-b2s B2S] [-a2s A2S] [-h2s H2S]

example:python s7scan.py crypto -t blogsir.com.cn

optional arguments:
  -h, --help            show this help message and exit
  -k KAISA, --kaisa KAISA
                        凯撒解密,只偏移英文大小写字母
  -k2 KAISA2, --kaisa2 KAISA2
                        凯撒移位,偏移整个ascii
  -m MORSE, --morse MORSE
                        摩斯解密
  -zl ZHALAN, --zhalan ZHALAN
                        栅栏解密
  -nb NBASE64, --nbase64 NBASE64
                        自动识别多重base64解密
  -b2s B2S              二进制转字符串,八位，七位分别解密
  -a2s A2S              ascii转字符串,用空格或者逗号分隔
  -h2s H2S              十六进制转字符串

```


### View

![](help.png)



### some issues

1. 导出日志的时候默认是在reports目录下面的，如果自己加上目录会导致报错，扫描的结果无法保存下来

解决:设置一个临时保存文件，如果保存路径出错，就暂时放在临时文件里面


2. 加载目标的时候会自动规范成http://或https://, 有的poc只需要主机部分，需要自行修改去掉协议名

3. 端口扫描的常见端口需要修改

4. 端口扫描的输出静默模式是只显示开放端口， -vv 显示详细模式

5. 端口扫描导出日志显示制定端口开放的主机数量

6. 漏洞利用模块： 攻击目标显示不足，fpm.py存在没有输出的情况

7. 去除whois和sub

8.  passwd 生成密码 -k "s7scan admin bistu 404" 任意生成一个任意组合的密码

9. 敏感信息扫描换成爬虫扫描，以及BBscan那种快速备份扫描。

