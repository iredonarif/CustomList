class Value(object):

	def isEmptyList(self):
		return False

class List(Value):
	
	def add(self, n):
		cl = CompositeList()
		cl.isHead = n
		cl.isTail = self
		return cl

class EmptyList(List):
	
	def isEmptyList(self):
		return True
		
class CompositeList(List):
	
	def head(self):
		return self.isHead
		
	def tail(self):
		return self.isTail	

class Atom(Value):
	pass
	
class Integer(Atom):
	def __init__(self, n):
		self.integer = n
		
	def value(self):
		return self.integer