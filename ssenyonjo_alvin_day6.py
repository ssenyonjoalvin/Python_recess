# Erroe handling in python
# Exception Hnadling with try, expect ,else and finally
# custom exception
"""
error handling in python it helps to handle unexpected situtations and errors.

try : contains code that midht throw an exception
NB :if an exception occurs , the rest of the code in the try block is skipped / ignored

except : catches and handles expections
NB : you can specify different handlers for different expection types

Else : the code runs if no expection occurs
if no exception are raised in the try block it runs


finally : it runs whether an expcetion is raised / occured or not
NB : used for clean up action
"""

# Example1 : handle expection with divison by zero

# try :
#     number = int(input("enter a number"))
#     result = 20 / number 

# except VauleError :
#     print("Invalid number !! number entered is invalid")
# except ZerDivisionError : 
#     print("This is an error ,")

# else : 
#     print("The answer is ",result)

# finally : 
#     print("Execution completed successfully")
# try :
#     number = int(input("enter a number"))
#     result = 20 / number 

# except VauleError :
#     print("Invalid number !! number entered is invalid")
# except ZerDivisionError : 
#     print("This is an error ,")

# else : 
#     print("The answer is ",result)

# finally : 
#     print("Execution completed successfully")

    # execise 1 : write a function that converts a string to an integer and handle both valueError 
    # if the string cannot be converted to an integer and the typeError if the input is not a string 
    # use multile except block to handle these exceptions
def string_to_int(s):
    try:
        # Attempt to convert the string to an integer
        result = int(s)
        return result
    except ValueError:
        # Handle the case where the string cannot be converted to an integer
        print("ValueError: The provided string cannot be converted to an integer.")
        return None
    except TypeError:
        # Handle the case where the input is not a string
        print("TypeError: The input provided is not a string.")
        return None

# Example usage:
# print(string_to_int("123"))  # Should return 123
# print(string_to_int("abc"))  # Should print ValueError message and return None
print(string_to_int(123))    # Should print TypeError message and return None


# CUSTOM EXCEPTION HANDLING
# Example 2: Exception raised for error in tht iput , if funds are insufficient.

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account."
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exceptions handling
try:
    balance = 20000
    amount_to_withdraw = 25000
    new_balance = withdraw(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
else:
    print("Transaction complete. New balance:", new_balance)



# execrise 2 : create a custom exception invalidAgeError and write a function that raises 
# this exception if the given age is negative . handle this custom exception when calling the function

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"The age entered is {self.age}, but age can never be negative."
        super().__init__(self.message)

def record_age(age):
    if age <= 0:
        raise InvalidAgeError(age)
    return age

try:
    age = int(input("Enter your age, please: "))
    record_age(age)
except InvalidAgeError as e:
    print(f"Error: {e.message}")
else:
    print(f"Your age is valid: {age}")

