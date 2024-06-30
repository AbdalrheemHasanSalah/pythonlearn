
############################
         #List#
############################

#[1] item enclosed in square brackets
#[2] List are ordered,to use index to Access item
#[3] List are Mutable => Add,Delete,Edit
#[4] is not unique
#[5] can have different data type



myList=["one",1,"two",2,"three",3,True]

print(myList)#['one', 1, 'two', 2, 'three', 3, True]
print(type(myList[1]))#class int 
print(myList[1])#1
print(myList[-1])#True
print(myList[-3])#three


print(myList[:-1])#['one', 1, 'two', 2, 'three', 3]
print(myList[2:-1])#['two', 2, 'three', 3]
print(myList[2:])#['two', 2, 'three', 3, True]

print(myList[::1])#['one', 1, 'two', 2, 'three', 3, True]
print(myList[::2])#['one', 'two', 'three', True]

myList[1]=2
myList[-1]=False
print(myList)#['one', 2, 'two', 2, 'three', 3, False]

myList[:3]=[]
print(myList)#[2, 'three', 3, False]

myList[:2]=["a","b"]
print(myList)#['a', 'b', 3, False]

myList[:2]=["a"]#that make edit not reblace edit the cut of list to the cut of list i give
print(myList)#['a', 3, False]



#############################
#---------List Method--------
#############################



#append()

number=["one","two","three"]
number2=["6",7.0,8]

number.append("four")
number.append(5.0)

print(number)#['one', 'two', 'three', 'four', 5.0]

number.append(number2)

print(number)#['one', 'two', 'three', 'four', 5.0, ['6', 7.0, 8]]

print(number[3])#four
print(number[4])#5.0
print(number[5])#['6', 7.0, 8]
print(number[5][1])#7.0




#to concatinat between two list 
#extend()

number=["one","two","three"]
number2=["6",7.0,8]
char=["a","b","c"]

number.extend(number2)
print(number)#['one', 'two', 'three', '6', 7.0, 8]

number.extend(char)
print(number)#['one', 'two', 'three', '6', 7.0, 8, 'a', 'b', 'c']





#to remove an  first elemant found  from list
#remove()
number.remove("one")
print(number)#['two', 'three', '6', 7.0, 8, 'a', 'b', 'c']

#number.remove("one","a","c")TypeError:takes exactly one argument
#print(number)
# number.remove("abd")
#print(number)#ValueError : if elemant not exict in list



#to sorting  number and char in list
#can sort between float and int but can not with char 
#sort()

y=[1,500,120,350,44]
x=["z","b","a","x"]
y.sort()#reverse =False by defulte
x.sort()
print(x)#['a', 'b', 'x', 'z']
print(y)#[1, 44, 120, 350, 500]
y.sort(reverse =True)
x.sort(reverse =True)
print(x)#['z', 'x', 'b', 'a']
print(y)#[500, 350, 120, 44, 1]

#a=[1,2.0,"a"]
#a.sort()#TypeError: '<' not supported between instances of 'str' and 'float'
#print(a)
a=[1,2.0,4,-1,-5.0]
a.sort()
print(a)#[-5.0, -1, 1, 2.0, 4]


#to reverse all elemant in list without sorting
#reverse()

a=[1,"a",2,"b",3,"c"]
a.reverse()
print(a)#['c', 3, 'b', 2, 'a', 1]





#clear all data from list
#clear()

a=[1,2,"a","b"]
a.clear()
print(a)#[]


#to get sahllow copy that mean an change in main list does not efact in copy
#copy()

a=[1,2,"a",True]
b=a.copy()
print(b)#[1, 2, 'a', True]
a.append(5)
print(b)#[1, 2, 'a', True]

#count(object) 
d=[1,2,3,1,1]
print(d.count(1))#3

#index(object)
print(d.index(1))#0


#insert(index,object)
a.insert(0,"abd")
print(a)#['abd', 1, 2, 'a', True, 5]
a.insert(-1,"abd")
print(a)#['abd', 1, 2, 'a', True, 'abd', 5]

#return the object of index
#pop(index)

print(a.pop(0))#abd
print(a.pop(-1))#5


