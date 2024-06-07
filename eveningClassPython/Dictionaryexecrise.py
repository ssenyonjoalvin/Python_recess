#Exercise5
Shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40

 }

#returns the size of the shoes
print(Shoes["size"])

#changes the value of the brand from Nick to Adidas
Shoes.update({"brand" : "Adidas" })
print( Shoes)

#Adds the type to the Shoes dictionary
Shoes["type"] = "sneakers"
print(Shoes)

#returns a list of the keys of the dictionary
m = list(Shoes.keys())
print(m)

#returns a list of the values of the dictionary
s = list(Shoes.values())
print(s)

#checks in the dictionary and returns a ture since "size exists in the dictionary"
x = "size" in Shoes
print(x)

#loops through the dictionary and prints each key with its value 
for x,y in Shoes.items() :
    print(x, ":" ,y)

#removes color from the dictionary
del Shoes["color"]
print(Shoes)

#empties the dictionary
Shoes.clear()

# created a dictionary called company
Company = {
  
   "company_name" : "Global Star Solution",
   "location" : "Kampala",
    "number_of_employees" : 23,
   "tin_number" : 124790083736
}
print(Company)

#make a copy from the company dictionary
mycompany = Company.copy()
print(mycompany)


#nested 
MakerereUniversity = {
    "Cocis" : {
        "year" : 2002,
        "number_of_courses" : 8
    },
    "Cobams" : {
        "year" : 1997,
         "number_of_courses" : 34
    },
    "Law" : {
        "year" : 1990,
         "number_of_courses" : 15
        
    },
}