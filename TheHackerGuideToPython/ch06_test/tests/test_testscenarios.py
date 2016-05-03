try:
    from unittest import mock
except ImportError:
    import mock

import requests
import testscenarios


class WhereIsPythonError(Exception):
    pass

def is_python_still_a_programming_language():
    try:
	r=requests.get("http://python.org")
    except IOError:
	#pass
	raise
    else:
  	if r.status_code==200:
	    return "Python is a programming language" in r.content
    	raise WhereIsPythonError("Something bad happen")

def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code=status_code
    m.content=content
    def fake_get(url):
	return m
    return fake_get

class TestPythonErrorCode(testscenarios.TestWithScenarios):
    scenarios = [
	{'N'}
    ]

def raise_get(url):
    raise IOError("Unable to fetch url %s" % url)

class TestPython(unittest.TestCase):
    @mock.patch('requests.get', get_fake_get(200, "Python is a programming language for sure"))
    def test_python_is(self):
	self.assertTrue(is_python_still_a_programming_language())

    @mock.patch('requests.get', get_fake_get(200, 'Python is no more a programming language'))
    def test_python_is_not(self):
	self.assertFalse(is_python_still_a_programming_language())

    @mock.patch('requests.get', get_fake_get(404, 'Whatever'))
    def test_bad_status_code(self):
	self.assertRaises(WhereIsPythonError, is_python_still_a_programming_language)
	
    @mock.patch('requests.get',raise_get)
    def test_raise_get(self):
	#self.assertRaises(WhereIsPythonError, is_python_still_a_programming_language)
	self.assertRaises(IOError, is_python_still_a_programming_language)
	
