#! /usr/bin/env python
# -*- coding: utf-8 -*-


import thread
import  time
import threading

'''
 def print_time(threadname,delay):
    count=0
    while count <5:
        time.sleep(delay)
        count+=1
        print "%s %s" % (threadname,time.ctime(time.time()))
try:
    thread.start_new_thread(print_time,("thread1",2,))
    thread.start_new_thread(print_time,("thread2",3,))
except:
    print  "error"
'''
'''
def multiple(arg,*args,**dict):
    print "arg",arg
    for value in args:
        print "args:",value
    for key in dict:
        print "dict:"+key+":"+bytes(dict[key])
multiple(1,2,3,4,num=34,mk=21)
'''

exitFlag=0
class mythread(threading.Thread):
    def __init__(self,threadid,name,counter):
        threading.Thread.__init__(self)
        self.threadid=thread
        self.name=name
        self.counter=counter
    def run(self):
        print "starting"+self.name
        print_time(self.name,self.counter,5)
        print "exiting"+self.name
def print_time(threadname,delay,counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s:%s" %(threadname,time.ctime(time.time()))
        counter-=1

thread1 =mythread(1,"1",1)
thread2 =mythread(2,"2",2)
thread1.start()
thread2.start()
print "exiting"