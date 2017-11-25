from list import *

# Check if a given element exist in a given list
def isListElem(l, e):
	if l.isEmptyList():
		return False	
	elif not l.isEmptyList() and (l.head().value() == e.value()):
		return True
	elif not l.isEmptyList() and (l.head() != e):
		return isListElem(l.tail(), e)

def isListElem2(l, e):
	return False if l.isEmptyList() else (True if not l.isEmptyList() and l.head().value()==e.value() else isListElem(l.tail(),e)) 

# Return a list without duplicate numbers (like a set)
def setList(l):
	lc = EmptyList()
	if l.isEmptyList():
		return lc
	else:
		if not isListElem(lc, l.head()):
			lc = lc.add(l.head())
			setList(l.tail())
		else: setList(l.tail())

# Return the number of element in a list (size)
def count(l):
	return 0 if l.isEmptyList() else  + count(l.tail())