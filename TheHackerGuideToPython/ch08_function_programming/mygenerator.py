import inspect

def mygenerator():
    yield 1
    yield 2
    yield 3

g=mygenerator()
print g.next()
print next(g)
print next(g)

print inspect.isgeneratorfunction(g)
print inspect.isgeneratorfunction(mygenerator)
