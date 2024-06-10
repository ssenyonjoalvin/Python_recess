#LIst is a collection which is ordered and  changeable and allow duplicate members
#To use a list you must declare it first  with square brackets and separate values with a comma

"""
#1
list1 = [1,2,3,4,4,5,[12,34,56],'s','erty']
print(list1)
print(type(list1))


#2
x = list()
tuple1 = (1,2,34,5)
x = list(tuple1)
print(x) 

#operations include
#indexing,slicing , adding ,multiplying and checkingfor membership
l = ['money', 'majja', 'mula']
print(l[-2]) #negative count from the right
print(l[1:]) #slicing fecthes sections
print(l[:1])


#list methods
#Del()
x = [1,2,3,4,6,5,4]
del(x[4])
print(x)
#to delete a complete list we use 
del(x)
print(x)
"""
#Append() : add an item to the end of the list
x = [1,2,3,4,6,5,4]
x.append(12)
x.append(34)
print(x)

#Extend()
m = [5,7,8,9,33,3]
s = [9,0,1,23,3,334]
m.extend(s)
print(m)
#Insert()