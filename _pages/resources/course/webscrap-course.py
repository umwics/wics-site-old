# importing the libraries
from bs4 import BeautifulSoup
import requests
import csv


# Step 1: Sending a HTTP request to a URL
url = "https://www.sci.umanitoba.ca/cs/courses-2/"
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
    headings.append(td.text.replace('\n', ' ').strip())
print(headings)


# Get all the 4 tables contained in "cs_table"
cs_table = soup.find_all('table')

for table, heading in zip(cs_table, headings):

    t_headers = [ 
        "name",
        "title"
    ]
    table_data = []
    for tr in table.tbody.find_all("tr"): # find all tr's from table's tbody
        t_row = {}

        # find all td's(2) in tr and zip it with t_header
        for td, th in zip(tr.find_all("td"), t_headers): 
            t_row[th] = td.text.replace('\n', '').strip()
        table_data.append(t_row)

    # Put the data for the table with his heading.
    data[heading] = table_data
    print(table_data)


# Step 4: Export the data to csv
"""
For this example let's create 4 seperate csv for 
4 tables respectively
"""
for topic, table in data.items():
    # Create csv file for each table
    with open(f"webscrap-course\\{topic}.csv", 'w') as out_file:
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
for file in os.listdir("webscrap-course\\"):
    if file.endswith(".csv"):
        print(file)
        csv_file = pd.DataFrame(pd.read_csv('webscrap-course\\'+file, sep = ",", header = 0, index_col = False))
        results = file.strip().split(".csv")
        csv_file.to_json('webscrap-course\\'+results[0]+".json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)