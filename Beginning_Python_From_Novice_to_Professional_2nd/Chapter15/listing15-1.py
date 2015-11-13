from urllib import urlopen
import re
#p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
p = re.compile('<a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://python.org/community/jobs').read()
# take notice of (.*?) in regex
for url, name in p.findall(text):
    print '%s (%s)' % (name, url)