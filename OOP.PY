#----------------------------------------------------------#
#--   Opject Oriented Programming => Class syntax info   --#
#----------------------------------------------------------#
#[1] _init_ Method called from class  
#[2] _init_ is initialize The date For the object
#[3] Any method with two underscore in the start and end its called dunder or Magic method
#[4] self refer to the current Instance Created From the class and must be first param
#[5] self can be named anything
#[6] in python you dont need to call new() keyword to create object

#--Class Method:
#-Marked with @classmethod Decorator To Flag Its As class Method
#-it take cls parameter not self to point to the class not instance
#-used when do someting with class it self
#static Method :
#-it takes no parameter

#Instance Attributes:instance define inside the constructor

# syntax
# class Name:
#       constructor => Do Instantion [create Instance From A class]
#       Each instance is separate object
#       def _init_(self,other_Data)
#            Body of function


class Member:
    list=["hell","chat"]
    user_num = 0
    @classmethod
    def shownum(cls):
        print(f"user number is {cls.user_num}")
    @staticmethod    
    def sey_hello():
        print("hello from static")
    def __init__(self,first_name,middle_name,last_name,) -> None:
        print("new member has been added ")
        self.name=first_name
        self.middle_name=middle_name
        self.lastname=last_name
        Member.user_num+=1
        pass
    def full_name(self):
        if self.name in Member.list:
             pass
          # raise ValueError("Name not allowed")#ValueError: Name not allowed
        else:
            return f"{self.name} {self.middle_name} {self.lastname}"
    def hello_mr(self):
        return f"hello MR {self.name}"
    def get_all_info(self):
        return f"{self.hello_mr()} your full info {self.full_name()}"



print(Member.user_num)

Member("abd","hasan","salah")
Member("abd","hasan","salah")
Member("abood","hasan","salah")

print(Member.user_num)#3


print("*"*20)

member=Member("abd","hasan","salah")
member2=Member("abood","hasan","salah")
member3=Member("abdalrheem","hasan","salah")
member4=Member("hell","chat","hell")

print(Member.user_num)#7


print("*"*20)

print(member.__class__)
print(dir(Member))

print(member.name,member.middle_name,member.lastname)#abd hasan salah
print(member2.name,member2.middle_name,member2.lastname)#abood hasan salah
print(member3.name,member3.middle_name,member3.lastname)#abdalrheem hasan salah
member.sey_hello()#hello from static

print("*"*20)
my_string="abdalrheem"
print(type(my_string))
print(my_string.__class__)
print(dir(str))

print("*"*20)

member.shownum()#user number is 7
print(member.full_name())#abd hasan salah
print(member.hello_mr())#hello MR abd
print(member.get_all_info())#hello MR abd your full info abd hasan salah
print(member4.full_name())#ValueError: Name not allowed
print(member.get_all_info())

print("*"*20)


print(member2.full_name())
#print(member.full_name(member2))


#####################################################
#--   Opject Oriented Programming => Inheritance  --#
#####################################################

print("*"*20)


class Food: #Base Class
      def __init__(self,name,price):
          self.name=name
          self.price=price + 20

          print(f"{self.name} from Base class")
      def eat(self):
          print("Eat method from base class")     

class Apple(Food): #Derived Class
        def __init__(self,name,price,amount):
            #Food.__init__(self,name)#create instance from base class
            super().__init__(name,price)
            self.name=name
            self.price=price + 20
            self.amount=amount
            print(f"{name} from derived and price is {self.price} and amount {self.amount}")


food_one=Food("pizza",50)#pizza from Base class
food_two=Apple("pizza",150,500)#pizza from derived and price is 170 and amount 500
                        #pizza from derived
food_two.eat() #Eat method from base class

print("*"*20)


##############################################################
#--   Opject Oriented Programming => Multiple Inheritance  --#
##############################################################

print("*"*20)

class base_one:
     def __init__(self) -> None:
          print("base one")
     def func_one(self):
          print("one")     
class base_two:
     def __init__(self) -> None:
          print("base two")
     def func_two(self):
          print("two")      
