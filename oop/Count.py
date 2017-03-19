class Count:
    listToTestAddr = [] #static var
    def __init__(self):
        print(self.listToTestAddr is self.__class__.listToTestAddr)
        self.listToTestAddr += [1] # self.count will try to define a instance var
        print(self.listToTestAddr is self.__class__.listToTestAddr)

if __name__ == "__main__":
    temp = Count()
    print(Count.listToTestAddr)
    print(temp.listToTestAddr)
