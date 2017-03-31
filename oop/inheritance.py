#! python3
def printAttributes(instance):
    for aStr in dir(instance):
        att = getattr(instance,aStr)
        if not callable(att):
            print(aStr,att)

class A:
    b = 456
    def m(self):
        print("method A")
    pass
class B(A):
    pass
# XXX dir return method you can call on the object
# but when you call a.x()
# python change it to type(a).__dict__[x]()
if __name__ == "__main__":
    a = A()
    a.c = 123 # a.__dict__['abc'] = 123
    print(A.__dict__) # class type (instance of type) has their own attributes
    print(a.__dict__) # if object has .__dict__, dynamically add attributes
    print(dir(a))
    print(dir(A))
    # not all classes have __dict__
    try:
        print([].__dict__)
    except:
        print("list has no __dict__")
    print(type(a).__dict__['m'])
    print(a.m) #bound
    b = B()
    print(type(B)) # meta classes
    print(type(type(B)))
    print(dir(A))
    print(dir(b)) # dir takes care of inheritance
    # dir in python2 does not print __class__ __dict__ special attributes
    # because they don't have? A.__class__ failed on 2.7.12
    print(A.__dict__)
    print(type(A).__dict__) # special
    printAttributes(A)
