#---------------------------------------------------
#--Practical => loop on Many Iterators with zip()--
#---------------------------------------------------

# zip() Return A zip Object Contains All object
# zip() Length Is the length of lowest object

#-----------------------------------------------

list_=["one","two","three","four"]
list2=[1,2,3,4]
set={1,2,3,4}
tuple=("A","B","C")
dict={
    "name":"abd",
    "age":21,
    
}

for item1,itemset,item2,item3 in zip(list_,set,tuple,dict):
    print(f"from list is =>{item1} and set is => {itemset}")
    print(f"from tuple is =>{item2}")
    print(f"from dict is {item3} and value =>{dict[item3]} ")


print("#"*20)

ultimatelist=zip(list_,list2)
print(ultimatelist)#<zip object at 0x00000187B3DF3C00>
print("#"*20)

for item in ultimatelist:
    print(item)


