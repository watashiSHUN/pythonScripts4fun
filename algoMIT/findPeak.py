#! /usr/bin/env python3

def getPeak(test):
    for i in range(1,len(test)):
        if test[i] <= test[i-1]:
            return i-1
    return len(test)-1

print(getPeak([1,2,3,4,5,2]))
