__author__ = 'james'

def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

test = counter(1)
print test.next()
print test.next()
print test.next()
print test.send(10)
print test.next()
print test.next()
print test.next()

test2 = counter(None)
print test2.next()
print test2.next()
print test2.next()