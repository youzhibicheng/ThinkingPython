http://www.pylint.org/
http://docs.pylint.org/

pip install pylint


1. 进入这个模块所在的文件夹，运行 pylint [options] module.py
这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。
2. 不进入模块所在的文件夹，运行 pylint [options] directory/module.py
这种调用方式当如下条件满足的时候是可以工作的：directory 是个 Python 包 ( 比如包含一个 __init__.py 文件 )，或者 directory 被加入了 Python 的路径中。
使用 Pylint 对一个包 pakage 进行代码检查：

1. 进入这个包所在文件夹，运行 pylint [options] pakage。
这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。
2. 不进入包所在的文件夹，运行 pylint [options] directory/ pakage。
这种情况下当如下条件满足的时候是可以工作的：directory 被加入了 Python 的路径中。比如在 Linux 上，export PYTHONPATH=$PYTHONPATH: directory。
此外，对于安装了 tkinter 包的机器，可以使用命令 pylint-gui打开一个简单的 GUI 界面，在这里输入模块或者包的名字 ( 规则同命令行 ), 点击 Run，Pylint 的输出会在 GUI 中显示。