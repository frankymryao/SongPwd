#! /usr/bin/python
from getchar import *
from datetime import *
from math import pow
from string import *

def getPwd():
    isInPwd = False
    timeRecord = []
    timeInterval = []
    initTime = datetime.now()
    intervalCount = 0

    while True:
        currentChar = getchar()
        print('got ' + currentChar)
        timeRecord.append((datetime.now() - initTime))
        intervalCount = intervalCount + 1
        if '#' == currentChar:
            if False == isInPwd:
                isInPwd = True
            else:
                break

    intervalCount = intervalCount - 2
    for i in range(1, len(timeRecord) - 2):
        timeDelta = timeRecord[i + 1] - timeRecord[i]
        timeInterval.append(timeDelta.seconds*pow(10, 7) + timeDelta.microseconds)

    return(timeInterval, intervalCount)
    #timeInterval = [123, 333, ...]

def getUsrData(fileName):
    usrDict = {}
    file_object = open(fileName)
    try:
        data = file_object.readlines()
        for i in range(0, len(data)):
            usrName, usrData = data[i].split('|')
            usrDict.setdefault(usrName, usrData.replace('\n', ''))
    finally:
        file_object.close()
    return(usrDict)
'''
{'solo': '14#654977.0#400487.0#400797.0#401637.0#400527.0#400635.0#400291.0#400379.0#400388.0#400365.0#400567.0#401152.0#400395.0$',
'franky': '11#401532.0#401186.0#400508.0#400604.0#491071.0#400425.0#400540.0#400599.0#455916.0#617675.0$'}
'''

def map2pwd(mapData):
    temp = mapData.replace('$', '').split('#')
    for i in range(0, len(temp)):
        temp[i] = atof(temp[i])
    return(temp[0], temp[1:len(temp)])

def getCmpPwd(fileName):
    usrMap = getUsrData(fileName)
    file_object = open(fileName)
    data = file_object.readline().split('|')
    name = data[0]
    pwd = usrMap.get(name)
    pwd = map2pwd(pwd)
    pwd = pwd[1:len(pwd)]
    file_object.close()
    return(pwd[0])

    

def register():
    usrName = raw_input('your name: ')
    print('your pwd, start and end with \'#\'')
    usrPwd, usrCount = getPwd()
    putPwd('usrData', usrName, usrCount, usrPwd)
   
def putPwd(fileName, usrName, usrCount, usrPwd):
    file_object = open(fileName, 'ab')
    file_object.write(usrName + '|' + str(usrCount) + '#')
    for i in range(0, len(usrPwd) - 1):
        file_object.write(str(usrPwd[i]) + '#')
    file_object.write(str(usrPwd[len(usrPwd) - 1]) + '$')
    file_object.write('\n')
    file_object.close()


if __name__ == '__main__':
    getUsrData('usrData')
    
