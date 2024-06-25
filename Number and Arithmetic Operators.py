
#################

#####Number######

#################


#integer 
print(type(1))
print(type(0))
print(type(-100))
print(type(-110))

#float

print(type(10.0))
print(type(100.0))
print(type(-100.0))
print(type(-0.0546))
print(type(0.0546))

#complex

complexnum=5+6j
print(type(complexnum))
#print("{:complex}".format(complexnum))#ValueError: Invalid format specifier 'complex' for object of type 'complex'
print("{}".format(complexnum))
print("{}".format(complexnum.real))
print("{}".format(complexnum.imag))


#convert type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

#print(float(5+10j))#can not convert from float to complex
#print(int(5+10j))#can not convert from int to complex


################################

########Arithmetic Operators####

################################



#Addition

print(5+5)
print(5+10.5)
print(6.5+4.5)
print(-5+4+6.5)

#suptraction

print(10-5)
print(-30-20)
print(-10--5)#in c++ give an error 
print(100--20)
print(5.66-4.55)





#Multiplication

print(5*10)
print(5.5*5)
print(5.5*5.65)
print((10+2)*100)


#division

print(5/4)#1.25 give it in float not int 
print(int(5/4))#1 in int
print(8.5/4.5)
print(5/4.5)
#print(5/0)#error ZeroDivisionError: division by zero

#modulus

print(8%4)#0 the reminder of division
print(7%5)#2
print(22%5)
print(20%5)

#Exponent

print(2**5)#32 
print(2*2*2*2*2)
print(5**4)



#Floor division


print(100//20)#5
print(100//19)#5
print(110//5)#22
print(120//20)#6
print(130//20)#6
print(140//20)#7
