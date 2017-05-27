#! /usr/bin/env python3

def identityM(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]

print(identityM(3))
