#--------------------------------#
#          control Flow          #
#   Ternary Conditional Operator #
#            nasted IF           #   
#--------------------------------#

print("-"*40)
print("control Flow ".center(40," "))
print(" Ternary Conditional Operator".center(40," "))   
print(  "nasted IF".center(40," "))
print("-"*40)

uCountry=input("your country is :")
uName=input("your name is :")
cprice=100
cName=input("your course name is :")
uState=input("your state  ")
if uCountry=="palestine" or uCountry=="palestine".capitalize() or uCountry=="palstine".title():
    print(f"your name is {uName} and country is {uCountry} and your state {uState}")
    if uState=="alquds" and cName=="python":
        print(f"course price it {cprice-100}")
    else:
        print(f"course price it {cprice-80}")
elif uCountry=="jordan" or uCountry=="jordan".capitalize() or uCountry=="jordan".title():
    print(f"your name is {uName} and country is {uCountry} and your state {uState}")
    print(f"course price it {cprice-50}") 
else :
    print(f"your name is {uName} and country is {uCountry} and your state {uState}")
    print(f"course price it {cprice-30}")   


age=int(input(" your age "))

#Ternary Conditional Operator
#condtion If True | if Condtion | Else | condtion If False
print("your school student"if(8<age<18)else "your university student")

#____________________________________#
#___________Calculate Age____________#
#____________________________________#

#write Note

print("-"*40)
print(f"CalculateAge".center(40,"-"))
print("-"*40)

import time
import datetime

#get age
age=int(input("please write your age").strip())
#add month of current year
age+=(datetime.datetime.now().month/12.0)
#get unitTime
unitTime=input("Choose Unit Time:month ,week,day ")


if unitTime=="month" or unitTime=="month".title() or unitTime=="month".capitalize() or unitTime.strip()=="month" :
    time.sleep(5)
    print(f"{age*12}")
elif unitTime=="week" or unitTime=="week".title() or unitTime=="week".capitalize() or unitTime.strip()=="week":
    time.sleep(2)
    print(f"{age*12*4}")
elif unitTime=="day" or unitTime=="day".title() or unitTime=="day".capitalize() or unitTime.strip()=="day":
    time.sleep(1)
    print(f"{age*365}")
else :
    print("invalid input")   

#second solve

#get age
age=int(input("please write your age").strip())
#add month of current year
age+=(datetime.datetime.now().month/12.0)
#get unitTime
unitTime=input("Choose Unit Time: hour,minutes,second  ").strip().lower()

if unitTime=="hour" :
    time.sleep(4)
    print(f"{age*365*24:,}")      
elif unitTime=="minutes":
    time.sleep(3)
    print(f"{age*365*24*60:,}")  
elif unitTime=="second" :
    time.sleep(7)
    print(f"{age*365*24*60*60:,}") 
else :
    print("invalid input")     