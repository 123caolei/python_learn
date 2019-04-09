#!/usr/bin/python
#coding: utf-8
import logging  
import commands
import sys
import os
from suds.client import Client  
import unittest

class Reg():
  def setUp(self):
    self._ui = test_ui.UI()
  def SetState(self, html, append=False):
    self._ui = test_ui.UI()
    self._ui.SetHTML(html,append,id=_ID_STATE_DIV)
  def runtest(self):
    pass
if __name__ == '__main__':  
    #logging.basicConfig(level=logging.INFO)  
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)  
    reg = Reg()
    hello_client = Client('http://112.27.208.240:8001/Service1.asmx?wsdl')  
    result = hello_client.service.ReturnRegistrationStr(commands.getoutput('vpd -g mlb_serial_number'))
    str = result
    ubind = 'vpd -i RW_VPD -s'+'ubind_attribute='+str[0][3]
    gbind = 'vpd -i RW_VPD -s'+'gbind_attribute='+str[0][4]
    if str[0][1]:
      os.system(ubind)
      logging.info('ubind is %s',str[0][3])
      #reg.SetState(_LOG_MESSAGE)
      os.system(gbind)
      logging.info('gbind is %s',str[0][4])
    else: 
      logging.info('Error is %s', str[0][2])
    #commands.getoutput('vpd -i RW_VPD -s abc=str[0][4]')
    #f=open('/usr/local/factory/python/reg.txt','w')
    #print str[0][4] 
    #f.close()
