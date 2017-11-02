#!/usr/bin/env python
# coding=UTF-8
import math
from time import ctime
import socket
import sys
import datetime
print(datetime.datetime.now())
from os.path import join
print (join('F://','ISO'))
print sys.path
print ctime()
def my_fun():
   a=set(['a','b','c','d','c','a','e'])
   b=set(['z'])
   print (a&b)
   print a
   print math.pi
def nop():
    pass
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(2,20)
print power(5)
