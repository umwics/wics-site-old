# importing the libraries
from bs4 import BeautifulSoup
import requests
import csv


# Step 1: Sending a HTTP request to a URL
url = "https://www.sci.umanitoba.ca/cs/undergraduate-programs/"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text


# Step 2: Parse the html content
soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html

# Step 3: Analyze the HTML tag, where your content lives
# Create a data dictionary to store the data.
data = {}

# Get all the headings of Lists
headings = []
for td in soup.findAll("h2", {"class": "section__title-md"}):
    # remove any newlines and extra spaces from left and right
    prg = td.text.replace('\n', ' ').strip()
    split = prg.split()
    for item in split:
        if item.lower() in ['honours', 'major']:
            headings.append(prg)
print(headings)


# Get all the 4 tables contained in "cs_table"
cs_table = {}
cs_table = soup.findAll("div", {"class": "section-two-column__content"})
 #   cs_table.append(td.text.replace('\n', ' ').strip())

#for item in cs_table:
#    print(item)
#    print("=============================================================")

for table, heading in zip(cs_table, headings):

    t_headers = [ 
        "name",
        "title"
    ]
    table_data = []
    
    for p in table.find_all("p"):
        
        p_row = p.text.strip()
        #print(p_row)
        #print("=============================================================")
        
        lines = []
        for item in p_row.strip().split('\n'):
            if item:
                lines.append(item)
        #print(line[0])
        #print("=============================================================")
        
        
        for line in lines:
            #print(item)
            split_line = line.strip().split()
            first = split_line[0]
            t_row = {}
            if first.lower() in ['comp', 'math', 'stat']:
                #courseline.append(line)
                name = split_line[0]+" "+split_line[1]
                split_line2 = line.strip().split(split_line[1])
                title = ""
                courseline = []
                if split_line2:
                    title = split_line2[1]
                courseline.append(name)
                courseline.append(title)
                
                for td, th in zip(courseline, t_headers): 
                    t_row[th] = td.replace('\n', '').strip()
                table_data.append(t_row)
                #print(line)
                #print("=============================================================")
            

        # t_row = {}
        # for td, th in zip(courseline, t_headers): 
        #     t_row[th] = td.replace('\n', '').strip()
        # table_data.append(t_row)

    # Put the data for the table with his heading.
    data[heading] = table_data
    #print(table_data)


# Step 4: Export the data to csv
"""
For this example let's create 2 seperate csv for 
2 tables respectively
"""
for topic, table in data.items():
    # Create csv file for each table
    with open(f"webscrap-program\\{topic}.csv", 'w') as out_file:
        # Each 4 table has headers as following
        headers = [ 
            "name",
            "title"
        ] # == t_headers
        writer = csv.DictWriter(out_file, headers)
        # write the header
        writer.writeheader()
        for row in table:
            if row:
                writer.writerow(row)




# Step 5: convert csv to json
import pandas as pd

import os
for file in os.listdir("webscrap-program\\"):
    if file.endswith(".csv"):
        print(file)
        csv_file = pd.DataFrame(pd.read_csv('webscrap-program\\'+file, sep = ",", header = 0, index_col = False))
        results = file.strip().split(".csv")
        csv_file.to_json('webscrap-program\\'+results[0]+".json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)