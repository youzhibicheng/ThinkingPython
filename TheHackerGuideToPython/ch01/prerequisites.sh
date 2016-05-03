#!/bin/bash

# This script is to install the prerequisites software that used in this chapter in CentOS7

# install easy_install
sudo yum -y install python-setuptools

# install pip
wget https://pypi.python.org/packages/source/p/pip/pip-7.1.2.tar.gz#md5=3823d2343d9f3aaab21cf9c917710196
tar zxvf pip-7.1.2.tar.gz
cd pip-7.1.2
sudo python setup.py install
cd ..
sudo rm -rf pip-7.1.2*
# use pip command to check

# install PEP8
# seach it in website www.pypi.python.org
# https://pypi.python.org/pypi/pep8
sudo pip install pep8
# edit hello.py
pep8 hello.py

# install pyflakes
# https://pypi.python.org/pypi/pyflakes
sudo pip install pyflakes
# 1. used as a command
# 2. used in vim
# hard to use
# passive already

# install pylint
# https://pypi.python.org/pypi/pylint
# http://docs.pylint.org/
sudo pip install pylint
pylint hello.py
# you can use
# pylint-gui

# pyflakes + pep8 = flake8
sudo pip install flake8
flake8 hello.py

# flake8 + openstack = hacking
# can not find in website
# https://pypi.python.org/pypi 

# right now, the style check of openstack
#Style Checks
#Style checks can be run via tox with `tox -epep8` or manually using `flake8`. 
