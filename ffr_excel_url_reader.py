"""
Automating collection of Fossil Free Research data.
Goal: To find all current (as of 2023) endowed chairs at the University of Toronto
that were either endowed or supported by a company on UBC’s list of fossil fuel enablers.

The current list of endowed chairs turned out to be a list of companies, rather than a list of URLs, so
this code was not needed. However, it's a helpful resource for looking through large numbers of websites.

Based on this tutorial: https://www.geeksforgeeks.org/python-web-scraping-tutorial/
Documentation for:
CSV library: https://docs.python.org/3/library/csv.html
BeautifulSoup: https://pypi.org/project/BeautifulSoup/
Requests: https://pypi.org/project/requests/

-Elise Corbin
"""

import requests
from bs4 import BeautifulSoup
import csv

# opening and reading csv files

# UBC list of dirty companies >:(
with open('ubc_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    ubc_list = [row[0] for row in reader]
# you have to do row[0] because when you edit and re-save CSV files in Excel it adds annoying extra commas

# endowed chairs TITLES
with open('', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    endowed_chairs = [row for row in reader]

# endowed chairs ARTICLES
with open('', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    endowed_urls = [row for row in reader]

endowed_urls = [str(row).replace('ï»¿', '', 1) for row in endowed_urls]

# flattening lists
endowed_chairs = [item for chair in endowed_chairs for item in chair]
endowed_urls = [item for url in endowed_urls for item in url]

# creating new lists and finding data for them
dirty_endowed_chairs = []
dirty_endowed_chair_titles = []
implicated_companies = []

count = 0
for row in endowed_urls:
    # counting iterations to keep me sane
    count += 1
    print('New row')
    print(count)

    # making a GET request
    r = requests.get(row[2: len(endowed_urls) - 2])  # taking out the quotation marks

    # parsing the HTML in each URL
    soup = BeautifulSoup(r.content, 'html.parser')
    lines = soup.find_all('p')
    print(lines)
    # checking for company names
    for company in ubc_list:
        if company in lines:
            print("Match found")
            dirty_endowed_chairs += row
            dirty_endowed_chair_titles += endowed_chairs[count-1]
            implicated_companies += company

# writing to new csv file
with open('new_endowed_chairs_current.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(['CHAIR TITLE', 'COMPANY', 'LINK TO CHAIR'])
    for i in range(len(dirty_endowed_chairs)):
        writer.writerow([dirty_endowed_chair_titles[i], implicated_companies[i], dirty_endowed_chairs[i]])
