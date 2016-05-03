import eventlet
from eventlet.green import socket  
  
def geturl(url):  
    c = socket.socket()  
    ip = socket.gethostbyname(url)  
    c.connect((ip, 80))  
    print ('%s connected' % url) 
    c.sendall('GET /\r\n\r\n') 
    return c.recv(1024)
  
if __name__ == '__main__':
    # urls = ['www.google.com', 'www.baidu.com', 'www.python.org']
    urls = ['www.baidu.com', 'www.python.org']
    pile = eventlet.GreenPile()
    for x in urls:  
        pile.spawn(geturl, x)  
      
     
    for url, result in zip(urls, pile):  
        print ('%s: %s :%s' % (url, repr(result), repr(result)[:50]))  