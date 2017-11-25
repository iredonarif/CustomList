from list import *

def emptyListIsEmpty():
	return "An empty list is empty", EmptyList().isEmptyList()
	
def compositeListIsNotEmpty():
	return "A composite list is not empty", not EmptyList().add(Integer(7)).isEmptyList()
	
def testEmptyAndCompositeList():
	return "An empty list is empty and a composite list is empty", EmptyList().isEmptyList() and EmptyList().add(Integer(7)).isEmptyList()		

def tailOFListWithOneElementIsEmpty():
	return "The tail of a list with one element is an empty list", EmptyList().add(Integer(4)).tail().isEmptyList()
	
def tailOfListWithAtLeastOneElementIsNotEmpty():
	cl = EmptyList().add(Integer(17)).add(Integer(9))
	return "The tail of a list with at least one element is not empty", not cl.tail().isEmptyList()

def testTheHead():
	return "The head of the list (9,17) is 9", EmptyList().add(Integer(17)).add(Integer(9)).head().value() == (Integer(9).value())

def testTheHead2():
	return "The head of the list (17) is 9", EmptyList().add(Integer(17)).head().value() == Integer(9).value() 

def showList():
	l = EmptyList().add(Integer(4)).add(Integer(7))
	return l.head().value(), l.tail().head().value()
	
#function calls

print(emptyListIsEmpty(),"\n")
print(compositeListIsNotEmpty(),"\n")
print(testEmptyAndCompositeList(),"\n")
print(tailOFListWithOneElementIsEmpty(),"\n")
print(tailOfListWithAtLeastOneElementIsNotEmpty(),"\n")
print(testTheHead(), "\n")
print(testTheHead2(), "\n")
print(showList(), "\n")