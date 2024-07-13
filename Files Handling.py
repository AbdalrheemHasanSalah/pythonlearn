#-------------------------#
#-----Files Handling------#
#-------------------------#

import os

print(os.getcwd)# give the directory of files dir
print(os.path.dirname(os.path.abspath(__file__)))#diectory for open file
os.chdir(os.path.dirname(os.path.abspath(__file__)))#change current work directory
print(os.getcwd)
print(os.path.abspath(__file__))#give abs path with this file code

#files=open("C:\Users\Abdal\nabd.txt")#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape  
file=open("python1.txt","w")

files=open(r"C:\Users\Abdal\nabd.txt")#to get all like string with out error  
file=open("python1.txt")


file=open("python1.txt","r")

print(file)#<_io.TextIOWrapper name='python1.txt' mode='r' encoding='cp1252'>
print(file.name)
print(file.mode)
print(file.encoding)

#######read=>files#######

#all oprator read  continues from outher 
#that mean '
#if raed method give all continis file the outher methon didnot print thing

print(file.read())#print file continis
print(file.read(10))#print char theat give number from first

print(file.readline(4))#print char  of line by  give number char
print(file.readline())#read the char from before line that get sum char not all  continue it
print(file.readline())#read line


print(file.readlines())#print all lines in list
print(file.readlines(5))#print char of line that give number char in list
print(type(file.readlines()))#<class 'list'>



for line in file:
    print(line)
    
    if line.find("2"): 
        break


file.seek(15)#to get cursor position to number give determine

print(file.read())

file.close()


######write=>Files######

file=open("python.txt","w")
file.write("line one\n")
file.write("line two\n")

file.write("line\n"*10)

list=["abd\n","abdalrheem\n","learnd\n","python\n"]

file.writelines(list)#write from list
file.close()
######write=>append######

file2=open("python2.txt","a")
file2.write("new line from append")
#file2.truncate(5)#to rewrite with give number char
print(file2.tell())#give the position of cursor in txt


file2.close()

import os
os.remove("python.txt")

os.remove("python1.txt")
os.remove("python2.txt")










