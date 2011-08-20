#! /usr/bin/python
import random
import time
import math
import os
import sys

_DEBUG = True
class pwdGenerator:
       
    def __init__(self):
        random.seed(time.time())

    def singlePwdGen(self, pwdSeq):
        index = int(random.uniform(0, len(pwdSeq)))
        return pwdSeq[index]

    def generator(self, pwdSeq, length):
        pwdStr = ''
        pwd = ''
        for i in range(0, length):
            pwd = self.singlePwdGen(pwdSeq)
            pwdStr += pwd
        return pwdStr

class pwdIterator:
    __pwdStr = ''
    __currentPwd = ''
    __seq_length = 0
    __pwd_length = 0
    __pwdSeq = ''
    __index = -1

    def __init__(self, pwdSeq, pwdStr):
        self.__pwdStr = pwdStr
        self.__pwdSeq = pwdSeq
        self.__seq_length = len(pwdSeq)
        self.__pwd_length = len(pwdStr)
        self.__currentPwd = pwdSeq[0] * self.__pwd_length

       
    def findIndex(self, letter):
        for index in range(0, self.__seq_length - 1):
            if letter == self.__pwdSeq[index]:
                return index
        return -1

    def testSeq(self):
        while True:
            if self.__currentPwd == (self.__pwdSeq[-1] * self.__pwd_length):
                raise StopIteration

            if self.__currentPwd[self.__index] == self.__pwdSeq[-1]:
                while self.__currentPwd[self.__index] == self.__pwdSeq[-1]:
                    self.__index -= 1

                first = self.__currentPwd[0:self.__index]
                middle = self.__pwdSeq[self.findIndex(self.__currentPwd[self.__index]) + 1]
                last = self.__pwdSeq[0] * (abs(self.__index) - 1)
                self.__currentPwd = first + middle + last
                self.__index = -1
                yield self.__currentPwd
            else:
                first= self.__currentPwd[0:self.__index]
                last = self.__pwdSeq[0] * (abs(self.__index) - 1)
                middle = self.__pwdSeq[self.findIndex(self.__currentPwd[self.__index]) + 1]
                self.__currentPwd = first + middle + last
                yield self.__currentPwd
        
    
def forceBoom(pwdStr, pwdSeq):
    print 'Pwd: ' + pwdStr
    length = len(pwdStr)
    PwdIter = pwdIterator(pwdSeq, pwdStr)
    testSeq = PwdIter.testSeq()
    while True:
        testPwd = testSeq.next()
        print testPwd
        if testPwd == pwdStr:
            print 'FOUND IT'
            break

if __name__ == '__main__':
    number = '0123456789'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mix = number + alphabet
    pwdGen = pwdGenerator()
    seq_type = sys.argv[1]
    length = int(sys.argv[2])
    if seq_type == 'number':
        pwdStr = pwdGen.generator(number, length)
        startTime = time.time()
        forceBoom(pwdStr, number)
        endTime = time.time()
    elif seq_type == 'alphabet':
        pwdStr = pwdGen.generator(alphabet, length)
        startTime = time.time()
        forceBoom(pwdStr, alphabet)
        endTime = time.time()
    elif seq_type == 'mix':
        pwdStr = pwdGen.generator(mix, length)
        startTime = time.time()
        forceBoom(pwdStr, mix)
        endTime = time.time()

    duration = round(endTime - startTime, 4)
    print 'Time Used: ' + str(duration)
    file_object = open('forceBoomData', 'ab')
    file_object.write('PASSWORD: ' + pwdStr + '\n' + 'LENGTH: ' + str(length) + '\n' + 'Duration: ' + str(duration) + 's')
    file_object.write('\n' * 2)
    file_object.close()
