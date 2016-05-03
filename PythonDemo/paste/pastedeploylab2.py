# coding=utf-8

import sys
import os
import webob
from webob import Request
from webob import Response
#from webob import environ
from paste.deploy import loadapp
from wsgiref.simple_server import make_server
from pprint import pprint


class AuthFilter(object):
      '''filter1,auth
         1.factory read args and print,return self instance
         2.call method return app
         3.AuthFilter(app)
      '''
      def __init__(self,app):
          self.app = app

      def __call__(self,environ,start_response):
          print 'this is Auth call filter1'
          #pass environ and start_response to app
          return self.app(environ,start_response)
      @classmethod
      def factory(cls,global_conf,**kwargs):
          '''global_conf and kwargs are dict'''
          print '######filter1##########'
          print 'global_conf type:',type(global_conf)
          print '[DEFAULT]',global_conf
          print 'kwargs type:',type(kwargs)
          print 'Auth Info',kwargs
          return AuthFilter

class LogFilter(object):
      '''
      filter2,Log
      '''
      def __init__(self,app):
          self.app = app
      def __call__(self,environ,start_response):
          print 'This is call LogFilter filter2'
          return self.app(environ,start_response)
      @classmethod
      def factory(cls,global_conf,**kwargs):
          #print type(global_conf)
          #print type(kwargs)
          print '######filter2###########'
          print '[DEFAULT]',global_conf
          print 'Log Info',kwargs
          return LogFilter

class ShowStuDetail(object):
      '''
      app
      '''
      def __init__(self, name, age):
          # 在url没有制定name和age的情况下
          # 会用pastedeploylab2.ini中对应的name,age初始化
          self.name = name
          self.age = age
      def __call__(self,environ,start_response):
          print 'this is call ShowStuDetail'
          #pprint(environ)
          #pprint environ
          start_response("200 OK",[("Content-type","text/plain")])
          content = []
          content.append("name: %s age:%s\n" % (self.name,self.age))
          content.append("**********WSGI INFO***********\n")
          for k,v in environ.iteritems():
              content.append('%s:%s \n' % (k,v))
          return ['\n'.join(content)] #return a list

      @classmethod
      def factory(cls,global_conf,**kwargs):
          #self.name = kwargs['name']
          #self.age = kwargs['age']
          return ShowStuDetail(kwargs['name'],kwargs['age'])

class ShowVersion(object):
      '''
      app
      '''
      def __init__(self,version):
          self.version = version
      def __call__(self,environ,start_response):
          print 'this is call ShowVersion'
          req = Request(environ)
          res = Response()
          res.status = '200 OK'
          res.content_type = "text/plain"
          content = []
          #pprint(req.environ)
          content.append("%s\n" % self.version)
          content.append("*********WSGI INFO*********")
          for k,v in environ.iteritems():
              content.append('%s:%s\n' % (k,v))
          res.body = '\n'.join(content)
          return res(environ,start_response)
      @classmethod
      def factory(cls,global_conf,**kwargs):
          #self.version = kwargs['version']
          return ShowVersion(kwargs['version'])

if __name__ == '__main__':
     config = "pastedeploylab2.ini"
     appname = "common"
     wsgi_app = loadapp("config:%s" % os.path.abspath(config), appname)
     server = make_server('localhost',8080,wsgi_app)
     server.serve_forever()
     pass