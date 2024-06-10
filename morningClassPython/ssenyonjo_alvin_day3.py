#best practices
"""
1. indentation 
2. maximum line length  limit 79 charcters
3. blank line
4.use meaningful names
5. use of list com

"""
#comprehension{list, dictionary}

#python operators
"""


#name of the operator
equal             x == y
not equal         x != y
Greater than       x > y
less than         x < y
greater than or equal  x >= y
less than or equal     x <= y
 

 #example of python logical operators
 and              and &
or                 or  |
not                not 

#example of membership operator 
in            x in y
not in        x not in y

# example of bitwise operators
AND               &
OR                |
XOR               ^
NOT

#python cases
1. snake_case
2. camelCase
3. PascalCase
4. UPPERCASE
5. kebab-case
"""


#COMPREHENSIONS (lists, dictionary)
"""
comprehensions provide a concise way to create lists and dictionary
lists       [] square bracekets    store multiple items in a single variable
dictionaries {} curly brackets    store data in key value pairs
"""
#example1
#create a list of squares  in a range of 10

list_of_squares = [x**2 for x in range(10)] 
print(list_of_squares)

#
#create a list of even squares in the range of  20
list_of_even_squares = [x**2  for x in range(20) if  x%2 == 0]

print(list_of_even_squares)

#DICTIONARY COMPREHENSION
#create a dictionary comprehensionfor favorite cars and count the lengths of characters
favorite_cars = ['BMW', 'Jeep', 'Mercedes', 'fordraptor']
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths) 

#create a dictionary comprehension
list_of_tuple = [1,2,3,4,5,6,7,8,9,10]
cube = {x:x**3 for x in list_of_tuple}
print(cube)