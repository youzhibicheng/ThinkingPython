distutils
setup_disutils.py
$ python setup.py build
$ sudo python setup.py install
# how to uninstall it???
$ sudo pip uninstall HelloWorld
$ python setup.py sdict
$ python setup.py bdist_wininst


setuptools
distribute
setuptools + distribute = setuptools

distutils2

distlib
$ sudo pip install distlib

pbr
Python Build Reasonable
supported by OpenStack
$ sudo pip install pbr
$ sudo pip install --upgrade pbr
$ vim setup.py
$ vim setup.cfg
$ vim README.rst
$ python setup.py build
$ python setup.py sdist
# do not pass the test,it's a little strange


wheel format, PEP 427
$ sudo pip install wheel
$ python setup.py bdist_wheel
# do not need to install wheel file, direct run it
$ 
# How to install a whl file
$ pip install test.whl

# pip install in home directory
$ pip install --user wheel
# set pip to use download cache
# 1. set environment PIP_DOWNLOAD_CACHE=
# 2. vim ~/.pip/pip.conf
#    download-cache

# list install packages
$ pip freeze

# upload pip tarball and whl file into pypi

# check the entry point
$ sudo pip install entry_point_inspector
$ epi group list
$ epi group show console_scripts

