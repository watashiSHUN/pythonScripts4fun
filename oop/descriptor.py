#! /usr/bin/env python3
class D:
    def __init__(self, mark):
        self.mark = mark
    def __get__(self, obj, type=None): # must be this signature
        return "descriptor D {0}".format(self.mark)
    def __set__(self,obj,value):
        # object itself is the key
        pass # return nothing, but D is now a data descriptor

class A:
    # class attributes
    d = D("class")
    def __init__(self,a,d):
        self.a = a
        self.d = d # does not invoke descriptor pattern
    def __get__(self, key):
        return "shun fooled you"
    # def __getattribute__(self,name):
    #     return "call getAttribute"
    # if defined, dot operator is going to direct to here
    # called unconditionally
    # override this method will prevent descriptor calls

class FuncOver:
    def fun(self):
        print("class defined function is called")

if __name__ == "__main__":
    x = A("a",D("instance"))
    print(x.a) # not how you use a descriptor
    print(x.d)
    temp = FuncOver()
    temp.fun()
    temp.fun = lambda : print("lambda function is called")
    temp.fun() # different
    print(dir(A))
    def setFun(self, obj, value):
        pass
    type(lambda : print()).__set__ = setFun # falled, builtin can not be monkey patched
    temp.fun()
