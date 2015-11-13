# invoke like this
# cat listing11-2.txt | python listing11-1.py

# somescript.py
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'Wordcount:', wordcount