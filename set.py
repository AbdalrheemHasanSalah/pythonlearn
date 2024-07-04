#-------------------------------
#          set
#-------------------------------

#[1]set item are enclosed with curly braces
#[2]set item are not orderd and not indexing
#[3]set indexing and selicing cant be done
#[4]set has immutable data type (number,string,tuple)list and dict are not
#[5]item is unique
#--------------------------------

#not orderd and not indexing
set1={1,2,"b",3,"a"}
print(set1)
#print(set1[0])#TypeError: 'set' object is not subscriptable

#set can not selicing
#print(set1[0:2])#TypeError: 'set' object is not subscriptable


#has immutable data type only

#set1={1,2,"b",3,"a",[1]}
#print(set1)#TypeError: unhashable type: 'list'
#set1={1,2,"b",3,"a",(1)}
#print(set1)#TypeError: unhashable type: 'list'


set1={1,2,"b",3,"a",(1,2)}
print(set1)#{1, 2, 3, (1, 2), 'a', 'b'}


#item is unique

set1={1,2,"b",3,"a",(1,2),"a","a"}
print(set1)#{1, 2, 3, (1, 2), 'a', 'b'}





##############################
        #set Method#
##############################



print("-"*40)

#clear()

#a={([1])}
#print(a)#TypeError: unhashable type: 'list'
a={1,2,3}
a.clear()
print(a)#set()

print("-"*40)

#union(set) or  |
a={1.2,3}
b={4,5,6}
d={7,8}
print(a|b)#{1.2, 3, 4, 5, 6}
print(a.union(b))#{1.2, 3, 4, 5, 6}
print(a.union(b,d))#{1.2, 3, 4, 5, 6, 7, 8}
a.union(b)
print(a)#{1.2, 3}

print("-"*40)


#add(value)
d={1,2,3}
d.add(4)
d.add(5)
print(d)#{1, 2, 3, 4, 5}

print("-"*40)

#copy()
#shallow copy that mean any change in main value doesnot effact to copy
a={1,2,3,4}
f=a.copy()

print(a)#{1, 2, 3, 4}
print(f)#{1, 2, 3, 4}


a.add(5)
print(a)#{1, 2, 3, 4, 5}
print(f)#{1, 2, 3, 4}


print("-"*40)

#remove(value)
#give error if value not found
a={1,2,3}
a.remove(1)
print(a)#{2, 3}

#a.remove(4)
#print(a)#KeyError: 4

print("-"*40)

#discard(value)
#discard() remove value if not found do nothing
a={1,2,3,4}
a.discard(1)
a.discard(7)
print(a)#{2, 3, 4}

print("-"*40)


#pop()
#pop random elemant of set becose that have not index
a={"one","two ",True,1,2}
print(a.pop())#random value

print("-"*40)


#update(set)
#Update the set, adding elements from all others.
# can use it with list

a={1,2,3}
b={4,5,6}
a.update([7,8,9])
a.update(b)
print(a)#{1, 2, 3, 4, 5, 6, 7, 8, 9}

print("="*40)#========================================


#difference(set)
#get difference from first set by seconed set
a={1,2,3,4,5}
b={1,2,3,"one","two"}
print(a)#{1, 2, 3, 4, 5}
print(a.difference(b))#{4, 5}
a.difference(b)
print(a)#{1, 2, 3, 4, 5}
print(a-b)#{4, 5}

print("="*40)#========================================


#difference_update(set)
#make update on the fisrt set by difference on seconed
a={1,2,3,4,5}
b={1,2,3,"one","two"}
print(a)#{1, 2, 3, 4, 5}
a.difference_update(b)
print(a)#{4, 5}
print(a-b)#{4, 5}

print("="*40)#========================================

#intersection(set)
#make and between first and second set 
#the change does not effact to first set and seconed
a={1,2,3,4,5}
b={1,2,3,"one","two"}
print(a)#{1, 2, 3, 4, 5}
print(a.intersection(b))#{1, 2, 3}
print(a)#{1, 2, 3, 4, 5}

print("="*40)#========================================


#intersection_update(set)
#make and between first and second set 
#the change do effact to original set 
a={1,2,3,4,5}
b={1,2,3,"one","two"}
print(a)#{1, 2, 3, 4, 5}
print(a.intersection_update(b))#print None put thay effact to set 
a.intersection_update(b)#a&b
print(a)#{1, 2, 3}


print("="*40)#========================================


#symmetric_difference(set)
#to get all difference value between two set from there with out update in original set
a={1,2,3,4,5}
b={1,2,3,"one","two"}
print(a)#{1, 2, 3, 4, 5}
print(a.symmetric_difference(b))#a^b #{'one', 4, 5, 'two'}
print(a)#{1, 2, 3, 4, 5}

print("-"*40)#========================================


#symmetric_difference(set)
#to get all difference value between two set from there with update in original set
a={1,2,3,4,5}
b={1,2,3,"one","two"}
print(a)#{1, 2, 3, 4, 5}
#print(a.symmetric_difference_update(b))#a^b #None #if i do symmetric_defference_update return to original value 
a.symmetric_difference_update(b)
print(a)#{'one', 4, 5, 'two'}

print("-"*40)#========================================


#issuperset(set)
#Report whether this set contains another set.
a={1,2,3,4,}
b={1,2,3}
c={1,2,3,4,5}
print(a.issuperset(b))#true
print(a.issuperset(c))#false

print("="*40)#========================================


#issubset(set)
#Report whether another set contains this set.

a={1,2,3,4,}
b={1,2,3}
print(a.issubset(b))#false
print(b.issubset(a))#true
print(a.issubset(a))#true

print("="*40)#========================================

#isdisjoint()
#Return True if two sets have a null intersection.

a={1,2,3,4}
b={1,2,3}
c={10,11,12}
print(a.isdisjoint(b))#false
print(a.isdisjoint(c))#true
print(c.isdisjoint(a))#true

