try:
    import unittest2 as unittest
except ImportError:
    import unittest

class TestKey(unittest.TestCase):
    def test_key(self):
        a = ['a','b']
        b = ['b']
        self.assertEqual(b, a)

class TestFail(unittest.TestCase):
    def test_range(self):
	for x in range(5):
	    if x>4:
		self.fail('range return a too big value : %d' % x)
