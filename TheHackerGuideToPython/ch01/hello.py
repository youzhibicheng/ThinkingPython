def hello():
    """
    This is the DOC for hello
    """
        print 'hello world'


def hello2(name):
    """
    this is the DOC for hello2
    """
    print "hello world %s" % name


if __name__ == '__main__':
    """
    This is the DOC for the hello module main
    """
    hello()
    hello2('James')
