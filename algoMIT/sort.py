 #! /usr/bin/python3
from random import randint

def mergeSort(test):
    if len(test) == 2:
        if(test[0] > test[1]):
            temp = test[0]
            test[0] = test[1]
            test[1] = temp
        return test
    elif len(test) <= 1:
        return test
    middle = len(test)//2
    left = []
    for i in range(middle):
        left.append(test[i])
    right = []
    for i in range(middle,len(test)):
        right.append(test[i])
    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)
    merge(sortedLeft, sortedRight, test)
    return test

def merge(a,b,dest):
    i = j = 0
    for c in range(len(dest)):
        if i >= len(a):
            dest[c] = b[j]
            j += 1
        elif j >= len(b):
            dest[c] = a[i]
            i += 1
        elif a[i] <= b[j]:
            dest[c] = a[i]
            i += 1
        else:
            dest[c] = b[j]
            j += 1


def insertOne(test, index, number):
    test.append(0)
    for i in reversed(range(index+1,len(test))):
        test[i] = test[i-1]
    test[index] = number

def binaryInsertion(test, number):
    # test is a sorted list
    start = 0
    end = len(test)-1
    returnIndex = 0
    while(start <= end):
        half = (end-start+1)//2
        middle = start+half
        if(test[middle] == number):
            return middle+1
        elif(number < test[middle]):
            end = middle - 1
            returnIndex = middle # if smaller, should replace the currentNode
                                 # depends on how your insertion algorithm is implemented
        else:
            start = middle + 1
            returnIndex = start
    return returnIndex

def insertionSortInPlace(test):
    for i in range(1,len(test)):
        # test[0], single element of sorted list
        for j in reversed(range(i)):
            if test[j] > test[j+1]:
                # swap
                temp = test[j]
                test[j] = test[j+1]
                test[j+1] = temp
            else:
                break

def bubbleSortInPlace(test):
    for i in reversed(range(len(test))):
        maxNum = test[0]
        maxIndex = 0
        for j in range(1,i+1):
            if test[j] > maxNum:
                maxNum = test[j]
                maxIndex = j
        temp = test[i]
        test[i] = maxNum
        test[maxIndex] = temp

def isSorted(test):
    for i in range(1,len(test)):
        if test[i-1] > test[i]:
            return False
    return True

testcases = 50
for i in range(testcases):
    test = [ randint(0,50) for i in range(10)]
    bubbleSortInPlace(test)
    if not isSorted(test):
        print("bubbleSortInPlace failed")
    test = [ randint(0,50) for i in range(10)]
    insertionSortInPlace(test)
    if not isSorted(test):
        print("insertionSortInPlace failed")
    insertNumber = randint(0,50)
    insertOne(test,binaryInsertion(test,insertNumber),insertNumber)
    if not isSorted(test):
        print("binaryInsertion failed")
    test = [ randint(0,50) for i in range(10)]
    mergeSort(test)
    if not isSorted(test):
        print("mergeSort failed")
