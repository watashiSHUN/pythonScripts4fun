 #! usr/env/python3
def memoization(recursion):
    d = {}
    def wrapper(*args):
        # use args tuple nature
        if args not in d:
            result = recursion(*args)
            # convert tuple back to argument List
            d[args] = result
        return d[args]
    return wrapper

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@memoization
def dp(n):
    if n < 2:
        return 1
    else:
        return dp(n-1) + dp(n-2)

import time
def test(function, *args):
    t1 = time.time()
    result = function(*args)
    t2 = time.time()
    print(function.func_name+str(args)+" = "+str(result))
    print("runtime = " + str(t2-t1) + "s")

test(fibonacci, 40)
test(dp,40)
# fibonacci(40,) = 165580141
# runtime = 34.3965408802s
# wrapper(40,) = 165580141
# runtime = 0.000146150588989s
