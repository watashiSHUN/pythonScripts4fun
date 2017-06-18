from random import randint

def shunRange(start, end, step):
    current = start
    while(current > end):
        yield current
        current += step

# print(reversed(shunRange(5,-1,-1))) failed
print(reversed(range(5))) # class listreverseiterator

# use O(n) extra space
# if you copy left and right, the divide is not constant time
def mergeSort(test):
    temp = [0]*(len(test)*2)
    mergeSortRapper(test,0,len(test)-1,temp)
# rewrite mergeSort() only does divide

def mergeSortRapper(test,start,end, temp):
    # determine when to stop divide
    if start >= end:
        return # already sorted
    half = (end-start)//2
    middle = start+half
    mergeSortRapper(test,start,middle, temp)
    mergeSortRapper(test,middle+1,end, temp)
    merge(test,start,half+1,middle+1,end-middle,temp)

# merge only does merge
def merge(test,a,lenA,b,lenB,temp):
    b1 = 0 # buffers
    b2 = len(test)
    # copy before merge
    for i in range(lenA):
        temp[b1+i] = test[a+i]
    for j in range(lenB):
        temp[b2+j] = test[b+j]
    x,y,z = 0,0,0
    while x < lenA and y < lenB:
        if(temp[b1+x] < temp[b2+y]):
            test[a+z] = temp[b1+x]
            x+=1
        else:
            test[a+z] = temp[b2+y]
            y+=1
        z += 1
    while x < lenA:
        test[a+z] = temp[b1+x]
        x+=1
        z+=1
    while y < lenB:
        test[a+z] = temp[b2+y]
        y+=1
        z+=1

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
