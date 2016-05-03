__author__ = 'james'

def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr

test = counter(5)
print test()

print test()

print test()

test2 = counter(100)
print test2()
print test2()
print test2()