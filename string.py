#string

#escape sequence char

#\b => back space remove char
print("hello\b world") #remove the first before char ( remove o)

#escape new line+\
print("hello\
python\
world"    
)# hellopythonworld

#escape back slash 
print("hello\\")#hello\

#escape single quote 
print('hello  \' test\' ')#hello  ' test'

#escape double quote
print("hello \"test\" ")#hello "test"


#line feed
print("hello first \n second line")# print hello first
                                    #       second line

#carriage return 
print("123456\rabcd")# print abcd56

#horizontal tap
print("hello \t python")#hello    python

#char hex value
print("\x41\x42\x44")#ABD



#concatenation



my_str="hello"
my_str2="python"
print(my_str+""+my_str2)#hellopython
a="first\
seconed\
third\
"
b="A\
b\
c\
"

print(a+" "+b)#firstseconedthird Abc


string_one="python 'hello' programmer "
string_two='python "hello" programmer '
print(string_one)#python 'hello' programmer
print(string_two)#python "hello" programmer

string_truble="""a\
b'test'\"test2"
c"""
string_truble2='''one
two"test"\'test1'
three'''
print(string_truble)#ab'test'"test2"  
                    #c

print(string_truble2)#one
                     #two"test"'test1'
                     #three




#indexing (Access Single item)



string_my="hello python"


print(string_my[0])#h
print(string_my[10])#o


print(string_my[-1])#first char from end (n)
print(string_my[-5])#start from end (y)




#Slicing (Access Multiple sequence items)


print(string_my[:])#print full data (hello python)
print(string_my[0:11])#end not include (hello pytho)
print(string_my[5:10])# pyth
print(string_my[:10])#start from 0 (hello pyth)
print(string_my[5:])#go to end (python)

print(string_my[0::1])#full data(hello python)
print(string_my[::1])#full data (hello python)
print(string_my[::2])#hlopto
print(string_my[::3])#hlph
print(string_my[5:10:1])#pyth
print(string_my[-5:10:2])#yh
print(string_my[-10:10:2])#lopt



#string method

space_string_my="     hello python 2d    "
space_string_my2="######hello python######"

#len
#len(string)
print(len(string_my))#print 12
print(len(space_string_my))#print 21

#strip to remove the spaces or any char before or after string 
#strip(),strip("char")
print(space_string_my.strip())#hello python 2d
print(space_string_my.rstrip())#     hello python 2d
print(space_string_my.lstrip())#hello python 2d

print(space_string_my2.strip("#"))#hello python
print(space_string_my2.rstrip("#"))#######hello python
print(space_string_my2.lstrip("#"))#hello python######

space_string_my2="aaaaaaahello python######"
print(space_string_my2.strip("a"))#hello python######"


#title and capitalize
print("is title :",space_string_my.istitle())
print(space_string_my.title())#first  char capital char after diget make capital (     Hello Python 2D    )
print(space_string_my.capitalize())#char after diget didnot made capital (     hello python 2d   )
print("is title :",space_string_my.istitle())

#zfill to fill zero before string number
#zfill(number of zero)
a,b,c="1","11","111"
print(a.zfill(3))#001
print(b.zfill(3))#011
print(c.zfill(3))#111

#upper and lower

name="Abd"
print(name.upper())#ABD
print(name.lower())#abd


#split 
#split(),split("char"),split("char",number of splited sting)
a="hello python and c++"
print(a.split())#['hello', 'python', 'and', 'c++']
b="hello-python-and-c++"
print(b.split())#['hello-python-and-c++']
print(b.split("-"))#['hello', 'python', 'and', 'c++']
c="hello-python-and-c++-sql"
print(c.split("-",2))#['hello', 'python', 'and-c++-sql']
print(c.rsplit("-",2))#['hello-python-and', 'c++', 'sql']

#center to add spaces or any char to string
#center(number of all charwith string),center(number of all charwith string,"char")

a="abdalrheem"
print(a.center(20))#     abdalrheem     # put spaces
print(a.center(20,"#"))#####abdalrheem#####  #put hashes
print(a.center(10,"-"))#abdalrheem #center method didnot efact it string 
                                   #just append if arrgment is less than arrgement of string
