#! /usr/bin/env python3
class PrivateProperty:
    def __init__(self):
        self.values = {}
    def __get__(self,instance,tmp): # readonly property
        pass
    def set(self,instance,value):
        self.values[instance] = value
    def get(self,instance):
        return self.values[instance]


class MyClass:
    p1 = PrivateProperty()
    def __init__(self,val):
        MyClass.__dict__['p1'].set(self,val)
    def printPrivateProperty(self):
        print(MyClass.__dict__['p1'].get(self))

if __name__ == "__main__":
    test = MyClass(123)
    print(test.__dict__) # {} since we store data with class not with instance
    print(test.p1) # None __get__ method of descriptor is invoked
    test.printPrivateProperty() # 123
    test.p1 = 456  # __set__ method of descriptor is invoked
    print(test.p1)
    test.printPrivateProperty()
    print(MyClass.__dict__['p1'])
