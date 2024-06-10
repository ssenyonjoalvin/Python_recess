#Array in Python can be created by importing an array module.
import array as arr

 #array(data_type, value_list) 
 # arrayName = array(typecode, [initializer])
 #is used to create array in Python with data type and value list specified in its arguments. 

students_marks = arr.array('i',[2,4,5,6,56,65])
print(type(students_marks))
print(students_marks)



#to print each element or loop through the arrays
#for x in students_marks :
 #   print(x)
  #  print(" ")


#for x in range(len(students_marks)) :
 #   print(students_marks[x])
  #  print(" ")


#Joining two arrays together
a = arr.array('d' , [1.6,3.7,4.4,5.3,6.2,7.4])

b = arr.array('d' , [1.2,3.4,5.6,7.8])

c = arr.array('d')

c = a + b
print(c)
print(" ")

#to access/searching for an individual elements of the array
print('the first element is ',c[0])
print('the second element is ',c[1])
print('the last element is ',c[-1])
print('the second last element is ',c[-2])

#deleting elements from an array
del c[3]
print(c)
print(" ")
print(" ")




numbers = arr.array('i' , [1,4,23,3,4,56,54,4,4,4,4])
#modifying elements in the array
print ("the array befor updating",numbers)

numbers[3]= 7
print ("the array after updating",numbers)
print(" ")

#counting number of occurences of an element in the array 
count = numbers.count(4)
print("the number occurs",count,"number of times")
print(" ")


#adding elements in array
numbers.append(89)
numbers.append(1)
numbers.append(96)
print(numbers)
print(".......................work............................")
print(students_marks[2:3])
# numbers.clear()

print(dir(numbers))

#insert()
numbers.insert(3,10000)
print(numbers)

