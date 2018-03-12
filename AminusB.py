 #! /usr/bin/env python3
import sys,os
from zipfile import ZipFile
import zipfile
zipA = sys.argv[1]
zipBs = sys.argv[2] # this is a folder

union_set = set()
for f in os.listdir(zipBs):
    f_full = os.path.join(zipBs,f)
    if zipfile.is_zipfile(f_full):
        with ZipFile(f_full,'r') as zipf:
            union_set.update(set(zipf.namelist()))

zipfileCommon = None
zipfileDiff = None
with ZipFile(zipA,'r') as zA:
    fdsA = zA.namelist()
    for fd in fdsA:
        if not fd.endswith('/'): #zip standard
            if fd in union_set:
                print("find common" + fd)
                if not zipfileCommon:
                    zipfileCommon = ZipFile("common.zip",'w')
                zipfileCommon.writestr(fd,zA.read(fd))
            else:
                if not zipfileDiff:
                    zipfileDiff = ZipFile("difference.zip",'w')
                zipfileDiff.writestr(fd,zA.read(fd))

if zipfileCommon:
    zipfileCommon.close()
if zipfileDiff:
    zipfileDiff.close()
