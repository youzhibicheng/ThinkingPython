#coding:utf-8
import urllib
import time

def a(url):
    content = urllib.urlopen(url).read()
    f = open('tmp%s.html' % str(time.time()), 'w')
    f.write(content)
    f.close()

def main(urls):
    for url in urls:
        a(url)

if __name__ == '__main__':
    urls = ['http://www.baidu.com','http://www.sohu.com']
    main(urls)