#_________________________________
#          dictionary
#_________________________________


#[1]dict item are enclosed in curly braces
#[2]dict:item are contains key : value
#[3]dict need to be immutable => (number,string,tuple) list not allowed
#[4]dict value can be any type of data
#[5]dict key must be unique
#[6]dict key is not orderd you access its element with key
#------------------------------------ 

#dictionary

user={
"name":"abd",
"age":21,
"country":"palestine",
"skills":["c","c++","java","python"],
#[1,2,3]#TypeError: string indices must be integers, not 'tuple'
(1,2):"test",
True:"true",
#"name":"abd2"# put the last value of it dict
}

print(user)#{'name': 'abd', 'age': 21, 'country': 'palestine', 'skills': ['c', 'c++', 'java', 'python'], (1, 2): 'test', True: 'true'}
print(user['country'])#palestine
print(user.get('country'))#palestine

print(user.keys())#dict_keys(['name', 'age', 'country', 'skills', (1, 2), True])
print(user.values())#dict_values(['abd', 21, 'palestine', ['c', 'c++', 'java', 'python'], 'test', 'true'])

print("_"*40)
#two-dimensional dictionary

languages={
"one":{
    "name":"python"
},
"two":{
"name":"java"
},
"three":{
    "name":"c++",
    "name2":"c"
}

}

print(languages)#{'one': {'name': 'python'}, 'two': {'name': 'java'}, 'three': {'name': 'c++'}}
print(languages["two"])#{'name': 'java'}
print(languages["three"]["name2"])#c


print(len(languages))#3
print(len(languages["three"]))#2

print("_"*40)

#creat dictionary from variables


one={
    "name":"python"
}
two={
"name":"java"
}

three={
    "name":"c++",
    "name2":"c"
}
all_languages={
 "one" :one,
 "two" :two,
 "three" :three
}

print(all_languages)#{'one': {'name': 'python'}, 'two': {'name': 'java'}, 'three': {'name': 'c++', 'name2': 'c'}}



#======================================
#            dictionary Method
#======================================

print("-_-"*15)

#clear()

user={
   "name":"abd",
   "age" :"21" 
}
user.clear()
print(user.clear())#None
print(user)#{}



print("-_-"*15)

#update(dict)
user={
   "name":"abd",
   "age" :"21" 
}
user.update({"country": "palestine"})
print(user)#{'name': 'abd', 'age': '21', 'country': 'palestine'}
user['state']='barqa'
print(user)#{'name': 'abd', 'age': '21', 'country': 'palestine', 'state': 'barqa'}

print("-_-"*15)

#copy()

user={
   "name":"abd",
   "age" :"21" 
}

usercopy=user.copy()
print(usercopy)#{'name': 'abd', 'age': '21'}
user.update({"country": "palestine"})
print(user)
print(usercopy)

#keys() + values()
print(user.keys())#dict_keys(['name', 'age', 'country'])
print(user.values())#dict_values(['abd', '21', 'palestine'])

print("-_-"*15)


#setdefault()
user={
    "name": "abd"
}
print(user)
print(user.setdefault("age","21"))
print(user)#{'name': 'abd', 'age': '21'}

print("-_-"*15)

#popitem()
user = {
  "name":"abd",
  "age":"21"
 }
print(user.popitem())#('age', '21')
user.update({"skill":"c++"})
print(user.popitem())#('skill', 'c++')

print("-_-"*15)

view ={
   "name":"abd",
   "age":"21"
}

allitem=view.items()
print(view)#{'name': 'abd', 'age': '21'}
print(allitem)#dict_items([('name', 'abd'), ('age', '21')])
view.update({"number":"0"})
print(view)#{'name': 'abd', 'age': '21', 'number': '0'}
print(allitem)#dict_items([('name', 'abd'), ('age', '21'), ('number', '0')])


print("-_-"*15)



#fromkeys()

a=("one","two","three")
b="A","B","C"
print(dict.fromkeys(a,b))
