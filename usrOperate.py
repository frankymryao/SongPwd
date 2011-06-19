from getchar import *
from datetime import *
from math import pow

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
    for i in range(1, len(timeRecord) - 1):
        timeDelta = timeRecord[i + 1] - timeRecord[i]
        timeInterval.append([i, timeDelta.seconds*pow(10, 7) + timeDelta.microseconds])

    return(timeInterval, intervalCount)

def register():
    usrName = raw_input('your name: ')
    print('your pwd, start and end with \'#\'')
    usrPwd, count = getPwd()
    file_object = open('usrData.txt', 'ab')
    file_object.write(usrName + '#' + str(count) + '#')
    for i in range(0, len(usrPwd)):
        file_object.write(str(usrPwd[i][1]) + '#')
    file_object.write('\n')
    file_object.close()

def login():
    usrName = raw_input('your login name: ')

    
