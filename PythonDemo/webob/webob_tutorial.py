from webob import Request
from webob import Response
from pprint import pprint

environ={'METHOD': 'GET'}
req=Request(environ)
# {'METHOD': 'GET'}
req_environ=req.environ
#pprint(req.environ)
# 'GET'
req_method=req.method
#pprint(req.method)
#
req_dir=dir(req)
# req
# <Request at 0x27cd9e8 (invalid WSGI environ)>

req=Request.blank('/article?id=1&id=2')
pprint(req.environ)

# demo for request body
req.body='This is a request body'

req.path_info_peek()
req.path_info_pop()
req.script_name

# Headers
req.headers['Content-Type'] = 'application/x-www-urlencoded'
req.headers.items()
req.environ['CONTENT_TYPE']

# Query & POST
req = Request.blank('/test?check=a&check=b&name=Bob')
req.GET
req.GET['check']
req.GET.getall('check')
req.GET.items()
req.GET.values()

# change to POST
req.POST
req.POST.items()
req.method = 'POST'
req.body = 'name=Joe&email=joe@example.com'
req.POST
req.POST['name']

req.params
req.params['name']
req.params.getall('name')
for name, value in req.params.items():
    print '%s: %r' % (name, value)

req = Request.blank('/test?check=a&check=b&name=Bob')
req.method = 'PUT'
req.body = body = 'var1=value1&var2=value2&rep=1&rep=2'
req.environ['CONTENT_LENGTH'] = str(len(req.body))
req.environ['CONTENT_TYPE'] = 'application/x-www-form-urlencoded'
req.GET
# Why post have items???
req.POST

req.charset = 'utf8'

req = Request.blank('/')
def wsgi_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hi!']
req.call_application(wsgi_app)
res = req.get_response(wsgi_app)

# add user defined attribute
req.some_attr = 'blah blah blah'
new_req = Request(req.environ)
new_req.some_attr
req.environ['webob.adhoc_attrs']

# response
res = Response()
res.status
res.headerlist
res.body
res.status = 404
res.status
res.status_code
res.headerlist = [('Content-type', 'text/html')]
res.body = 'test'
print res

# response headers
res.headers
res = Response(content_type='text/plain', charset=None)  
f = res.body_file  
f.write('hey')  
f.write(u'test')
f.encoding
res.charset = 'utf8'
f.encoding
f.write(u'test')
res.app_iter
res.body

# Header Getters
