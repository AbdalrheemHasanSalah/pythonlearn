#--------------------------------#
#--Errors And Exceptions Raising--
#--------------------------------#
#[1] Exceptions is runtime Error Reporting Mechanism
#[2] Exceptions Gives You the Massage to understand The problem
#[3] Traceback Gives You The line to look fo the code in this line
#[4] Exceptions Have type (syntax error,Index Error,KeyError,Etc...) 
#[5] Exceptions List https://docs.python.org/3/liprary/exceptions.html
#[6] raise keyword Used To Raise Your own Exceptions
#---------------------------------------------------------------------

x=10
y=0
if y==0:
   # raise Exception("The number {y} Is zero ")#Exception: The number {x} Is zero

    print(f"This will not print")
else :
    print(f"{x/y}")

print('print Message After If condition')

y='abd'

if type(y)!=int:
    pass
   # raise ValueError("only Number Allowed") #ValueError: only Number Allowed

#print('print Message After If condition')

#--------------------------------#
#--      Exceptions Handling   --#
#--    Try|Except|Else|Finally --#
#--------------------------------#
# Try => Test the code for error
# Except => Handle The error 
#--------------------------------
# Else => If No Error
# Finally => Run the code 
#--------------------------------


print("*"*15)

#if put string
number=int(input("write Your Age: "))#ValueError: invalid literal for int() with base 10: '   '

print(number)
print(type(number))


try: # test code 
    number=int(input("write Your Age : "))
except: # Handle the Error if you found 
    print("this is not int")        
else:#if theres no Error If its found 
    print("Good,This Is int")
finally:

    print("print From Finally whatever")

try:
    print(10/0)
    print(x)
    print(int("hello"))

except ZeroDivisionError:
    print("cant divide")    
except NameError:
    print("type error not found")
except:
    print("other error")