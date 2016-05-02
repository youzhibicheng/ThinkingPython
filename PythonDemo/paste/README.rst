paste
http://pythonpaste.org/index.html
paste.deploy
http://pythonpaste.org/deploy/

installation
$ sudo pip install PasteDeploy

simple_test.py
    http://127.0.0.1:8080

interactive_test.py
    http://127.0.0.1:8080

pastedeploylab.py
pastedeploylab.ini
    http://127.0.0.1:8080/
    http://127.0.0.1:8080/calc?operator=plus&operand1=12&operand2=23
        输出：
        UnicodeMultiDict([('operator', u'plus'), ('operand1', u'12'), ('operand2', u'23')])
        RESULT= 35

如果使用pycharm运行的话，会出现这样的错误
C:\Python27\python.exe E:/WorkspaceThinking/ThinkingPython/WsgiDemo/paste/pastedeploylab.py
Traceback (most recent call last):
  File "E:/WorkspaceThinking/ThinkingPython/WsgiDemo/paste/pastedeploylab.py", line 11, in <module>
    from wsgiref.simple_server import make_server
ImportError: No module named simple_server
但如果直接到目录下python执行，就可以，不知道是什么原因



pastedeploylab2.py
pastedeploylab2.ini
    http://127.0.0.1:8080/
    http://127.0.0.1:8080/detail
    http://127.0.0.1:8080/detail?name=jameszou&age=32
        这种方式并不能初始化程序中的name和age


pastedeploylab3.py
pastedeploylab3.ini
这个示例的看点是结合route, 再次进行了路由
http://localhost:8080/
http://localhost:8080/log
http://localhost:8080/v1
http://localhost:8080/v1/test
    这个例子相对比较难理解,需要多调试，多看看