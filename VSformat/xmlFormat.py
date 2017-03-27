# although I can try to change it in notepad++, but in case I run into this issue again
# write a script is a long term investment
import re
regex = re.compile('[^ ]/>')

# define a helper function that read a xml file
def helper(fileName):
    newLines = []
    changes = False;
    with open(fileName,'r') as f: # both reading and writing
        lines = f.readlines() # equivalent of list(f)
        for i,line in enumerate(lines):
            newLine = replace(line)
            if newLine:
                changes = True
                print(i,line,end='')
                newLines.append(newLine)
            else:
                newLines.append(line) # no change
    # write to file
    # instead, use truncate, cut till the current f.tell()
    if changes:
        with open(fileName,'w') as f:
            f.writelines(newLines)

def addSpace(matchObj):
    # print("called")
    matchStr = matchObj.group(0)
    newStr = matchStr[0] + " " + matchStr[1:]
    return newStr

def replace(s):
    if regex.search(s):
        return regex.sub(addSpace,s)
    return None

if __name__ == "__main__":
    # helper("test.xml") # does not work in atom runner....
    temp = "123 />456\"/>789/>" # first replace, second not replace
    print(temp)
    print(replace(temp))
    # unit test
    helper("test.xml")
