from getchar import *
from plot import *
from usrOperate import *
import os

x = raw_input('Login<L> or Register<R>?')
if x == 'L':
    getUsrData()
elif x == 'R':
    register()
elif x == 'C':
    os.popen('rm usrData.txt')
    print('usrData CLEARED!')
else: print('wrong')
