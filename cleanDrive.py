 #! /usr/bin/env python3
import os

class Tree:
    def __init__(self, directory):
        self.root = Directory(directory)
        self.prefix = directory
        self.prefixL = len(directory.split(os.sep))

    def __str__(self):
        return str(self.root)

    def printDirs(self, levels=100):
        print(self.root.dirsOnly(levels))

    def addSubDir(self,dirPath,fileList):
        currentDir = self.root
        dirPathSep = dirPath.split(os.sep)
        dirName = dirPathSep[-1]
        # create a directory object for this subdir
        finalDir = Directory(os.sep + dirName)
        for f in fileList:
            temp = File(dirPath,f)
            finalDir.files[f] = temp
            finalDir.sizeIncrease(temp.size)
        # update the tree

        if (len(dirPathSep) > self.prefixL):
            middle = dirPathSep[self.prefixL:-1]
            for d in middle:
                if d not in currentDir.subDirs:
                    currentDir.subDirs[d] = Directory(os.sep + d)
                    # print(currentDir.subDirs, currentDir.dirName)
                destDir = currentDir.subDirs[d]
                currentDir.sizeIncrease(finalDir.size)
                currentDir = destDir
            # last one is special, if its the end, assign else update files
            if dirName not in currentDir.subDirs:
                currentDir.subDirs[dirName] = finalDir
            else:
                currentDir.subDirs[dirName].files = finalDir.files
            currentDir.sizeIncrease(finalDir.size)
        else:
            currentDir.files = finalDir.files
            currentDir.sizeIncrease(finalDir.size)

class Directory:
    def __init__(self, dirName, size = 0):
        self.subDirs = {} # list of directory objects
        self.files = {} # list of file object
        self.dirName = dirName
        self.size = size
    def sizeIncrease(self, increase):
        self.size += increase
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
        return spaceIndent + self.dirName + " : " + str(self.size) + " bytes\n" + ds + fs

    def dirsOnly(self, levels, indent=0):
        if(levels < 0):
            return ''
        spaceIndent = '  '*indent
        ds = ''
        dKeys = list(self.subDirs.keys())
        dKeys.sort(key=lambda s: self.subDirs[s].size, reverse=True)
        for d in dKeys:
            ds += self.subDirs[d].dirsOnly(levels -1,indent=indent+1)
        return spaceIndent + self.dirName + " : " + str(self.size) + " bytes\n" + ds


class File:
    def __init__(self, dirPath, fileName):
        self.fileName = fileName
        self.fullPath = os.path.join(dirPath,fileName)
        try:
            self.size = os.path.getsize(self.fullPath)
        except:
            self.size = 0
            print("failed to retrieve " + self.fullPath)
    def __str__(self, indent = 0):
        spaceIndent = '  '*indent
        return spaceIndent + self.fileName + " : " + str(self.size) + " bytes"

drive = "C:\\Users\\shucai\\Downloads"
t = Tree(drive)

for dirPath, subDirs, files in os.walk(drive, topdown=False): # topdown deal with root at the end
    #print(dirPath, subDirs, files)
    t.addSubDir(dirPath,files)
# print(t)
t.printDirs(1)
