#!/usr/bin/python
#coding: utf-8
import logging  
import commands
import sys
sys.path.append('/usr/local/factory/py/test/')
import os
import test_ui
from suds.client import Client  
import unittest
#from cros.factory.test import test_ui
_ID_STATE_DIV = 'state_div'
_LOG_MESSAGE = ( lambda t : test_ui.MakeLabel('abcis %s' % t,
                                               'abcd is %s.' % t))

if __name__ == '__main__':  
    #logging.basicConfig(level=logging.INFO)  
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)  
    hello_client = Client('http://112.27.208.240:8001/Service1.asmx?wsdl')  
    result = hello_client.service.ReturnStationInfoStr(commands.getoutput('vpd -g mlb_serial_number'))
    str = result
    if str[0][1]:
      print('pass the station')
    else: 
      print('Error is %s', str[0][2])
      stop
