#Boolean functions
#these boolean functions return a false because the variables  entered in the bool() function have no  value
print(bool(False))
print(bool({}))
print(bool(0))
print(bool(""))

#these boolean functions return a true because the variables  entered in the bool() function has a value
m = 15
s = "Hello"
print(bool(m))
print(bool(s))


#This function portrays the use of boolean values in functions

def myFunction() :
        return True
if myFunction():
    print(1)

else:
    print(0)

#Strings 
# string declaration (using double quotes and single quotes) && string concation (using a comma , and using a plus sign)
x = "Come early"
y = 'you late '

print("I told you to " , x , "but " , y)

print("I told you to " + x + "but " + y)


#3
#this lines of code below show the use of strings and boolean values
isAdmitted = True
school = "Makerere"
reg_number = "22/u/8904"
course = 'BSSE'

if(isAdmitted == True):
    print("My University is " + school + " and registration number is "+ reg_number+ " my course is "+ course)
    print ('')
else:
    print('Records do not exist for such a student .')


"""
        List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
