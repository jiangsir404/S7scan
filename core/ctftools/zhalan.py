#!/usr/bin/env python    
#coding:utf-8
import sys

def zhalan(e):
  elen = len(e)
  field=[]
  for i in range(2,elen):
      if(elen%i==0):
          field.append(i) # 求出公因子数

  print '栏数:',field
  for f in field:
      b = elen / f
      result = {x:'' for x in range(b)}
      #print result
      for i in range(elen):
         a = i % b;
         result.update({a:result[a] + e[i]})
      #print result
      d = ''
      for i in range(b):
         d = d + result[i]
      print d

if __name__ == '__main__':
  e = 'thisisflag'
  zhalan(e)