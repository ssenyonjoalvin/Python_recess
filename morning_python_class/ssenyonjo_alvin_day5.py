# functions

# example
# functions in python are defined using the 'def keyword
# followed by the function name ,parenthenes{ , inside the parenthenses you pyt a parameter name and  a colon.abs

# example1 
def multiply(a,b) :
    return a*b

result = multiply(5,10)
# print(result)

def get_coordinates():
    return 10,20

x,y =get_coordinates()
print(x,y)



    # execrise 1 : define a function greet with parameter name , set to 'guest' and print a message
    # i am a software programmer


def greet(guest):
     print("I am a software programmer.") 
greet("get")


    # execrise return multiple values of your name and age 

def personal_details(name, age) :
        return name ,age 

name ,age =personal_details("alvin",23)
print(name ,age )


"""
def : keyword to define a function
function name : is the name of the function

"""
# # syntax for definnig a function
# def function_name(parameters) :
#     #Docstring Optional
#      function body
#     return value

# Lambda function

# syntax for lambda function 
# lambda parameter : expression

# example 4

add = lambda a, b: a + b
print(add(45,70))

# |exmaple 5: Usecase of lambda function for sorting

coordinates = [(1,2), (2,3), (3,1), (5,0)]

coordinates.sort(key =lambda coordinate:coordinate[1])
print(coordinates)


# Map ,filter and reduce
# get the squares of 1 to 5 using map , filter and reduce

number_squares = [1, 2, 3, 4, 5]

# execrise : define a function to get user info that avccept arditray keyword aruments and prints 
# each key value pair


def get_user_info(**kwargs):
  """
  Gets user information with arbitrary keyword arguments and prints each key-value pair.

  Args:
      **kwargs: Arbitrary keyword arguments representing user information.
  """
  for key, value in kwargs.items():
    print(f"{key}: {value}")

# Example usage
user_info = get_user_info(name="Alice", age=30, city="New York")
# **kwargs: allow passing an arbitrary number of keyword aruguments to a function

# Example 7 : how to handle a **kwargs in functions

def ahaabwe_function(a, b, **kwargs):
    print(f"a: {a}, b:{b}")

    for key , value in kwargs.items():
        print(f"{key}:{value}")

ahaabwe_function(1,2, x=100, y=200, z=300)


