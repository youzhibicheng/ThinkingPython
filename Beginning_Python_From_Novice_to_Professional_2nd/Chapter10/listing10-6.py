# numberlines.py

import fileinput

# how to invoke it
# python numberlines.py numberlines.py
for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num  = fileinput.lineno()
    print '%-40s # %2i' % (line, num)