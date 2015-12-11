from webob import Request
from webob import Response
from webob.dec import wsgify
from webob.exc import HTTPForbidden

# wsgify
@wsgify
def myfunc(req):
    return Response("Hello World")

class MyRequest(Request):
    @property
    def is_local(self):
        return self.remote_addr == '127.0.0.1'

@wsgify(RequestClass=MyRequest)
def myfunc(req):
    if req.is_local:
        return Response('hi!')
    else:
        raise HTTPForbidden
