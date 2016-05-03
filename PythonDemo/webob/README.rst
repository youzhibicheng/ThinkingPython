webob
WebOb provides objects for HTTP requests and responses. Specifically it does this by wrapping the WSGI request environment and response status/headers/app_iter(body)

http://webob.readthedocs.org/en/latest/
http://www.webob.org/

# pip install webob



webob_example_wiki.py
http://webob.readthedocs.org/en/latest/wiki-example.html
wiki server:侧重于webob实现WSGI应用
webob_example_wiki.py
http://localhost:8080/
    -> http://localhost:8080/?action=edit
http://localhost:8080?action=view
http://localhost:8080?action=edit

@property 用来干嘛呢?
    作为html页面中{{page.title}}的属性



webob_example_comment.py
http://webob.readthedocs.org/en/latest/comment-example.html
comment server:侧重于webob来做中间件
Every middleware needs an application (app) that it wraps. This middleware also needs a location to store the comments
How to set BASE_DIRECTORY
保存网站,然后添加评论，再将评论添加到保存的网站上保存
请注意这里 paste StaticURLParser 的使用
新建base_directory, 在里面新建 index.html
python webob_example_comment.py base_directory
http://localhost:8080/index.html
    -> http://localhost:8080/.comments
http://localhost:8080/.comments?url=JamesZou&name=JamesZouTest1&homepage=www.jameszou1.org&comments=JamesZouComments1
http://localhost:8080/.comments?url=JamesZou&name=JamesZouTest2&homepage=www.jameszou2.org&comments=JamesZouComments2
JamesZou#comment-area
这个例子调试没通过，放弃


testdeploy.py
testdeploy.ini
http://www.aboutyun.com/thread-8551-1-1.html
