# https://www.hackerrank.com/challenges/coinage
def helper(denomination,number,beforeList):
    sumList = [0]*len(beforeList)
    for i in range(1,number+1):
        startIndex = i*denomination
        for j in range(len(beforeList)-startIndex):#move the list to the right by "startIndex"
            sumList[j+startIndex] += beforeList[j]
    for i in range(len(beforeList)):
        beforeList[i] += sumList[i]
# use integer addition
# but that means result is 0 to 9
for _ in range(1):
    n = 26
    one,two,five,ten = 28, 33, 10, 8
    initList = [0]*(n+1)
    initList[0] = 1
    helper(1,one,initList)
    helper(2,two,initList)
    helper(5,five,initList)
    helper(10,ten,initList)
    print(initList[-1])
