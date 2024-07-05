#################################
#           typeConversion
#################################


# & in python is and
# | in python is or
# ! in python is npt

print(bool(None))
print(bool(0))
print(bool(" "))
print(bool(""))

print("_"*20)

variableList=[1,2,3]
variableset={1,2,3}
variabledictionary={
    "one":1,
    "two":2,
    "three":3
}

a=10
b=10.0

print(type(str(a)))
print(type(str(b)))
print(str(variabledictionary))
print(type(str(variableList)))
print(type(str(variableset)))
print(type(str(variabledictionary)))


print("_"*20)

#tuple()
variableList=[1,2,3]
variableset={1,2,3}
variabledictionary={
    "one":1,
    "two":2,
    "three":3
}
variablestring="python"

print(tuple(variabledictionary))
print(type(tuple(variableList)))
print(type(tuple(variableset)))
print(type(tuple(variabledictionary)))
print(type(tuple(variablestring)))
#print(type(tuple(10)))#TypeError: 'int' object is not iterable
#print(type(tuple(10.0)))#TypeError: 'float' object is not iterable

print("_"*20)


#list()

variabletuple=(1,2,3)
variableset={"A","b","c"}
variabledictionary={
    "A":1,
    "B":2
}
string="A B C"

print(list(variabledictionary))
print(type(list(variabletuple)))
print(type(list(variableset)))
print(type(list(variabledictionary)))
print(type(list(string)))


print("_"*20)

#set()

variabletuple=(1,2,3)
variablelist=["A","b","c"]
variabledictionary={
    "A":1,
    "B":2
}
string="A B C"

print(set(variabledictionary))
print(type(set(variabletuple)))
print(type(set(variablelist)))
print(type(set(variabledictionary)))
print(type(set(string)))


print("_"*20)


#dict()
#sholud in nested of any type key+value

#TypeError: cannot convert dictionary update sequence element #0 to a sequence
#for all type under
#variabletuple=(1,2,3)
#variablelist=["A","b","c"]#
#variableset={"A","B"}#
#string="A B C" #can not convert string to dict
        
 #variableset={{"a",1},{"b",2}}
     #TypeError: unhashable type: 'set'

variabletuple=((1,"A"),(2,"b"),(3,"c"))
variablelist=[["A","one"],["b","two"],["c","three"]]

print(dict(variablelist))#{'A': 'one', 'b': 'two', 'c': 'three'}
print(type(dict(variabletuple)))
print(type(dict(variablelist)))
