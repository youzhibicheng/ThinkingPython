class Singleton(object):
	__instance=None
	def__init__(self):
		pass
	def__new__(cls,*args,**kwd):
		if Singleton.__instance is None:
			Singleton.__instance=object.__new__(cls,*args,**kwd)
		return Singleton.__instance



