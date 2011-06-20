from pychart import *
from getchar import *
from plot import *
from usrOperate import *
from pwdCompare import *
import os

x = raw_input('Login<L> or Register<R>?')
if x == 'L':
    lib_name, lib_count, lib_pwd = getUsrData()
    input_pwd, input_count = getPwd()
    print(lib_count, input_count)
    if input_count == lib_count:
        dualPlot(input_pwd, lib_pwd)
    else:
        print('wrong count')
elif x == 'R':
    register()
elif x == 'C':
    os.popen('rm usrData')
    print('usrData CLEARED!')
else: print('wrong')
