string = input()
subString = input()
lenSub = len(subString)
lenString = len(string)
returnV = 0
for x in range(lenString):
    xPrime = x
    for y in range(lenSub):
        if xPrime >= lenString or subString[y] != string[xPrime]:
            break
        xPrime += 1
    if xPrime-x == lenSub:
        returnV += 1
print(returnV)
