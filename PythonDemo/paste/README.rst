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
        �����
        UnicodeMultiDict([('operator', u'plus'), ('operand1', u'12'), ('operand2', u'23')])
        RESULT= 35

���ʹ��pycharm���еĻ�������������Ĵ���
C:\Python27\python.exe E:/WorkspaceThinking/ThinkingPython/WsgiDemo/paste/pastedeploylab.py
Traceback (most recent call last):
  File "E:/WorkspaceThinking/ThinkingPython/WsgiDemo/paste/pastedeploylab.py", line 11, in <module>
    from wsgiref.simple_server import make_server
ImportError: No module named simple_server
�����ֱ�ӵ�Ŀ¼��pythonִ�У��Ϳ��ԣ���֪����ʲôԭ��



pastedeploylab2.py
pastedeploylab2.ini
    http://127.0.0.1:8080/
    http://127.0.0.1:8080/detail
    http://127.0.0.1:8080/detail?name=jameszou&age=32
        ���ַ�ʽ�����ܳ�ʼ�������е�name��age


pastedeploylab3.py
pastedeploylab3.ini
���ʾ���Ŀ����ǽ��route, �ٴν�����·��
http://localhost:8080/
http://localhost:8080/log
http://localhost:8080/v1
http://localhost:8080/v1/test
    ���������ԱȽ������,��Ҫ����ԣ��࿴��