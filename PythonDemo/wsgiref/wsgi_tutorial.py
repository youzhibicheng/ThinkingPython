#! /usr/bin/env python

from wsgiref.simple_server import make_server

'''
This is the application
'''
def application(environ, start_response):
    response_body = ['%s : %s' % (key, value) for key, value in sorted(environ.items()) ]
    response_body = '\n'.join(response_body)
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

# create the wsgi server using wsgiref module
# 1: receive the request from client and pass it to application
# 2: send the application's response to the client
httpd = make_server('localhost', 8081, application)
httpd.handle_request()