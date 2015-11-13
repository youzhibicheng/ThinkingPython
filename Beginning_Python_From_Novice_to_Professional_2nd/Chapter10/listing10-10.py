# find_sender.py
import fileinput, re
# what does 'From: (.*) <.*?>$' mean???
pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m: print m.group(1)