#----------------------------#
#----Iterable Vs Iterater----#
#----------------------------#

# Iterable
#[1] Object Contanins Data That Can Be Iterated Upon
#[2] Example (string,List,set,Tuple,Dictionary)
#---------------------------------------------------------
# Iterater
#[1] Object Used to Iterater Over Iterable Using next() Method Return 1 Element at A time
#[2] You can Generate Iterater From Iterable when using iter() method
#[3] For loop Already Calls iter() Method on the Iterable Behind the scene
#[4] Gives "StopIteration" if Theres No Next Element
#--------------------------------------------------------------------------------------------






# Iterable

string="abdalrheem"
list=[1,2,3,4]

#notIterable=True
#for latter in notIterable:#TypeError: 'bool' object is not iterable
#   print(latter)

#notIterable=10
#for number in notIterable:
#    print(number)#TypeError: 'int' object is not iterable

for latter in string:
    print(latter,end=" ")

for number in list:
    print(number,end=" ")

#print(next(string))#TypeError: 'str' object is not an iterator
string=iter(string)
print("\n")
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))

for latter in iter("abdalrheem"):
    print(latter,end=" ")




