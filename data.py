import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


#Make HTTP Get request for webpage content
web_page = requests.get('https://en.wikipedia.org/wiki/Road_safety_in_Europe')

#Get all Tables in webpage
soup = BeautifulSoup(web_page.content, 'html.parser')
tables = soup.find_all("table", "wikitable")

#Select the European Union Road Safety Facts and Figures table
for table in tables:
    if table.caption  != None :
        if  table.caption.text.strip() == "European Union Road Safety Facts and Figures":
            selected_table = table;
            break


#Table Column names
headings = [ 'Country', 'Area', 'Population', 'GDP per capita', 'Population density', 
            'Vehicle ownership','Road Network Lenght' ,
            'Total road deaths','Road deaths per Million Inhabitants', 'Killed', 'Injury']



row = table.contents


#Get Records in table
records = []
rows = table.tbody.find_all('tr')

for x in range(1, len(rows)-1):
    record = rows[x]
    refined_record=[]
    for value in record:
        if value.__class__.__name__ == 'Tag':
            refined_record.append(value.text.strip())
    records.append(refined_record)

#Create pandas dataframe from  Lists
df = pd.DataFrame(records, columns=headings)

#Add year colum
df['Year'] = 2018
data = df.iloc[:,[0,11,1,2,3,4,5,7,8]]
#sort data by Road deaths per Million Inhabitants
data = data.sort_values('Road deaths per Million Inhabitants' , ignore_index=True)
#Export Data to CSV
data.to_csv('data.csv')