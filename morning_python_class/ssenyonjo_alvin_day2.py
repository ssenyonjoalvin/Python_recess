
#Write a python script to determine the price 
#of a movie based on age
#condition , children under 13 years get a discout for price  = shs .1000
#teenagers between 13 and 18 get discount price of shs. 500
#Adults 18 and above pay full price  = shs 2000
#otherwise , senior citizens 

client_age = int(input("Enter your age please : \n"))
     
if client_age <= 13 :
  print("you payment will be shs.1000") 

elif 13 < client_age <= 18:
    print("Your payment will be shs.1500")

elif 18 < client_age < 55 :
   print("your payment will be shs.2000")

else :
   print("senior citizens pay is shs.5000")




#create your own list of favourite colours using for loop
#create a reverse of the input 12345 to be 54321 using a while loop

Colours = ['black' , 'green', 'yellow', 'red', 'grey']
for Colour in Colours :
    print(Colour )
    
print ("")

count = 5
while count > 0 :
    print (count)
    count -= 1

    #this lines of code below show the use of strings and boolean values
isAdmitted = False
school = "Makerere"
reg_number = "22/u/8904"
course = 'BSSE'

if(isAdmitted == True):
    print("My University is " + school + " and registration number is "+ reg_number+ " my course is "+ course)
    print ('')
else:
    print('Records do not exist for such a student .')
