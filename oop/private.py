#! /usr/bin/env python3
class PrivateProperty:
    def __init__(self):
        self.values = {}
    def __get__(self,instance,type): # readonly property
        pass
    def __set__(self,instance,value):
        pass                        # data descriptor, overide __dict__ when using dot
    def set(self,instance,value):
        self.values[instance] = value
    def get(self,instance):
        return self.values[instance]

class MyClass:
    p1 = PrivateProperty()
    def __init__(self,val):
        # if MyClass.p1 will invoke type.__getattribute__
        MyClass.__dict__['p1'].set(self,val)
    def printPrivateProperty(self):
        return MyClass.__dict__['p1'].get(self)

def debugF (list_of_statements):
    for log in list_of_statements:
        try:
            print(log,":",eval(log))
        except:
            # if not a statment, no output
            exec(log)
            print("statement:",log)

if __name__ == "__main__":
    debugF(["test = MyClass(123)",
    "test.__dict__",
    "test.p1",
    "test.printPrivateProperty()",
    "test.p1 = 456",
    "test.__dict__",
    "test.printPrivateProperty()"])
