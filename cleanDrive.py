 #! /usr/bin/env python3
import os

GigaBytes = 1073741824 # bytes
MegaBytes = 1048576 # bytes
KiloBytes = 1024

# this just shows implementation detail requires no change in the original function
class Bytes:
    def __init__(self, bytes):
        self.bytes = bytes
    def __str__(self):
        GB = self.bytes // GigaBytes
        if GB > 0:
            return str(GB) + " GBs"
        MB = self.bytes // MegaBytes
        if MB > 0:
            return str(MB) + " MBs"
        KB = self.bytes // KiloBytes
        if KB > 0:
            return str(KB) + " KBs"
        return str(self.bytes) +  " bytes"
    def __add__(self, other):
        return Bytes(self.bytes+other.bytes)
    def __lt__(self, other):
        return self.bytes < other.bytes

class Directory:

    def __init__(self, dirName, size = Bytes(0), subDirs = {}, files = {}):
        self.subDirs = subDirs
        self.files = files
        self.dirName = dirName
        self.size = size

    def __str__(self,indent=0):
        spaceIndent = '  '*indent
        fs = ''
        ds = ''
        dKeys = list(self.subDirs.keys())
        fKeys = list(self.files.keys())
        fKeys.sort(key=lambda s: self.files[s].size, reverse=True)
        dKeys.sort(key=lambda s: self.subDirs[s].size, reverse=True)
        for d in dKeys:
            ds += self.subDirs[d].__str__(indent=indent+1)
        for f in fKeys:
            fs += self.files[f].__str__(indent=indent+1) + '\n'
        return spaceIndent + self.dirName + " : " + str(self.size) + "\n" + ds + fs

    def Lvls(self, levels, indent=0):
        if(levels < 0):
            return ''
        spaceIndent = '  '*indent
        ds = ''
        fs = ''
        dKeys = list(self.subDirs.keys())
        dKeys.sort(key=lambda s: self.subDirs[s].size, reverse=True)
        for d in dKeys:
            ds += self.subDirs[d].Lvls(levels -1,indent=indent+1)
        if(levels != 0):
            #directoryOnly
            fKeys = list(self.files.keys())
            fKeys.sort(key=lambda s: self.files[s].size, reverse=True)
            for f in fKeys:
                fs += self.files[f].__str__(indent=indent+1) + '\n'
        return spaceIndent + self.dirName + " : " + str(self.size) + "\n" + ds + fs

class File:

    def __init__(self, dirPath, fileName):
        self.fileName = fileName
        self.fullPath = os.path.join(dirPath,fileName)
        try:
            self.size = Bytes(os.path.getsize(self.fullPath))
        except:
            self.size = Bytes(0)
            print("failed to retrieve " + self.fullPath)

    def __str__(self, indent = 0):
        spaceIndent = '  '*indent
        return spaceIndent + self.fileName + " : " + str(self.size)


# return a tuple
# need subDirs to tell how much to pop()
def createDirectory(dirPath, subDirs, files):
    createdSubDirs = {}
    subDirSize = Bytes(0)
    # for debugging
    # if len(subDirs) > len(globalStack):
    #     print("error too many subDirs", subDirs, globalStack)
    for i in range(len(subDirs)):
        name, sub = globalStack.pop()
        createdSubDirs[name] = sub
        subDirSize += sub.size
    # for debugging
    # for s in subDirs:
    #     if (s not in createdSubDirs):
    #         print("error missing ", s, createdSubDirs, subDirs)
    currentDirFiles = {}
    for f in files:
        newf = File(dirPath, f)
        currentDirFiles[f] = newf
        subDirSize += newf.size

    dirName = dirPath.split("\\")[-1]
    return (dirName, Directory(dirPath, subDirSize, createdSubDirs, currentDirFiles))

drive = "C:\\php"
print("processing \""+drive+"\"")
globalStack = [] # tuple (directoryname, directory object)

for dirPath, subDirs, files in os.walk(drive, topdown=False):
    # topDown=False, is like postorder traversal
    # for d in subDirs...do things
    # then return dirpath
    globalStack.append(createDirectory(dirPath, subDirs, files))

print(globalStack[0][1].Lvls(2))
