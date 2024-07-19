#-----------------------------#
#          Decorators         #
#-----------------------------#

# Decorators => Intro--


#[1] sometime Called meta programming
#[2] Every thing in python is Opject Even function
#[3] Decorators warp other  function and Enhance their behaviour
#[4] Decorators take function and add some functionality and return it
#[5] Decorators is higher order function (function Accept function as parameter)

#-------------------------------------------------------------------------------------------


def Decorators(func):#Decorators 
    
    def nestedFunc(): # Any name its just for Decoration
        print("Before") # Massage For Decorator
        func() # Execute function
        print("After") # Massage From Decorator

    return nestedFunc # return all data   
 
@Decorators #suger syntax
def sayhello():
    print("hello From say hello function ")

#afterdecoration=Decorators(sayhello)
#afterdecoration()

@Decorators #suger syntax
def sayhowareyou():
    print("how are you From function ")


print("#"*50)


sayhello()

print("#"*50)


sayhowareyou()



def Decorators(func):#Decorators 
    
    def nestedFunc(num1,num2): # Any name its just for Decoration
        print("Decorators one") # Massage For Decorator
        if num1<0 or num2<0:
            print("one  number is less than zero") # Massage For Decorator
        func(num1,num2) # Execute function

    return nestedFunc # return all data  


def Decoratorstwo(func):#Decorators 
    
    def nestedFunc(num1,num2): # Any name its just for Decoration
        print("Decorators two") # Massage For Decorator

        if num1>0 or num2>0:
            print("one  number is more than zero") # Massage For Decorator
        func(num1,num2) # Execute function

    return nestedFunc # return all data 

@Decorators
@Decoratorstwo
def calculate(n1,n2):

    print(n1+n2)

print("#"*50)
 
calculate(-100,-90)


print("#"*50)


def Decorators(func):#Decorators 
    
    def nestedFunc(*num): # Any name its just for Decoration
        print("Decorators one") # Massage For Decorator
        for number in num:
           if number<0:
                 print("one  number is less than zero") # Massage For Decorator
        func(*num) # Execute function

    return nestedFunc # return all data  



@Decorators
def calculate(n1,n2,n3,n4):

    print(n1+n2+n3+n4)

print("#"*50)
 
calculate(-100,-90,50,4)


print("#"*50)

from time import time
def speedTest(func):
    def wrapper():
        start=time()
        func()
        end=time()
        print(f"Function Running time is {end -start}")
    return wrapper


@speedTest
def count():
    for number in range(1,20000):
        print(number)


count()