#https://www.hackerrank.com/challenges/building-a-list

for _ in range(int(input())):
    n = int(input())
    count = 2**n-1 # size of a powerset, does not print the emptyset
    string = list(input())
    string.sort() # alphabetical order
    dictionary = {} # unique letters, each letter correspond to its index
    for index,value in enumerate(string):
        dictionary[value] = index
    previousOutput = list(string[0])

    while count != 1:
        count -= 1
        print("".join(previousOutput))
        # produce next based on previous
        lastLetterIndexInPrevious = dictionary[previousOutput[-1]]
        if  lastLetterIndexInPrevious != n-1:
            # append next available letter
            previousOutput.append(string[lastLetterIndexInPrevious+1])
        else:
            del previousOutput[-1]
            lastNonEndLetterIndex = dictionary[previousOutput[-1]]
            previousOutput[-1] = string[lastNonEndLetterIndex+1]

    print(string[-1])


# test to write nested for loops
testIn = "abcde"
n = len(testIn)
for i in range(n):
    # always represent the first letter in the output
    print(testIn[i])
    for j in range(i+1,n):
        print(testIn[i],testIn[j],sep="")
        for k in range(j+1,n):
            print(testIn[i],testIn[j],testIn[k],sep="")
            for l in range(k+1,n):
                print(testIn[i],testIn[j],testIn[k],testIn[l],sep="")
                for m in range(l+1,n):
                    print(testIn[i],testIn[j],testIn[k],testIn[l],testIn[m],sep="")
