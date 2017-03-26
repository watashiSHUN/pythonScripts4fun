# although I can try to change it in notepad++, but in case I run into this issue again
# write a script is a long term investment
extraSpace = " />"
normal = "/>"
extraSpaceLength = 3
# define a helper function that read a xml file
def helper(fileName):
    newLines = []
    with open(fileName,'r') as f: # both reading and writing
        lines = f.readlines() # equivalent of list(f)
        for line in lines:
            newLines.append(replace(line))
    #write to file
    # instead, use truncate, cut till the current f.tell()
    with open(fileName,'w') as f:
        f.writelines(newLines)

def replace(s): #TODO use re.sub(a,b,lines)
    index = s.find(extraSpace)
    if index == -1:
        return s
    return s[:index] + normal + replace(s[index+extraSpaceLength:])
    # recursive?

if __name__ == "__main__":
    helper("C:\\Users\\shucai\\Desktop\\test.xml")
    # temp = "123 />456 /> 789//>"
    # print(temp)
    # print(replace(temp))
    # unit test
