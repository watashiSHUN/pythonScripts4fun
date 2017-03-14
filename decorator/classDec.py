class swallow:
    '''takes two arguments
        1. exception type that we want to catch inside the decorator
        2. returnType for these caught exceptions
    '''
    def __init__(self, exceptions = BaseException, default = None):
        "construct a callable in place"
        self.exceptions = exceptions
        self.default = default

    def __call__(self, func):
        "since @ takes a callable that has only 1 argument"
        # return a function
        def helper(*args):
            try:
                return func(*args)
            except self.exceptions:
                # except take a single exception/ a tuple
                return self.default
                raise
        return helper

if __name__ == "__main__":
    # test
    @swallow(exceptions=ZeroDivisionError,default=0)
    def divide(divident = 0, divisor = 1):
        return divident/divisor
    print(divide(1,0))
    print(divide("helloworld"))
