 #! /usr/bin/env python3
import sys,os
from zipfile import ZipFile
zipA = sys.argv[1]
zipB = sys.argv[2]

with ZipFile(zipA,'r') as zA:
    fdsA = zA.namelist()
    with ZipFile(zipB,'r') as zB:
        fdsB = set(zB.namelist())
        with ZipFile("difference.zip",'w') as difference:
            with ZipFile("common.zip",'w') as common:
                for fd in fdsA:
                    if not fd.endswith('/'): #zip standard 
                        if fd in fdsB:
                            common.writestr(fd,zA.read(fd))
                        else:
                            difference.writestr(fd,zA.read(fd))
