http://eventlet.net/
pip install eventlet

协程 coroutines
关于协程,大致可以理解成允许子程序可以多次暂停和恢复执行,是实现多任务的一种有效手段
协程又被称作?"微线程“，简单点说就是在一个原生线程上通过"拷贝"和"切换"?堆栈帧数据来实现执行多个工作，看上去和传统的"单CPU,多线程(Threading)"执行方式差不多

web_crawler.py

web_crawler_greenpile.py

socket_server.py

