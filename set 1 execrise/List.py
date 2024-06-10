mylist = ["Paul", "Juma", "Joe", "Deo", "Joseph"]
print("Original list is :", mylist)
print(mylist[1])
print(type(mylist))

#change the value of the first element
def change_first_item(lst, new_value):
    if lst:
        lst[0] = new_value
        return lst
mylist = change_first_item(mylist, "John")
print("Update list:", mylist)

#put the sixth element
def add_sixth_item(lst, new_item):
    lst.append(new_item)
    return lst

mylist = add_sixth_item(mylist, "Francis")
print(mylist)

# add “Bathel” as the 3rd item in your list
def add_third_item(lst, new_item):
    lst.insert(2, new_item)
    return lst

mylist = add_third_item(mylist, "Bathel" )
print(mylist)

#remove 4th item from the list
def remove_4th_item(lst):
    if len(lst) >= 4:
        del lst[3]
        return lst
mylist = remove_4th_item(mylist)
print(mylist)
        
        
#print last item using negative indexing

def print_last_item(lst):
    if lst:
        print("the last item is: ",lst[-1])
print_last_item(mylist) 

#new list and print a given range of elements
new_list =["book", "pen", "chair", "table", "ruler", "bag", "belt"]
def print_items_in_middle(lst):
    print("the 3rd, 4th and 5th items are: ", lst[2:5])
print_items_in_middle(new_list) 

#list of countries and print a copy
country_list = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
print("The original copy of countries is: ",country_list)
x = country_list.copy()
print("The duplicate of countries is: ",x)  

#loop through the countries
for x in country_list:
    print(x)           


#list of animal names and sort them in both descending and ascending order.
animal_list = ["dog", "goat", "sheep", "cow", "monkey", "zebra"]

#ascending sort
ascending_sort = sorted(animal_list)
print("This list is sorted in assending order: ", ascending_sort)

#descending sort
desceding_sort = sorted(animal_list, reverse=True)
print("this list is sorted in descending order: ", desceding_sort)

# Filter animal names with the letter 'a' in them
animal_names_with_a = [name for name in animal_list if 'a' in name.lower()]
print("Animal names with the letter 'a':", animal_names_with_a)

#list of my name
first_name = ["Paul"]
second_name = ["Akol"]

second_name.extend(first_name)
print(second_name)


#myList = list(("Oranges", "Mangoes", "Apples"))
#print(myList)

