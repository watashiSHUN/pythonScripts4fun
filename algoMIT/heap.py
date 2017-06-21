#! /usr/bin/env python3
from random import randint

def heapSort(test):
    for i in range(len(test)//2,-1,-1):
        bubbleDown(test,i)
    # for i in range(len(test)):
    #     insertHeap(test,test[i],i)
    # both method can build a heap
    for i in range(len(test)-1,0,-1):
        # i being the last element
        test[0],test[i] = test[i],test[0]
        bubbleDown(test,length=i) # which stop process at i-1

def bubbleDown(array,parent=None,length=None):
    if(parent is None):
        parent = 0
    if(length is None):
        length = len(array)
    leftchild = 2*parent+1
    rightchild = 2*parent+2
    while True:
        if leftchild < length and rightchild < length:
            l = array[leftchild]
            r = array[rightchild]
            maxChildren = max(l,r)
            if array[parent] < maxChildren:
                if maxChildren == l:
                    array[parent],array[leftchild],parent = array[leftchild],array[parent],leftchild
                else:
                    array[parent],array[rightchild],parent= array[rightchild],array[parent],rightchild
                leftchild = 2*parent+1
                rightchild = leftchild+1
            else:
                break
        elif leftchild < length:
            if array[parent] < array[leftchild]:
                array[parent],array[leftchild] = array[leftchild],array[parent]
            break
        else:
            break
    return

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
        print(test)
        print("heapSort failed")
