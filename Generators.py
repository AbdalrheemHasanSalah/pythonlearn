#-------------------------#
#       Generators        #
#-------------------------#

#[1]  Generators Function with "yield" keyword Instead of return 
#[2]  It support Iteration and return generators iterator by calling "yield"
#[3]  Generators can have one or more "yield"
#[4]  By using next() it resume From Where It Called "yield" Not From bigining 
#[5]  when called, Its Not start automatically, Its only Give you the control
#--------------------------------------------------------------------------------


def Generators():
    yield 1
    yield 2
    yield 3
    yield 4

print(Generators())
Generators()
generat=Generators()

print(next(generat))
print(next(generat))
print(next(generat))
#for number in generat:
#    print(number)#print4

print(next(generat))
print("#"*15)

for number in Generators():
    print(number)






