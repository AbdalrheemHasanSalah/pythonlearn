#__________________________#
#_____while loop___________#
#__________________________#
print("hello")
a=0
#print index 0 to 9
while a<10:
    print(a)
    a+=1
else:
    print(" end1")    
    
print("end2")   

listchar=["a","b","d","a","l","r","h","e","e","m"]
string1=input("string to git char number")
listchar=list(string1)
i=0
#to print all elemant by loop
while i<len(listchar):#a<10
    print(f"number is ( {str(i+1).zfill(3)} )and char is {listchar[i]}")
    i+=1
print("end")    

#get empty list
listWepsite=[]
#get maxindex
maxIndex=5
#getindex to increase
i=0
while i<maxIndex:
    print("input url of wepsite : ")
    string="https:\\"
    string2=input(f"https:\\\\ ")
    stringcon=string + string2
    listWepsite.insert(i,stringcon)
    print(listWepsite)
    i+=1
#to sort the wepsitelist by char   
if len(listWepsite)>0:
       listWepsite.sort()
print("listWepsite after sorting ")       
print(listWepsite)

i=0   
#to get name of wepsite without domin 
while i<len(listWepsite)  :
    if listWepsite[i].find(".")!=-1:
      print(listWepsite[i][(listWepsite[i].index("\\")+1):listWepsite[i].index(".")])
    i+=1




#__________________________________#
#-------sample password gess-------#
#__________________________________#

import random

#list of user name
listname=["abd","abood"]
#list of password
listpassword=["abd123","abood123"]
#list of email
email={
    "abd":{"email":"abd@gmail.com", "codeResive":0},
    
}
#number of trais
trais=4
#index to start count
i=0
#input user name
username=input("your user name ").strip().lower()
#print if user name exict
print(listname.__contains__(username))
#loop until input correct user name or sign up
while listname.__contains__(username).__eq__(False):
    print("input correct name")
    username=input("your user name ").strip().lower()
    #to check if you wont to sing up 
    logicSign=input("put yes or no if you wont to sign up new user ").strip().lower()
    if logicSign.__eq__("yes"):
        #to put new user data
        username=input("your user name ").strip().lower()
        listname.append(username)
        passwordIn=input("put your  new password\n ").strip()
        listpassword.append(passwordIn)
        email.update({username:input("your email is ").strip().lower()})
#to check if user is sing up in site
if listname.__contains__(username):
#loop for trais password that give 4 trais
 while i<=trais:
     passwordIn=input("put your password\n ").strip()
     indexUser=listname.index(username)
     #end loop if password is correct
     if passwordIn==listpassword.__getitem__(indexUser):
        #i=4
        print(f"welcome {username}")
        break#dont print try later
     else :
        print("password wrong")
            
     i+=1
#if all trais end and you wont to change password      
 else:
    emailGet=input("yor email is : ").strip()
    #to check email is exict with thier user
    if email[username]["email"]==emailGet:
        #to check if that your email by resive code in it 
        email.update({username:{"email":emailGet,"codeResive":[random.randint(0,9),random.randint(0,9),random.randint(0,9)]}})
        print(email.get(username))    
        #put code you resive 
        code=int(input("put the code resive in email  ").strip())
        #to check if code put is correct with email can change password
        if int(code/100)==email[username]["codeResive"][0] and int((code%100)/10) ==email[username]["codeResive"][1]  and code%10==email[username]["codeResive"][2]:
          passwordIn=input("put your  new password\n ").strip()
          indexUser=listname.index(username)
          listpassword.pop(indexUser)
          listpassword.insert(indexUser,passwordIn)
          print("password update ")

    
print("welcome")     
