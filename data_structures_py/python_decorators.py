def deco1(func):
    def inner(*args, **kwargs):
        print 'deco1: arguments are {0}, {1}'.format( args, kwargs)
        return func(*args, **kwargs)
    return inner

def doco2(*args, **kwargs):
    def inner(*args, **kwargs):
        print 'deco2: this is decorator 2'
        return func(*args, **kwargs)
    return inner


@deco1
@deco2
def foo(a,b):
    return a +b

if __name__=='__main__':
    foo(3,4)