print(a.center(11,"-"))#-abdalrheem


#count to get count of any give char or string
#count(char or string),count(char or string,strat index ,end index)
print(a.count("e"))#2
a="HeLLO abdalrheem programmer!"
print("count of e char from 6 to end :",a.count("e",6))#3 from 6 to end
print("count of e char from 6 to 16 :",a.count("e",6,16))#2 from 6 to 16


#swapcase() to make Uppercase letter to lowercase letter and opposite

print(a.swapcase())#hEllo ABDALRHEEM PROGRAMMER!


#startswith give bool answer if start with that char
#startswith("char"),startswith("char",start index,end index)

print("is start with that char \"H\" :",a.startswith("H"))#TRUE
print("is start with that char \"a\" :",a.startswith("a"))#FALSE
print("is start with that char \"a\" from 6 to 18 :",a.startswith("a",6,18))#TRUE

#endswith give bool answer if end with that char
#endswith("char"),endswith("char",start index,end index)

print("is end with that char \"!\" :",a.endswith("!"))#TRUE
print("is end with that char \r!\" :",a.endswith("r"))#FALSE
print("is end with that char \"m\"from 6 to 16 :",a.endswith("m",6,16))#TRUE


#get index of char
#index("char"),index("char",startindex,endindex)
a="HeLLO abdalrheem programmer!"
print("index of a char is:",a.index("a"))#6 print first char from left 
print("index of a char is start from 7:",a.index("a",7))#9 print first char find
#print(a.index("a",10,20))  # give an error if didnot found the char 
print("index of a char is start from 10 to infinte:",a.index("a",10,9999999))#22 give the value correct if give the end large then size
print("index of a char is start from 0:",a.index("a",0))#6 start index should include in method

#get index of char
#find("char"),find("char",startindex,endindex)

print("index of a char is:",a.find('a'))#6
print("index of a char is start from 7:",a.find("a",7))#9
print("index of a char is start from 10 to 20:",a.find("a",10,20))#-1 is give -1 then error
print("index of a char is start from 10 to 12:",a.find("a",10,12))#-1 is give -1 then error

#fill index with give char or space
#rjust(width,"char"),ljust(width,"char")
a="HeLLO abdalrheem programmer!"
print(a.rjust(10))#HeLLO abdalrheem programmer! if rjust less than size index print the string just
print(a.rjust(30))#  HeLLO abdalrheem programmer! print the space after all index to fill the width give
print(a.rjust(40,"#"))#############HeLLO abdalrheem programmer! fill width with give char

print(a.ljust(10))#HeLLO abdalrheem programmer!
print(a.ljust(30))#HeLLO abdalrheem programmer! 
print(a.ljust(40,"#"))#HeLLO abdalrheem programmer!############

#to get list of string lines
#splitlines()

e = """first
second
third"""
print(type(e))
print(e)
print(e.splitlines())
print(type(e.splitlines()))

f="first\nsecond\nthird"
print(type(f))
print(f)
print(f.splitlines())

#to give tap at \t loction by integer you give 
#expandtabs(int)

a="first\tsecond\tthird"
print(a.expandtabs())#first   second  third  #if didnot give int \t mean four taps
print(a.expandtabs(2))#first second  third   #if give int < 4 taps shrink than \t
print(a.expandtabs(15))#first          second         third #add taps to int 


#space cheak
#isspace()
space=" "
print("is space :",space.isspace())#true
space=""
print("is space :",space.isspace())#false

a="hello python"
print("is lower",a,":",a.islower())#true
a="Hello python"

print("is lower ",a,":",a.islower())#false

a="abd_hasan"
print("\nis identifire ",a,":",a.isidentifier())#true
a="abd111"
print("is identifire ",a,":",a.isidentifier())#true
a="abd--hasan"
print("is identifire ",a,":",a.isidentifier())#false

a="abd_hasan"
print("\nis alpha ",a,":",a.isalpha())#false
a="abdhasan"
print("is alpha ",a,":",a.isalpha())#true


#to replace char
#replace("old char","new char"),replace("old char","new char",count)
a="one two three one one one"
print("\n",a.replace("one","1"))# 1 two three 1 1 1
print(a.replace("one","1",2))#1 two three 1 one one
print(a.replace("e","1"))#on1 two thr11 on1 on1 on1
print(a.replace("ne","1"))#o1 two three o1 o1 o1



