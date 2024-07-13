#____________________________#
#-------loop for-------------#
#____________________________# 


listnumber=[0,1,2,3,4,5,6,7,8,9]
for number in listnumber:
    #print(number)
    if number%2==0 and number!=0:
        print(f"{number} is even")
    elif number%2==1:
        print(f"{number} is odd")
    else:
        print(" is zero")  

string=input("string to print char").strip()
for latter in string:
    print(latter)

##loop and dict##
dic={
    "python":"%70",
    "c++":"85%",
    "c":"%95",
    "java":"%79"
}

myRange=range(1,100)
for number in myRange:
    print(number)#print from 1 to 99

for num in dic:
    print(num)#print key

for num in dic:
    print(f"key is {num} : valus is {dic[num]}")    

for num in dic.values():
    print(num)#print values

#########Nested loop###########
myRange=range(0,5)
for num1 in myRange:
    for num2 in myRange:
        print(f"{num1}{num2}")  


dictNested={
    "abd":{
    "python":"%70",
    "c++":"85%",
    "c":"%95",
    "java":"%79"},
    "abdalrheem ":{
    "python":"%70",
    "c++":"85%",
    "c":"%95",
    "java":"%79"}
}

for name in dictNested:
    print(f"name is {name}")
    for skil in dictNested[name]:
        print(f"{skil}=>{dictNested[name][skil]}")


#######################################
#######break and continue and pass#####
#######################################

myRange=range(0,10)

for num in myRange:
    if num== 5:
        break
    print(f"num is {num}")
print("#"*15)
for num in myRange:
    if num==0:
        continue#dont print 0
    print(num)
print("#"*15)
#for num in myRange:
 #   if num==0:
        #error
 #   print(num)
 


