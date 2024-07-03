
# Inheritance and Polymorphism
"""summary

Inheritance and method overriding
Polymorphism and method resolution
order
Abstract classes and interfaces

    """

# Inheritance and method overriding
"""summary
--description
Inheritance and method overriding allows a class(child class) to inherit attributes and methods
from another class (parent class).

Key concepts
Base class (parent class): Class whose properties are inherited by another class.
Derived class (child class): Class that inherits attributes and properties from another base class.

    """

# Example 1: Syntax Create a class where a dog inherits from animal and overrides with a speak method


class Animal:
    def speak(self):
        return "Mwe Mwe Mwe Mwe Mwe"


class Dog(Animal):
    def speak(self):
        return "Barks"


# # Implementatiion of inherited classes

# animal = Animal()
# dog = Dog()

# print(animal.speak())
# print(dog.speak())

# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method resolution Order (MRO). is order in which python looks for a method in hierarchy classes.

# Example 2: How polymorphismworks in python


class Animal:
    def speak(self):
        return "Croock"


class Dog(Animal):
    def speak(self):
        return "Barks"


class Cat(Animal):
    def speak(self):
        return "Meow"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())
"""

# execrise1:

create a simple application to manage different types of vechiles. implement dervied class to demonstrate inheritance and plolymorphism 

1. base class vechiles
attributes: make, modeland year
methids:display_info()

2.dervied classes
Car : inherits from vechile 
attributes:: number of doors
overrides : display_info()

motorcycle : inherit from vechile 
attributes: type of bike (cruiser, sport, touring)
overrides : display_info()


# execrise 2 : 
create a function that accepts a list of vechiles objects and call their display_info()metod to print details of each vechile


"""

class Vechile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This vehicle is a {self.make}, model {self.model}, made in {self.year}.")


class Car(Vechile):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"The car is a {self.make}, model {self.model}, made in {self.year}, with {self.number_of_doors} doors.")


class Motorcycle(Vechile):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        print(f"The motorcycle is a {self.make}, model {self.model}, made in {self.year}, and it is a {self.type_of_bike} bike.")


def display_all_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()



car1 = Car("Toyota", "Corolla", 2020, 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2019, "cruiser")

vehicles = [car1, motorcycle1]
display_all_vehicles(vehicles)


"""
Working with tex files

handling CSV files 
JSON and XML file processing 

"""
# 1 . Working with text files , open ,read ,write and close
# note : python provides inbuilt functions to handle text files.

"""
__ description  
 opening files : open() function {r, w, a, r+}
 Reading files : read() fuction 
 Writing files : write() function
 close file : close()function

"""
# example 3: write a file and read afile

with open ("avlin.txt" , 'w') as file :
    file.write('I am Alvin and i am in love with python.\n')
    file.write('i used python for automation')

    # reading from a text file
    with open ('alvin.txt', 'r' ) as file :
        content = file.read()
        print(content)

    
# handling CSV file
"""
CSV (Comma Separated value) file widely for data exchange

key concepts 
read CSV files: using 'csv.reader()'
writing csv files : using 'csv.writer()'
DictReader and Dictwriter : the class read and write CSV files as dictionaries

"""
#example4 : writing and reading a csv
import csv

# Writing to a csvfile
wih open ("alvin.csv","w",newline="") as csv_file:
    writer =csv.writer(csv_file)
    writer.writerow(['name','age'])
    writer.writerow(['alvin','3'])
    writer.writerow(['ggobi','5'])
    writer.writerow(['dero','7'])

    # read fron a csv file 
    with open ('alvin.csv','r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader :
            print(row)

# JSON and XML file processing 
"""
JSON (Javascript Object Notation) and XML (Extensible Markup language)
are

key concepts 
load JSON data:json.load()

"""
# example 6 : write  and read JSON file 
import json 

# writing to a JSON file 
student_data = {
    'name' : 'ssenyonjo',
    'course': 'BSE'
}

# open the file 
with open ('student_data.json ', 'w') as json_file:
    json.dump(student_data,json_file)

# reading the JSON File 
with open('student_data.json','r') as json_file:
    student_data = json.load(json_file)
    print(student_data)




# exercise2 : write and read in the xml file 
# execrise3 : using abstraction caclulate the area and perimeter of the a rectangle


import xml.etree.ElementTree as ET

def write_xml(file_name):
    # Create the root element
    root = ET.Element("data")

    # Create a child element
    item1 = ET.SubElement(root, "item")
    item1.set("name", "item1")
    item1.text = "This is item 1"

    # Create another child element
    item2 = ET.SubElement(root, "item")
    item2.set("name", "item2")
    item2.text = "This is item 2"

    # Create a tree structure
    tree = ET.ElementTree(root)

    # Write to the file
    with open(file_name, "wb") as files:
        tree.write(files)

def read_xml(file_name):
    # Parse the XML file
    tree = ET.parse(file_name)
    root = tree.getroot()

    # Iterate through the elements and print them
    for item in root.findall("item"):
        name = item.get("name")
        text = item.text
        print(f"Item name: {name}, text: {text}")

# Write to XML
write_xml("example.xml")

# Read from XML
read_xml("example.xml")



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of Rectangle
rect = Rectangle(5, 3)

# Calculate and print area
area = rect.calculate_area()
print(f"Area of the rectangle: {area}")

# Calculate and print perimeter
perimeter = rect.calculate_perimeter()
print(f"Perimeter of the rectangle: {perimeter}")

