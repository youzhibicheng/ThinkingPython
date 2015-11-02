# install nose
# http://nose.readthedocs.org/en/latest/
$ pip install nose
vim tests/test_nose.py
$ nosetests

unittest
vim tests/test_unittest.py
cd tests
python -m unittest -v test_unittest
setUp()
tearDown()

fixtures
sudo pip install fixture
vim tests/test_fixtures.py
cd tests
python -m unittest -v test_fixtures

mocking
>>> import mock
>>> m=mock.Mock()
>>> m.some_method.return_value=42
>>> m.some_method()
42
>>> def print_hello():
...     print "hello world"
... 
>>> m.some_method.side_effect=print_hello
>>> m.some_method()
hello world
>>> def print_hello():
...     print "hello world"
...     return 42
... 
>>> m.some_method.side_effect=print_hello
>>> m.some_method()
hello world
42
>>> m.some_method.call_count
3

mock path
>>> import mock
>>> import os
>>> def fake_os_unlink(path):
...     raise IOError("Testing")
... 
>>> with mock.patch('os.unlink', fake_os_unlink):
...     os.unlink('foobar')
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in fake_os_unlink
IOError: Testing

vim tests/test_mock.py
cd tests
python -m unittest -v test_mock

mixin class
vim tests/test_mixin.py
# do not finish and it's hard to understand

testscenarios
sudo pip install testscenarios
vim tests/test_testscenarios.py

