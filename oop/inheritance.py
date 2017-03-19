#! /usr/bin/env python3
class A:
    def m(self):
        print("method A")
    pass
class B(A):
    pass

if __name__ == "__main__":
    b = B()
    print(b.__class__)
    print(type(B))
    print(type(type(B)))
    print(type(b))
    print(dir(b)) # same as dir(B)
    print(dir(B))
    # dir in python2 does not print __class__ __dict__ etc
    print(b.__dict__) # instance attribute
    print(B.__dict__) # class attribute
