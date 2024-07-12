# libraries for web scrapping
# Request, BeautifulSoup,lxml, scrapy,Salenium
# API keys
# Execrises, openwethermap.org UGX50000000 re

# step1 : Import Libraries
import requests
from bs4 import BeautifulSoup
import csv
import json

#Step 2: Fetch the web pages 

url= 'http://ryeko.org'
response = requests.get(url)
html_content = response.text

# step 3:parse the Html using Beautifulsoup
soup = BeautifulSoup(html_content,'html.parser')

# step4 : find the specific data
data = []
for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link':link})



# step5 :save the data to CSV file

csv_file = 'scraped_data.csv'
with open('scrapped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature", "Humidity", "Wind Speed", "Description"])
    
    for row in data:
        writer.writerow(row)
        

        # step 6 : save the data to a JSON file
        json_file = 'scraped_data.json'
        with open(json_file,mode='w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False, indent=4)


        # step 7 : Save the data to a JSON file
        print(f'Data saved successfully to {csv_file}and {json_file} formate')
      
#    execrise1 : scrape data from the http://openweathermap.org
# current weatherdata
#Step 2: Fetch the web pages 

url= 'http://ryeko.org'
response = requests.get(url)
html_content = response.text

# step 3:parse the Html using Beautifulsoup
soup = BeautifulSoup(html_content,'html.parser')

# step4 : find the specific data
data = []
for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link':link})



# step5 :save the data to CSV file

csv_file = 'scraped_data.csv'
with open('scrapped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature", "Humidity", "Wind Speed", "Description"])
    
    for row in data:
        writer.writerow(row)
        

        # step 6 : save the data to a JSON file
        json_file = 'scraped_data.json'
        with open(json_file,mode='w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False, indent=4)


        # step 7 : Save the data to a JSON file
        print(f'Data saved successfully to {csv_file}and {json_file} formate')
