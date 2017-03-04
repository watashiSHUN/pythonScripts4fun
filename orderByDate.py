#! /usr/bin/env python3
import os
parentDir = '/home/watashishun/Desktop/MIT6.046JF05MPEG4'
fileNames = os.listdir(parentDir)

#ocw-6.046-21sep2005-220k.mp4
dic = {'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06','jul':'07','aug':'08','sep':'09','oct':'10','nov':'11','dec':'12'}

def generateNum(string):
    date = string.split('-')[2] #21sep2005
    day = date[:2]
    month = dic[date[2:5]]
    year = date[-4:]
    return year+month+date

fileNames.sort(key=generateNum)
print(fileNames)

for name in fileNames:
    os.rename(parentDir+os.sep + name,parentDir+os.sep+generateNum(name)+'.mp4')
