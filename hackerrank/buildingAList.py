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
