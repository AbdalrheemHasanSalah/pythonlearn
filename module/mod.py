name=5
age=0
def setname(aname):
    global name
    name=aname

def getname():
    return name  
  
def sayHello():
    print(f"hello {name}")

def setage(age2):
    global age
    age=age2
    
def getage():
    return age

def details():
    print(f"your name {getname()} your age {getage()}")    


setname("abd")
sayHello()
setage(21)
details()