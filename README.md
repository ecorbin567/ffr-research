# ffr-research
Automating collection of Fossil Free Research report data at the University of Toronto.

Methodology for Data Analysis 
Endowed Chairs List: 
Goal: To find all current and former endowed chairs at the University of Toronto that were either endowed or supported by a company on UBC’s list of fossil fuel enablers. 
Methods:  
The list of former endowed chairs (from 2008) was in the form of a list of URLS. Since the URLs linked to sites on the internet archive and were therefore inaccessible by traditional webscraping methods, we checked the 2008 list manually. 
To search the list of current endowed chairs, we converted an existing spreadsheet of names into a pandas dataframe and modified the spreadsheet so that it only contained endowed chairs sponsored by companies on the UBC list. 
Research Sponsors: 
Goal: To find all corporate research sponsors at the University of Toronto that are on UBC’s list of fossil fuel enablers. 
Methods: Using CSV files containing a list of current corporate research sponsors and the UBC list, we simply ran a loop searching each element in the research sponsor list for a match to each element in the UBC list. Finally, we made a new CSV file containing the list of research sponsors that are also on the UBC list. 

# Read the finished report here:
https://drive.google.com/file/d/1tHaYgQuaLOoE9z6yNcMxASwQJIhhEqDX/view
