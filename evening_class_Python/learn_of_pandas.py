# import pandas 

# student ={
#     'name' : ['alvin', 'richie', 'ricelle','angel'],
#     'age' : ['34','56','90','89']
# }

# # BSE = pandas.DataFrame(student)
# BSE = pandas.Series(student)                                                              

# print(BSE)


# cs = pandas.read_csv('soil_data.csv')
# # print(cs.to_string())



import pandas as pd
df = pd.read_csv("soil_data.csv")
print(df)

import pandas as pd 
print(pd.read_csv(r"/home/ssenyonjoalvin/Documents/django/django-ml--crop-prediction/crop-prediction/soil.csv"))

# Reading files in pandas
"""
pd.read_csv = for csv files
pd.read_json = for json files
pd.read_table = for txt files



print(pd.read_csv(r"/home/ssenyonjoalvin/Documents/django/django-ml--crop-prediction/crop-prediction/soil.csv"))

# full display of large data forms
by default jupyter gives us the first 5 elements and the last five element 
inorder to see all the values in the document , you should identenfy wc part 
is missing ( columns / rows )

# columns 
pd.set_option('display.max.columns', 6755)

# rows
pd.set_option('display.max.rows', 67584)

to find out we use 

import pandas as pd
df = pd.read_csv("soil_data.csv")
print(df)
df.info()

"""

# Filtering and ordering 
"""
filter based on columns

df[df['column_name'] > 10]

# eg
df[df['b01'] > 10]

if we are to check if specific value exist under a given culomn

specific_students = ['Alvin', 'Josh']

df[df[names].isin(specific_students)]
 in the above line of code we are checking if the names specified in the list exist in the column names 


df[df['country'].str.contains('united')]
Line of code checks from the column country and returns strings that contain the string united in them

we can also use index 
**filter 
**loc = location 
**iloc = integer location

df2.filter(items = ['course', 'year', 'residence_status'])
the line of code only returns the columns that are specified in the the angular brackets
 
 **we can filter by axises  0 for the horizontal and 1 for the vertical (this is the default)

"""