#to convert form itrable -list or tuple- to string
#" ".join(itrable),"char".join(itrable)
my_list=["abd","hasan","salah"]
print(type(my_list))
print(" ".join(my_list))
c=" ".join(my_list)
print(type(c))
print("-".join(my_list))
print(",".join(my_list))




###########################

#####String Formatting#####

############################

name="abdalrheem"
age=21
rank=10

print("My name is "+name)
#print("My name is "+name+"my age is :"+age)#Error: can only concatenate str (not "int") to str
print("My name is :%s and my age : %s rank is : %s"%(name,age,rank))#give all type with sting type do type casting
                                                                   #My name is :abdalrheem and my age : 21 rank is : 10

print("My name is : %s ,my age is: %d ,my rank is:%f"%(name,age,rank))#give all with spicfic type i give
                                                                     # My name is : abdalrheem ,my age is: 21 ,my rank is:10.000000

#control floting number
print("rank is :%.2f",rank)#rank is :%.2f 10 if i put (,) make concatenate
print("rank is :%.2f"%rank)#rank is :10.00 to determine number of Decimal places 
print("rank is :%.5f"%rank)

#truncate string
print("name is :%.3s"%(name))#name is :abd to determine number of char for string
print("name is :%.3s"%(name)+" Salah")#name is :abd Salah 





#####################################
#####String Formatting new way#####
#####################################


# Replacement %s,%d,%f with {:s},{:d},{:f}

name="abdalrheem hasan salah"
age=21
rank=10

print("My name is "+name)
#print("My name is {} my age is :{}".format(name).format(age))#IndexError: cannot use format in that way
print("My name is :{} and my age : {}rank is : {}".format(name,age,rank))#give all type with sting type do type casting
                                                                   #My name is :abdalrheem and my age : 21 rank is : 10

print("My name is : {:s} ,my age is: {:d} ,my rank is:{:f}".format(name,age,rank))#give all with spicfic type i give
                                                                     # My name is : abdalrheem ,my age is: 21 ,my rank is:10.000000

#control floting number

print("rank is :{:.2f}".format(rank))#rank is :%.2f 10 if i put (,) make concatenate
print("rank is :{:.2f}".format(rank))#rank is :10.00 to determine number of Decimal places 
print("rank is :{:.5f}".format(rank))#rank is :10.00000

#truncate string
print("name is :{:.3s}".format(name))#name is :abd to determine number of char for string
print("name is :{:.3s}".format(name)+" Salah")#name is :abd Salah 


#format money

money=5994941461
print("money : ,%d"%money)#money : ,5994941461
print("money is :{}".format(money))#money is :5994941461
print("money :{:_d}".format(money))#money :5_994_941_461
print("money :{:,d}".format(money))#money :5,994,941,461
#print("money {:$d}".format(money))#ValueError: Invalid format specifier '$d' for object of type 'int' cannot use any char for this format


#Rearrange item 

a,b,c="one","two","three"

print("a =: {} b ={} c={}".format(a,b,c))#a =: one b =two c=three
print(" {} {} {} ".format(c,b,a))#three two one that its change variable not rearrange
print("{1} {0} {2}".format(a,b,c))#two one three
print("{2} {0} {2}".format(a,b,c))#three one three if you input varible and not input that index it run and can repeated  
print("{0} {2}".format(a,b,c))#one three if you input varible and not input that def  it run 

x,y,z=10,20,30
print("{} {} {}".format(x,y,z))#10 20 30
print("{2} {1} {0}".format(x,y,z))#30 20 10
print("{2:.4f} {1:.2f} {0:d}".format(x,y,z))#30.0000 20.00 10  can def it with index


#format the best way and easy for use 
a="abd "
b= 21
print("name {a} and age {b}")#name {a} and age {b}
print(f"name {a} and age {b}")# name abd  and age 21

#Accessing arguments by name: in dict
coord={'x':"5" ,'y':"6"}
print(type(coord))
print("coord= {x},{y}".format(**coord))


#use pyformat to get know more about formating
