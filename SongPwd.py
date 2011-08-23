#! /usr/bin/python
from pychart import *
from getchar import *
from plot import *
from usrOperate import *
from pwdCompare import *
import os

x = raw_input('Login<L> or Register<R>?')
if x == 'L':
    usrName = raw_input('your name:')
    usrDict = getUsrData('usrData')
    libPwd = usrDict.get(usrName)
    if libPwd == None:
        print('no usr')
    libCount, libPwd = map2pwd(libPwd)
    print(libPwd)
    print('input pwd');
    inputPwd, inputCount = getPwd()#get inputPwd
    print(inputPwd)
    if inputCount == libCount:
        print('same count')
        putPwd('cmp1', usrName, libCount, libPwd)
        putPwd('cmp2', usrName, inputCount, inputPwd)
        #use pwdCompare to outpu diagram
    else:
        print('wrong count')
elif x == 'R':
    register()
elif x == 'C':
    os.popen('rm usrData')
    os.popen('rm cmp1')
    os.popen('rm cmp2')
    print('usrData CLEARED!')
elif x == 'T':
    file_object = open('usrData')
    print(file_object.readlines())
else: print('wrong')
