#!/usr/bin/env/python
#coding=utf-8

from routes import Mapper
from routes import middleware
import webob.dec
from wsgiref.simple_server import make_server

class controller(object):
    def __init__(self):
        self.i = 1
    def __call__(self):
        print self.i
    def search(self):
        return "do search()"
    def show(self):
        return "do show()"
    def index(self):
        return "do index()"
    def update(self):
        return "do update()"
    def delete(self):
        return "do delete()"
    def create(self):
        return "do create()"
    def create_many(self):
        return "do create_many()"
    def update_many(self):
        return "do update_many()"
    def list_many(self):
        return "do list_many()"
    def delete_many(self):
        return "do delete_many()"

class appclass(object):
    def __init__(self):
        a = controller()
        map = Mapper()

        # ATTENTION: for the following condition, should test one by one !!!

        """routes match condition 1"""
        # curl -X GET http://localhost:8088/images
        # map.connect('/images',controller=a,
        #            action='search',
        #            conditions={'method':['GET']})

        """routes match condition 2"""
        # curl -X GET  http://localhost:8088/show/hihi
        # curl -X POST  http://localhost:8088/failfunc/test
        # map.connect('name',"/{action}/{pid}",controller=a)

        """routes match condition 3"""
        # map.resource("message","messages",controller=a)
        # the same as the following
        # map.connect('/messages',controller=a,action='index',conditions={'method':['GET']})
        # map.connect('/messages',controller=a,action='create',conditions={'method':['POST']})
        # map.connect('/messages/{id}',controller=a,action='show',conditions={'method':['GET']})
        # map.connect('/messages/{id}',controller=a,action='update',conditions={'method':['PUT']})
        # map.connect('/messages/{id}',controller=a,action='delete',conditions={'method':['DELETE']})
        # curl -X GET  http://localhost:8088/messages   -> do index()
        # curl -X POST http://localhost:8088/messages   -> do create()
        # curl -X GET  http://localhost:8088/messages/12    -> do show()
        # curl -X PUT  http://localhost:8088/messages/12    -> do update()
        # curl -X DELETE  http://localhost:8088/messages/12 -> do delete()
        # what does collection={'search':'GET'} mean ???
        # map.resource("message","messages",controller=a,collection={'search':'GET'})

        """routes match condition 4"""
        # curl -X GET  http://localhost:8088/messages/search        -> do search()
        # curl -X POST  http://localhost:8088/messages/create_many  -> do create_many()
        ## curl -X GET  http://localhost:8088/messages/create_many  -> do show()
        ## curl -X PUT  http://localhost:8088/messages/create_many  -> do update()
        # curl -X DELETE  http://localhost:8088/messages/create_many    -> do delete()
        # curl -X POST  http://localhost:8088/messages/1/update_many    -> do update_many()
        # curl -X POST  http://localhost:8088/messages/1/delete_many    -> do delete_many()
        # map.resource('message', 'messages',controller=a,
        #                 collection={'list_many':'GET','create_many':'POST'},
        #                 member={'update_many':'POST','delete_many':'POST'})

        """routes match condition 5"""
        # curl -X POST  http://localhost:8088/proj1/messages    -> do create()
        # curl -X GET  http://localhost:8088/proj1/messages     -> do index()
        # curl -X PUT  http://localhost:8088/proj1/messages     -> fake url
        # curl -X DELETE  http://localhost:8088/proj1/messages  -> fake url
        # curl -X GET  http://localhost:8088/proj1/messages/list_many   -> do list_many()
        # curl -X POST  http://localhost:8088/proj1/messages/member_3/update_many   -> do update_many()
        map.resource('message', 'messages',controller=a,path_prefix='/{projectid}',
                    collection={'list_many':'GET','create_many':'POST'},
                    member={'update_many':'POST','delete_many':'POST'})

        # map.resource('type', 'types',controller=other_controller,
        #                    parent_resource=dict(member_name='message', collection_name='messages'),
        #                    path_prefix = '{projectid}/%s/:%s_id' %('nex','nexs'))

        # for more information, please check
        # http://routes.readthedocs.org/en/latest/restful.html

        self.route = middleware.RoutesMiddleware(self.dispatch,map)

    @webob.dec.wsgify
    def __call__(self,req):
        return self.route

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        print "route match result is:",match
        if not match:
            return "fake url"

        controller = match['controller']
        action = match['action']
        if hasattr(controller,action):
            func = getattr(controller,action)
            ret = func()
            return ret
        else:
            return "has no action:%s" %action


if __name__=="__main__":
    app = appclass()
    server = make_server('',8088,app)
    server.serve_forever()
