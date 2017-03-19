#! /usr/bin/env python3
import types

class override:
    "any instance will evaluate to false in a conditional statement"
    b = "attribute in class" # will not be accessible, b(self) shadow
    def __bool__(self):
        return False # only works in python3
    def b(self):
        print("function in class")

if __name__ == "__main__":
    temp = override() # system created a dictionary for you
    print("true" if temp else "false")
    def a():
        print("funcion in instance")
    temp.b = a
    print(temp.b)
    print(temp.__class__.b)
    a = 1 # everything in python is an object
#    a.bla = "bla"
    print(override.__class__.__getattribute__(override,'b'))
