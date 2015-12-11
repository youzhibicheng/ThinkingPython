import nose
from temperature import to_celsius
from temperature import above_freezing

def test_above_freezing ():
	'''Test above_freezing '''
	assert above_freezing(89.4), 'A temperature above freezing'
	assert not above_freezing(-42), 'A temperature below freezing'
	assert not above_freezing(0), 'A temperature at freezing'

def test_boiling ():
	'''Test boiling point'''
	assert to_celsius(212) == 100

def test_roundoff ():
	'''Test that roundoff works'''
	assert to_celsius(100) == 38, 'Returning an unrounded result'   #not 37.77...

if __name__ == "__main__":
	nose.runmodule()