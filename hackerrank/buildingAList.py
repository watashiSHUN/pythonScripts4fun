#https://www.hackerrank.com/challenges/building-a-list

for _ in range(int(input())):
    n = int(input())
    string = list(input())
    string.sort() # alphabetical order
    lastLetter = string[-1] # all unique
    lastLetterIndexInPrevious = 0
    init = [0]*n
    init[0] = 1
    previousIndex = init
    previousOutput = list(string[0])

    while not (len(previousOutput) == 1 and previousOutput[0] == lastLetter):
        print("".join(previousOutput))
        # produce next based on previous
        if lastLetterIndexInPrevious != (n-1):
            # append next available letter
            lastLetterIndexInPrevious += 1
            previousOutput.append(string[lastLetterIndexInPrevious])
            previousIndex[lastLetterIndexInPrevious] = 1
        else:
            # goes back and find the last no zero index, replace it with zero and move it back by 1
            previousIndex[-1] = 0
            del previousOutput[-1]
            for i in range(1,n):
                inspectIndex = lastLetterIndexInPrevious-i; # lastLetterIndexInPrevious == n-1
                if previousIndex[inspectIndex]:
                    lastLetterIndexInPrevious = inspectIndex+1
                    previousIndex[inspectIndex] = 0
                    previousIndex[lastLetterIndexInPrevious] = 1
                    del previousOutput[-1]
                    previousOutput.append(string[lastLetterIndexInPrevious])
                    break

    print(string[-1])
