 #! /usr/bin/env python3
import sys,os
from zipfile import ZipFile
zipA = sys.argv[1]
zipB = sys.argv[2]

newZip = "new.zip"

with ZipFile(zipA,'r') as zA:
    fdsA = set(zA.namelist())
    with ZipFile(zipB,'r') as zB:
        fdsB = set(zB.namelist())
        with ZipFile(newZip,'w') as out:
            for fd in fdsA.difference(fdsB):
                if not fd.endswith('/'): # use to determine files, zip standard
                    out.writestr(fd,zA.read(fd))
