#! /usr/bin/env python3
from random import randint

def getPeaks(test):
    if len(test) == 1:
        return [0]
    result = []
    for i in range(len(test)):
        if i > 0 and i < len(test)-1:
            if test[i-1] <= test[i] and test[i] >= test[i+1]:
                result.append(i)
        elif i == 0 and test[i] >= test[i+1]:
            result.append(i)
        elif i == len(test)-1 and test[i-1] <= test[i]:
            result.append(i)
    return result

def getPeakN(test):
    for i in range(1,len(test)):
        if test[i] <= test[i-1]:
            return i-1
    return len(test)-1

def getPeakLogN(test):
    start = 0
    end = len(test)-1
    while(start != end):
        half = (end-start+1)//2
        middle = start + half
        if(middle == start):
            print(start, end, "on the left edge")
        elif(middle == end):
            return middle if test[middle] >= test[middle-1] else middle-1
        else:
            if not test[middle] > test[middle-1]:
                end = middle - 1
            elif not test[middle] > test[middle+1]:
                start = middle + 1
            else:
                return middle
    return start


def binarySearch(test, look):
    start = 0
    end = len(test)-1
    while(start <= end):
        half = (end-start+1)//2
        middle = start + half
        if (test[middle] == look):
            return middle
        if (test[middle] < look):
            start = middle+1
        else:
            end = middle -1
    return -1

testcases = 50
for i in range(testcases):
    test = [ randint(0,50) for i in range(10)]
    results = getPeaks(test)
    a = getPeakN(test)
    b = getPeakLogN(test)
    if(a not in results):
        print("getPeakN error", test, results, a)
    if(b not in results):
        print("getPeakLogN error", test, results, b)
