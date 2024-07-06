########################################
############MembershipOperators#########
########################################



a="abd"
print("a"in a)#True
print("b"in a)#True
print("c"in a)#False
print("d"in a)#True
print("-"*20)

print("a" not in a)#False
print("b"not in a)#False
print("c"not in a)#True
print("d"not in a)#False

print("$"*20)

List=[1,2,3,4]

print(1 in List)#True
print(2 in List)#True
print(5 in List)#False

print("-"*20)
print(1 not in List)#False
print(2 not in List)#False
print(5 not in List)#True

List=["jordan","palestine"]

myCountry=input("input your country ").strip().lower()

if myCountry in List:
    print(f"you have discount is : {50}%")

elif myCountry not in List:
    print(f"you have discount is : {10}%")



#__________________________________________#
#_______ Practical Membership Control______#
#__________________________________________#

#List contins Admin
Admin=["abd","abdalrheem","Abood"]

 #login
myName=input("your name is ").strip().lower()

#to check if name in Admin
if myName in Admin:
    print("welcome to wepsite")
elif myName not in Admin:
    print("you can add your name if you wont enter")  
    if input("yes / no ") =="yes":
        Admin.append(myName)
        print("welcome to our wepsite")
    else:
        print("good luke")

#to update Admin name
if myName in Admin:
    choose=input("put update or delete to your admin ").lower().strip()
    if choose=="update":

     logicUp=input("update you name put yes /no ").strip().lower()
     if logicUp.__eq__("yes"):
        index =Admin.index(myName)
        Admin.insert(index,input("your new name"))
        Admin.remove(myName)
        print("name Update")
        print(Admin)
        #second way 
        #Admin[index]="new name"
     else:
       print("if you wont to update your name come back")   
#to check if wont delete your admin 
    elif choose=="delete":
      print("do you wont to delete your admin access to wepsite")
      logicDel=input("yes / no ").strip().lower()

      if logicDel=="yes":
         print("Nice to meet you good bey")
         Admin.pop(Admin.index(myName))
         print(Admin)
         print("name Deleted")
      else:
          print("welcome to wepsite")
    #wrong choose
    else:
       print("please write correct method")











































