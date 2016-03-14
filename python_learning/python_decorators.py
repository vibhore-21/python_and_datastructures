'''
FUNCITON DECORATORS:
Understanding the orrder of '@<decorator>' resolution order by a simple example

'''
def deco1(func):
    def inner(*args, **kwargs):
        print 'deco1: arguments are {0}, {1}'.format( args, kwargs)
        return func(*args, **kwargs)
    return inner

def deco2(func):
    def inner(*args, **kwargs):
        print 'deco2: this is decorator 2'
        return func(*args, **kwargs)
    return inner


@deco1
@deco2
def foo(a,b):
    return a +b

'''
Note "@<decorator name>" is just a syntactic sugar for "foo = decorator(foo)"
'''

def foo2(a,b):
    return a*b

if __name__=='__main__':
    print foo(3,4)

    '''
    decorator order on foo is equivalent same as decorator order for foo2 defined below
    '''
    foo2 = deco2(foo2)
    foo2 = deco1(foo2)
    print foo2(3,4)



