#coding:utf-8

'''
a test function module
'''

import urllib
import time

def fetch(url):
    '''
    fetch url
    '''
    content = urllib.urlopen(url).read()
    f_html = open('tmp%s.html' % str(time.time()), 'w')
    f_html.write(content)
    f_html.close()

def main(urls):
    '''
    main func to be called
    '''
    for url in urls:
        fetch(url)

if __name__ == '__main__':
    FROM_URLS = ['http://www.baidu.com', 'http://www.sohu.com']
    main(FROM_URLS)
