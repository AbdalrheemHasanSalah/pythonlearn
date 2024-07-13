#--------------------------#
#------Function------------#
#--------------------------#

#[1] A Function is Reusable Block of code Do A Task 
#[2] A Function Run when call it
#[3] A Function Accept Element To Deal with called [parameters]
#[4] A Function can do the Task without Returning Data
#[5] A Function can Return Data After it finished
#[6] A Function creat to prevent DRY
#[7] A Function Accept Element when you call it called [Arguments]
#[8] There's built-in Function and user defined function
#------------------------------------------------------------------


#for defined function use def
def printfunction():
    print("hello function method in python")#with out return 

#for call function  
printfunction()

def printfunction_return():
    return "function with return"


print(printfunction_return())


print("#"*15)
####Function parameters And arguments#####


a,b,c="abd","abdalrheem","abood"

#print(f"{a},{b},{c}")


#value in def function  => parameter 
#any value in call funtion called arrguments


def sey_Hello(name):
    return f"hello {name}"#Task is what i do in function

print(sey_Hello(a))
print(sey_Hello(b))
print(sey_Hello(c))



def multibliction(number1,number2):
    return number1*number2

def suptractor(number1,number2):
    return number1-number2

def div(number1,number2):
    return number1/number2

def add(number1,number2):
    return number1+number2

def mod(number1,number2):
    return int(number1)%number2

def Floor_div(number1,number2):
    return int(number1)//int(number2)
number1,number2="a","b"
while number1.isalpha():
    number1=input("first number ").strip()

while number2.isalpha():
    number2=input("seconed number ").strip()

number1=int(number1)
number2=int(number2)
print(f"multibliction is : {multibliction(number1,number2)}")
print(f"suptractor is :{suptractor(number1,number2)}")
print(f"division{div(number1,number2)}")
print(f"addtion is : {add(number1,number2)}")
print(f"mod is : {mod(number1,number2)}")
print(f"Floor_divition : {Floor_div(number1,number2)}")


print("#"*15)


########################################################
#        Function Paking And Unpaking arguments *Args  #
########################################################

list=[1,2,3,4]
print(list)
#(*)is task  print list value
print(*list)#1 2 3 4

#  (*) => to give any number of parameters
def sey_hello(*people):
    for sumone in people:
        print(f"hello {sumone}")



sey_hello("abd","abdalrheem","abood")
sey_hello("abood","abdalrheem")
sey_hello("abd")

print("#"*15)

####Function Default value####

#def personDetails(name="unknown",age,country="unknown"): give an error Default value should for all parameter after define it 
 #   print(f"name is {name} age is {age} country is {country}")

def personDetails(name,age="unknow",country="unknown"):
        print(f"name is {name} age is {age} country is {country}")

personDetails("abd")#name is abd age is unknow country is unknown


def personDetails(name,age,country="unknown"):
    print(f"name is {name} age is {age} country is {country}")

    
personDetails("abd",21,"palestine")
personDetails("abd",21)#name is abd age is 21 country is unknown
#personDetails("abd")#TypeError:missing 1 required positional argument.

print("#"*15)


########################################################
#     Function Paking And Unpaking arguments **kwArgs  #
########################################################

#def function to use args (*)
def show_skill(*skills):
    print(type(skills))#print tuble type
    for skill in skills:
        print(f"skill :{skill}")

skill=("c++","python","java")
show_skill(skill)#skill :('c++', 'python', 'java')
show_skill(*skill)#print tuble one by one  example  
show_skill("c++","java","python")                                         #skill :c++
                                                   #skill :python
                                                   #skill :java

skills={
     "c++":"%90",
     "python":"70%",
     "java":"89"

}
def sow_skill(**skills):
    print(type(skills))#print dict type
    for skill,skillvalue in skills.items():
        print(f"skill :{skill} skill value :{skillvalue}")

#sow_skil(skills)#TypeError: sow_skil() takes 0 positional arguments but 1 was given
sow_skill(java="90%",python="70")#if i put c++ give an error syntax print it look like exampl under
sow_skill(**skills)#print dict one by one example 
                                         #skill :c++ skill value :%90
                                         #skill :python skill value :70%
                                         #skill :java skill value :89
print("#"*15)
                                    
                                         
########################################################
#    Function Paking And Unpaking arguments traninings #
########################################################


def show_skill(name,*skill,**skills):
    print(f"hello {name}\n skill with out progress Is :")
    for skil in skill:
        print(f"- {skil}")
    print(f"skill with progress Is :")
    for skil,values in skills.items():
        print(f"skill {skil} => {values}")
   
dict={
     "c++":"%90",
     "python":"70%",
     "java":"89"

}
tup=("java","python","c++")
show_skill("abd","java","python","c++",python="70%")
show_skill("abd",*tup,dict)#arrange argumants to give date correct and here print dict with out progress
show_skill("abd",*tup,**dict)

print("#"*15)

#-----------------#
# Function scope--#
#-----------------#
def value():
    global x #to make variable global 
    x=1
    print(f"values :{x}")

def value2():
    print(f"values :{x}")
def value3():
    x=15
    print(f"values :{x}")

#print(x)#NameError: name 'x' is not defined 
value()#1
print(x)#1
value2()#1
value3()#15


print("#"*15)



#------------------------#
#---function recursion---#
#------------------------#

def function_recursion(x=1):
   if x==10:
       return x
   return function_recursion(x+1)



print(function_recursion(5))#10


def cleanword(word):
    if len(word)==1:
        return(word)
    #to get char with out rebeat one by one by delete first 
    if    word[1]==word[0]:
        return cleanword(word[1:]) 
    #to add char that not rebeat to slicing
    return word[0]+cleanword(word[1:])

print(cleanword("wwooorrlldd"))#world


#------------------------#
#---Function Lambda------#
#---Anonymos Function----#
#------------------------#

#[1] It Has not Name
#[2] Can call it in line with out defining it
#[3] Can use return data from outher function
#[4] Lambda use for simple function and Def Handle The large Tasks
#[5] Lambda function is single Exprtion not block code
#[6] Lambda Type is function

def say_hello(name,age):
    return f"hello {name} your age  {age}"
hello= lambda name,age :f"hello {name} your age  {age}"

print(say_hello("abd",21))
print(hello("abd",21))
print(type(hello))






