webob
WebOb provides objects for HTTP requests and responses. Specifically it does this by wrapping the WSGI request environment and response status/headers/app_iter(body)

http://webob.readthedocs.org/en/latest/
http://www.webob.org/

# pip install webob



webob_example_wiki.py
http://webob.readthedocs.org/en/latest/wiki-example.html
wiki server:������webobʵ��WSGIӦ��
webob_example_wiki.py
http://localhost:8080/
    -> http://localhost:8080/?action=edit
http://localhost:8080?action=view
http://localhost:8080?action=edit

@property ����������?
    ��Ϊhtmlҳ����{{page.title}}������



webob_example_comment.py
http://webob.readthedocs.org/en/latest/comment-example.html
comment server:������webob�����м��
Every middleware needs an application (app) that it wraps. This middleware also needs a location to store the comments
How to set BASE_DIRECTORY
������վ,Ȼ��������ۣ��ٽ�������ӵ��������վ�ϱ���
��ע������ paste StaticURLParser ��ʹ��
�½�base_directory, �������½� index.html
python webob_example_comment.py base_directory
http://localhost:8080/index.html
    -> http://localhost:8080/.comments
http://localhost:8080/.comments?url=JamesZou&name=JamesZouTest1&homepage=www.jameszou1.org&comments=JamesZouComments1
http://localhost:8080/.comments?url=JamesZou&name=JamesZouTest2&homepage=www.jameszou2.org&comments=JamesZouComments2
JamesZou#comment-area
������ӵ���ûͨ��������


testdeploy.py
testdeploy.ini
http://www.aboutyun.com/thread-8551-1-1.html
