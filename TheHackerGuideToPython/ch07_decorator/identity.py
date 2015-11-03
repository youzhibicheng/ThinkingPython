def identity(f):
    print 'identity'
    return f

@identity
def foo():
    print 'foo'
    return 'bar'

foo()
