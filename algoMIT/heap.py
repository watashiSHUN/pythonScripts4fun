#! /usr/bin/env python3
from random import randint

def heapSort(test):
    for i in range(len(test)):
        insertHeap(test,test[i],i)
    for i in range(len(test)-1,-1,-1):
        test[i] = extractHeap(test,i)

def extractHeap(array,last=None):
    if last is None:
        last = len(array)-1
    returnV = array[0]
    array[0] = array[last]
    # bubble down
    parent = 0
    leftchild = 2*parent+1
    rightchild = leftchild+1
    while True:
        if leftchild < last and rightchild < last:
            if array[parent] < array[leftchild] or array[parent] < array[rightchild]:
                if array[leftchild] > array[rightchild]:
                    array[leftchild],array[parent] = array[parent],array[leftchild]
                    parent = leftchild
                else:
                    array[rightchild],array[parent] = array[parent],array[rightchild]
                    parent = rightchild
                leftchild = parent*2+1
                rightchild = leftchild+1
            else:
                break
        elif leftchild < last:
            if array[parent] < array[leftchild]:
                array[parent],array[leftchild] = array[leftchild],array[parent]
            break
        else:
            break
    return returnV


def insertHeap(array,elem,last=None):
    if last is None:
        last = len(array)
        array.append(elem)
    # else assume the last is the new element
    child = last
    parent = (child-1)//2 # -1//2 = -1
    while(parent >= 0 and array[parent] < array[child]):
        array[child], array[parent] = array[parent],array[child]
        child = parent
        parent = (parent-1)//2

def isSorted(test):
    for i in range(1,len(test)):
        if test[i-1] > test[i]:
            return False
    return True

testcases = 50
for i in range(testcases):
    test = [randint(0,50) for x in range(10)]
    heapSort(test)
    if not isSorted(test):
        print("heapSort failed")
