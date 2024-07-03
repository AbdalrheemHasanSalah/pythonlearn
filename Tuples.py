#------------------------------#
#----------Tuples--------------#
#------------------------------#

#[1]Tuples item are Enclosed with parentheses
#[2]you can remove the parentheses
#[3]tuple are orderded,to use index to access item
#[4]tuple are immutaple => you can not add or delete
#[5]tuple item is not unique
#[6]tuple can have different data type
#[7]
#----------------------------------------------
tuples1=("one","Two")
tuples2="one","two"

print(tuples1)#('one', 'Two')
print(tuples2)#('one', 'Two')

print(type(tuples1))#<class 'tuple'>
print(type(tuples2))#<class 'tuple'>

#tuple index

tuple3=(1,2,3,4,5)

print(tuple3[0])#1
print(tuple3[-1])#5
print(tuple3[-2])#4

#tuple delete and add immutaple
tuple3=(1,2,3,4,5)
#ctuple3[1]="two"
#print(tuple3) # TypeError: 'tuple' object does not support item assignment

#tuple item
tuple4=("one",2,"three",4,"one",True)
print(tuple4[1])
print(tuple4[-1])

#tuble with one elemant

tupleone=("is string")
tupletwo="is string"
#add comma to end to make it tuple
tuple3=("is not sting",)
tuple4="is not string",

print(type(tupleone))
print(type(tupletwo))
print(type(tuple3))#tuple
print(type(tuple4))#tuple
print(len(tuple3))#1

a=1,2,3
b=4,5,6
c=a+b
print(c)#(1, 2, 3, 4, 5, 6)
#c=a+"A,b,c"+b#TypeError: can only concatenate tuple (not "str") to tuple
c=a+("a","b","c")+b
print(c)#(1, 2, 3, 'a', 'b', 'c', 4, 5, 6)

#tuple,list,string rebeat
#use (*) with what do you want to rebeat
string1="string "
tuple1=("tuple",)
List1=[1,2]

print(string1*4)#string string string string
print(tuple1*4)#('tuple', 'tuple', 'tuple', 'tuple')
print(List1*4)#[1, 2, 1, 2, 1, 2, 1, 2]

#Method =>count(value)
a=(1,2,3,4,5,6,7,8,4,6)
print(a.count(4))#2
b=(1,2,3,4,5,6,7,8,4,6)
#print("index is "(b.index(7)))#error
print("index is {:d}".format(b.index(7)))#index is 6
print(f"index is {b.index(6)}")


#tuple destruct

a=("a","b","c")
x,y,z=a
print(x)#a
print(y)#b
print(z)#c
a=("a","b",4,"c")
x,y,_,z=a# under score to pass value
print(x)#a
print(y)#b
print(z)#c