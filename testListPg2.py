from list import *

for expression in \
["EmptyList().isEmptyList()","not EmptyList().add(Integer(7)).isEmptyList()", 
"EmptyList().add(Integer(4)).tail().isEmptyList()",
"not EmptyList().add(Integer(17)).add(Integer(9)).tail().isEmptyList()",
"EmptyList().add(Integer(17)).add(Integer(9)).head().value() == (Integer(9).value())"
]: print(expression, eval(expression), "\n")