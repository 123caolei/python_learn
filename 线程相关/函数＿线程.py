#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
'''
i=2
while (i<100):
    j=2
    while (j<=(i/j)):
        if not(i%j):break
        j+=1
    if (j>i/j): print i,"shisushu"
    i+=1

print "bye"
'''
'''
print os.getcwd()

try:
    file=open("2.py","w")
    file.write("just for test")

finally:
    print "chenggong"
    file.close()
'''
'''
class test():
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1
        self.arg2=arg2
        self.arg3=arg3
class foo(test):
    def __init__(self,arg1,arg2,arg3,arg4):
        test.__init__(self,arg1,arg2,arg3)
        self.arg4=arg4


c=foo(1,2,3,4)
print c.arg1,c.arg2,c.arg4
'''
import thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

while 1:
    pass