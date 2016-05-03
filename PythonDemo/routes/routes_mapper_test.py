from routes import Mapper

map = Mapper()

map.connect(None,"error/{action}/{id}",controller="controller_obj")
result1 = map.match('error/myapp/4')
print result1
# result
# {'action': u'myapp', 'controller': u'controller_obj', 'id': u'4'}

map.connect(None,"/message/:name",controller='my_control')
result2 = map.match('/message/12')
print result2
# result
# {'controller': u'my_control', 'name': u'12'}
