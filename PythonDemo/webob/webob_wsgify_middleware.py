from webob.dec import wsgify
from webob.exc import HTTPForbidden

@wsgify.middleware
def restrict_ip(app, req, ips):
    if req.remote_addr not in ips:
        raise HTTPForbidden('Bad IP: %s' % req.remote_addr)
    return app

@wsgify
def app(req):
    return 'hi'

wrapped = restrict_ip(app, ips=['127.0.0.1'])
