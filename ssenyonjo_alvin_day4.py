# dictionaries
# creating and using dictionaries
# dictionary methods and operations
"""
dictionaries are a collection of a keys and values
-Unordered
-mutuable 
-indexed with keys

"""
# example 1
# create a dictionary of a student persuing software engineering 
# the keyy mst be your name , age , technology interest, course and year of study
# put your own details

student_dict = {
    "name" : "SSENYONJO ALVIN",
    "age" : 23,
    "technology" : "AI , ML",
    "course"  : "BBSE",
    "year"  : "year3"
}
# access value 
print(student_dict["name"])

# modify values:
# execise 1 : Modify age and technology
student_dict['age'] = '42'
student_dict['technology'] = 'Robotics'

print(student_dict['age'])  
print(student_dict['technology'])

student_dict.update({"age":45})
student_dict.update({"technology":"android"})

print(student_dict)

# adding keys and values 
student_dict['email'] = 'alvin@gmail.com'


# Exercise 2: Remove a key and value from student dictionary

del student_dict['age']
print(student_dict)


# Common Dictionary methods
"""summary
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value



"""

# Example 3: Use the get method to get the value

print(student_dict.get('technology'))

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary
if 'age' in student_dict :
    print("the key 'age ' : ",student_dict["age"]," is inn the dictionary")
else:
    print("its not")

    # keys(),values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

# keys() returns a veiw of objects that display s a list of all keys 
#  values() returns a veiw of objects that displays alist of all values
# items()returns a veiw of objects that displays a list of dictionarykeys and values tuple pairs)
# 



# Exercise : Use the update method to change the course and add a new 
# key "WhatsApp_Number" to the dictionary
student_dict.update({
    "course" : "bscs" , 
    "whatsApp_number" : "0762621194"
    })

print(student_dict)







