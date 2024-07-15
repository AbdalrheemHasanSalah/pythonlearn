#---------------------------#
#----Built In Function------#
#---------------------------#
# all()
# any()
# bin()
# id()
#-----------------------------

x=[1,2,3,4]


if all(x):
    print("all is true")
else :
    print("thare at least one is false")    

x=[[],0]
if any(x):
    print("at least one is true")
else :
    print("at lest one is False")

print(bin(4))#0b100
print(bin(97))#0b1100001


x=1
y=2
print(id(x))#140707452257664
print(id(y))#140707452257696

#---------------------------------
# sum()
# round()
# range()
#print()
#---------------------------------


# sum(iterable,start)

a=[1,50,100,5]

print(sum(a))#156
print(sum(a,50))#206 add number to the sum of iterable

a=(1,2,3,4)
print(sum(a))#10
print(sum(a,10))#20 add number to the sum of iterable

a={1,2,3}

print(sum(a))#6
print(sum(a,11))#17

a={
    1:1,
    2:2,
    4:5
}

print(sum(a))#7 sum for key
print(sum(a,50))#57

print(sum(a.values()))#8
print(sum(a.values(),15))#23


# round(number,numberofdigit)

print(round(150.45))#150
print(round(150.55))#151

print(round(150.654,2))#150.65
print(round(150.655,2))#150.66


# range(start,end,step)

print(list(range(0)))#[]
print(list(range(10)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,5)))#[0, 1, 2, 3, 4]
print(list(range(0,21,2)))#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# print()

print("hello abd")
print("hello","abd")
print("hello","abd","how","are","you",sep="@")


print("first line ",end=" end ")
print("seconed line")
print("Third line ")#first line  end seconed line
                      #Third line


print(" # "*15)

#----------------------------------
# abs()
# pow()
# min()
# max()
# slice()
#----------------------------------

# abs(number)
print(abs(15))
print(abs(-15))
print(abs(15.5))
print(abs(-15.5))

# pow(base,exp,mod)
print(pow(2,5))#32
print(pow(4,5))#1024
print(pow(2,5,10))#2


print(" # "*15)

# min(item,item,item or itrator)
tuple=(1,-5,-9,7)
print(min(10,20,-50,-10))#-50
print(min(tuple))#-9
print(min("a","z","abd"))#a
print(min("z","abd"))#abd

print(" # "*15)

# max(item,item,item or itrator)
tuple=(1,-5,-9,7)
print(max(10,20,-50,-10))#20
print(max(tuple))#7
print(max("a","z","abd"))#z
print(max("z","abd"))#z

print(" # "*15)

# slice()
a=["a","b","c","d","e"]
print(a[:4])#['a', 'b', 'c', 'd']
print(a[slice(4)])#['a', 'b', 'c', 'd']
print(a[slice(2,4)])#['c', 'd']


print(" # "*15)

#----------------------------------
#         Map
#----------------------------------

#[1] Map take a function + iterator 
#[2] Map Called Map becuse it map function in every element
#[3] the function can be pre-defined function or lambda function 
#------------------------------------------------------------------------


def formatetext(text):
    return f"-{text}-"
txt=["pyhton","c++","java"]

formated=map(formatetext,txt)
print(formated)

for name in formated:
    print(name)

for name in map(formatetext,txt):
    print(name) 


for name in list(map(formatetext,txt)):
    print(name)    

for name in list(map(lambda txt:f"-{txt.strip().capitalize()}-",txt)):
    print(name)
  

#----------------------------------
#         Filter
#----------------------------------

#[1] Filter take a function + iterator 
#[2] Filter Called Map becuse it map function in every element
#[3] the function can be pre-defined function or lambda function 
#[4] Filter out all element for which function return true
#[5] finction return boolean value 
#------------------------------------------------------------------------


def checkNumber(num):
    if num >10:
        return num
    

number= [1,5,10,19,20,4]
numberResult=filter(checkNumber,number)

for number in numberResult:
    print(number)#19
                 #20






def checkName(name):
    
        return name.startswith("a") 
    

data= ["abd","abood","abdalrheem","pyhton","c++"]
dataResult=filter(checkName,data)

for data in dataResult:
    print(data)



#def checkName(name):
    
 #       return name.startswith("a") 
    

data= ["abd","abood","abdalrheem","pyhton","c++"]
dataResult=filter(lambda name:name.startswith("a"),data)

for data in dataResult:
    print(data)

for data in filter(lambda name:name.startswith("a"),data):
    print(data)

#----------------------------------- 
#        Reduce()
#-----------------------------------
from functools import reduce
def sumall(num1,num2):
    return num1+num2

number=[1,20,25,50,90,100]
result=reduce(sumall,number)
result=reduce(lambda num1,num2:num1+num2,number)

print(result)#286
#((1+20)+25)+.....

#----------------------
# enumerate()
# help()
# reversed()
#----------------------


#enumerate(iterable,start=0)


skill=["c","c++","java","python"]
enumskill=enumerate(skill,20)
print(type(enumskill))#<class 'enumerate'>
for skil in enumskill:
     print(skil)#(20, 'c')
               #(21, 'c++')
               #(22, 'java')
               #(23, 'python')

for counter,skil in enumskill:
    print(f"{counter} - {skil}")#20 - c
                                #21 - c++
                                #22 - java
                                #23 - python

print("-"*15)

#help()
#print(help(print))


#reversed(iterable)
num="1234567"
print(reversed(num))

for number in reversed(num) :
    print(number)#7
                 #6 
                 #5
                 #4
                 #3
                 #2
                 #1

for skil in reversed(skill) :
    print(skil)
