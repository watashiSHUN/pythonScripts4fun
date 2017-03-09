size1 = 8388608
name1 = 'ManualTriggerCSharp1.dat'
f = open('C:\\Users\\shucai\\Desktop\\'+name1,'w')
for i in range(size1):
    f.write('1') # ascii, each char is a byte
f.close()

size2 = 8300000
name2 = 'ManualTriggerCSharp2.dat'
f = open('C:\\Users\\shucai\\Desktop\\'+name2,'w')
for i in range(size2):
    f.write('1') # ascii, each char is a byte
f.close()
