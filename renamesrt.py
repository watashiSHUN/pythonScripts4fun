#! /usr/bin/env python3
"""
    rename subtitle files downloaded with cousera's videao
    from suffix '.en.srt' ==> '.srt' so the video play loads
    it automatically
"""
from os import walk,rename
from os.path import join
import sys
for dirpath,dirnames,filenames in walk('/home/watashishun/Desktop/principles-of-computing-2'):
    for f in filenames:
        if f.endswith('.en.srt'):
            src = join(dirpath,f)
            dest = join(dirpath,f.replace('.en.srt','.srt'))
            rename(src,dest)
