class CountList:
    listToTestAddr = [] #static var
    def __init__(self):
        print(self.listToTestAddr is self.__class__.listToTestAddr)
        self.listToTestAddr += [1] # self.count will try to define a instance var
        print(self.listToTestAddr is self.__class__.listToTestAddr)

class Count:
    count = 0
    l = []
    def __init__(self):
        print("init",locals()) # does not have access to count
        # can only access self, then self.class.count
        self.count += 1 # getitem and setitem is implemented differently
        # setitem is always immediate, getitem use the inheritance tree
        self.l.append(1)

def countFun():
    count = 0
    l = []
    def inner():
        print("inner",locals()) #locals does not have count
        l.append(1)
        count + 1
        # count += 1 # error
        # python intepreter read inner function
        # if it finds out +=, the variable is thus no longer added
        # to the locals
    print(inner.__code__)
    inner()

if __name__ == "__main__":
    def abc():
        pass
    print(locals())
    temp = CountList()
    print(CountList.listToTestAddr)
    print(temp.listToTestAddr)
    temp2 = Count() # not error?
    print(temp2.count, temp2.l)
    print(Count.count, temp2.l)
    countFun()
    # temp2.abc += 1
    # print(temp2.abc)
