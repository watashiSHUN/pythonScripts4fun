 #! /usr/bin/env python3
import sys,os
from zipfile import ZipFile
print(sys.argv)
zipA = sys.arg[1]
zipB = sys.argv[2]

newZip = "new.zip"
returnV = []
with ZipFile(newZip,'w') as out:
    with ZipFile(zipA,'r') as zA:
        with ZipFile(zipB,'r') as zB:
            fds = set(zB.namelist())
            for fd in zA.namelist():
                if not fd.endswith('/'):
                    if fd in fds:
                        returnV.append(fd)
                    else:
                        out.writestr(fd,zA.read(fd))
                        # write fd to another zip file
returnCount = 0
for fd in returnV:
    # for zip file in fd is /, no matter which os it is running on
    print(fd)
    returnCount += 1
print('overlaps',returnCount)