class Derived(base_one,base_two):
     pass

my_var=Derived()

print(Derived.mro())#[<class '__main__.Derived'>, <class '__main__.base_one'>, <class '__main__.base_two'>, <class 'object'>]
print(my_var.func_one)#<bound method base_one.func_one of <__main__.Derived object at 0x0000019FD6AE6A50>>
print(my_var.func_two)#<bound method base_two.func_two of <__main__.Derived object at 0x0000019FD6AE6A50>>

my_var.func_one()#one
my_var.func_two()#two


class base:
     pass
class derivedone(base):
     pass
class derivedtwo(derivedone):
     pass


print("*"*20)



##############################################################
#--   Opject Oriented Programming => Polymorphism          --#
##############################################################

print("*"*20)


class A:
     def dosomething(self):
          print("hello From class A")
         # raise NotImplementedError("Derived class must Implemented this method")
class B(A):
     def dosomething(self):
          print("hello  From class B")
class C(A):
     pass

instance=A()
instance.dosomething()


instance=B()
instance.dosomething()


instance=C()
instance.dosomething()#NotImplementedError: Derived class must Implemented this method


print("*"*20)


##############################################################
#--   Opject Oriented Programming => Encapsulation         --#
##############################################################

# Encapsulation
# Restrict Access to data stored in Attirbutes and Methods

# Public
# Every Attirbutes and method that we used is public

# Protected
# Attirbutes and method prefixed with one underscore_

#privte 
# Attirbutes and method prefixed with one underscore__
print("*"*20)


class Member:
     def __init__(self,name):
          self.name=name #public

one=Member("abd")    

print(one.name)

one.name="abdalrheem"
print(one.name)




class Member:
     def __init__(self,name):
          self._name=name  # Protected

one=Member("abd")    

print(one._name)

one._name="abdalrheem"
print(one._name)


class Member:
     def __init__(self,name):
          self.__name=name  # privte
     def say_hello(self):
          return f"hello {self.__name}"
one=Member("abd")    



one.__name="abdalrheem"
print(one.__name)
print(one.say_hello())

print("*"*20)

##############################################################
#--   Opject Oriented Programming => Getters And Setters   --#
##############################################################    
     
class Member:

     def __init__(self,name):
          self.__name=name  # Protected
     def say_hello(self):
          return f"hello {self.__name}"
     def set_name(self,new_name):
          self.__name=new_name
     def get_name(self):# Getter 
          return self.__name
one=Member("abd")    


print(one.say_hello())
#one._Member.__name = "abdalrheem"
#print(one._Member.__name)

print(one.get_name())
one.set_name("abood")
print(one.get_name())

print("*"*20)




##############################################################
#--   Opject Oriented Programming => @Property Decorator   --#
##############################################################    

class Member:

     def __init__(self,name,age) -> None:
          self.name=name
          self.age=age
     def sey_hello(self):
          return f" hello {self.name}"     
     @property
     def age_in_days(self):
          return self.age*365

one=Member("abood",21)

print(one.name)
print(one.age)
print(one.sey_hello())
print(one.age_in_days)#7665
#print(one.age_in_days())#TypeError: 'int' object is not callable




################################################################
#--   Opject Oriented Programming =>ABCs Abstract Base Class --#
################################################################

#-class called abstract class if it has one or more Abstract method
#-abc module in python Provides Infrastructure for Defining Custom Abstract Base Class
#-by adding @absttractmethod Decorator on the method 
#-Abcmeta class Is a metaclass used for defining Abstract Base class
#-------------------------------------------------------------------------------------

from abc import ABCMeta,abstractmethod

class programming(metaclass=ABCMeta):
     @abstractmethod
     def has_oop(self):
          pass
     @abstractmethod
     def has_name(self):
          pass
class python(programming):
       def has_oop(self):
          return"yes"
   

class pascal(programming):
     def has_oop(self):
          return"NO"
     def has_name(self):
          return"pascal"
one=pascal()

print(one.has_oop())
print(one.has_name())
