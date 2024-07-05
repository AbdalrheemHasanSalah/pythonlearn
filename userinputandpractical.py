#_______________________________
#             userinput
#_______________________________

fname=input("first name is ")
mname=input("middle name is ")
lname=input("last name is ")
fname=fname.capitalize().strip().lower()

lname=lname.capitalize().strip().upper()

print(f"{fname}{mname.capitalize().strip().title():.1s}{lname}")
print(fname,mname[0],lname)
print("{} {} {}".format(fname,mname,lname))
print({fname},{mname},{lname})#{'abd'} {'hasan'} {'SALAH'}
print("first :%s "%fname,"second %s"%mname,"third %s"%lname)

print("_"*15)

#______________________________#
#       email practical        #
#______________________________#

email="abdsalah@outlook.com"

print(email.index("@"))
print(email[:email.index("@")])#abdsalah


theName=input("your name is ").strip().capitalize()
theEmail=input("your Email is ").strip()

print(f"hello your name is {theName} your Email is {theEmail}")
print(f"your user name is {theEmail[:theEmail.index("@")]} and your email is {theEmail[(theEmail.index("@")+1):theEmail.index(".")]} and your domin is {theEmail[(theEmail.index(".")+1):]}")


#-----------------------------------#
#        Age Full ditails           #
#-----------------------------------#

import datetime

Age=input("your age ").strip()
print(type(Age))
integerAge=int(Age)
yearBirth=(datetime.datetime.now().year)-integerAge
yearDate=integerAge+((datetime.datetime.now().month)/12.0)

print(f"{yearBirth}")

#Get age in all time unit 

month=yearDate*12
weeks=month*4
day=yearDate*365
hour=day*24
minutes=hour*60
second=minutes*60

print(f"age in month is {month} \n age in weeks {weeks:,} \n age in day is {day:,} \n age in hour {hour:,} \n age in minutes {minutes:,} \n  age in second {second:,}")
