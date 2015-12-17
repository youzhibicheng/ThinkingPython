# coding=utf-8


def original_func():
    print 'this is original function!'


def modified_func():
    print 'this is modified function!'


def main():
    original_func()

if __name__ == '__main__':
    original_func = modified_func
    main()
