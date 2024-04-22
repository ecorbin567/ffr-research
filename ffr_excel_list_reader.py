"""
Automating collection of Fossil Free Research data.
Goal: To find all corporate research sponsors at the University of Toronto
that are on UBC’s list of fossil fuel enablers.

The list of research sponsors is no longer available, so I could not include it here.

Documentation for:
CSV library: https://docs.python.org/3/library/csv.html

-Elise Corbin
"""

import csv

# opening and reading csv files

# UBC list of dirty companies >:(
with open('ubc_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    ubc_list = [row[0] for row in reader]
# you have to do row[0] because when you edit and re-save CSV files in Excel it adds annoying extra commas

# industry sponsor TITLES
with open('industry_research_sponsors.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    industry_sponsors = [row for row in reader]

# flattening industry sponsor list
industry_sponsors = [item for sponsor in industry_sponsors for item in sponsor]

# checking each industry sponsor for oil company names
dirty_industry_sponsors = []

for row in industry_sponsors:
    # checking for company names
    for company in ubc_list:
        if company in row:
            dirty_industry_sponsors.append(str(company))

# writing to a new csv file
with open('new_industry_sponsors.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for sponsor in dirty_industry_sponsors:
        writer.writerow([sponsor])
