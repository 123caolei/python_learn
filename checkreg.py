#!/usr/bin/python
#coding: utf-8
import commands

if __name__ == '__main__':
  ubind = commands.getoutput('vpd -i RW_VPD -g ubind_attribute')
  gbind = commands.getoutput('vpd -i RW_VPD -g gbind_attribute')
  print len(ubind)
  if len(gbind) != 0:  
    if len(ubind) != 0:
      pass
    else: 
      stop
  else:
    stop 
     
