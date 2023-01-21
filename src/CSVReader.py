"""
File 1 of 3.
Responsible for: Parsing CSV and extracting Domain Name from the lead's email.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Using Python's Built-in CSV module.
import csv
import re
#sourcefile = 'src/PythonAutomationSource.csv'

# Function to Extract Site from CSV.
def extract_website(sourcefile):
    try:
        #Parse the CSV.
        with open (sourcefile, newline ='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            i = 0               # Row Counter
            automated = 0       # Automated Counter to count Leads that have the Domain Website in their E-mail.
            manual = 0          # Manual Counter to count Leads that don't have the Domain Website in their E-mail.
            manual_list = []    # List to collect Names of Leads that will require Manual Attention.
            automated_list = [] # List to collect Domain Names to crawl. 

            for row in csvreader:        
                i += 1 
                print(i, " \n")
                # if i < 10 and i > 2: # In case you need to specify select rows.
                # Assigning the values from the fields in the CSV to variables. You may replace the field names to suit your CSV.
                fac_name, fac_email = row['Facility Name'], row['Facility Email'] 

                print ("Facility Name is ", fac_name)
                print ("Facility E-mail is ", fac_email)

                fac_website = fac_email[fac_email.index('@') + 1 :]
                if (fac_website != "GMAIL.COM" and fac_website != "YAHOO.COM"):
                    # Successfully extracted the Domain Website so this can be automated.
                    print ("Extracted Website: ", fac_website)
                    automated += 1 
                    automated_list.append(fac_website)

                else:
                    # Couldn't extract the Domain Website so this will need manual attention.
                    print("Domain Website not specified in E-mail.") 
                    manual += 1 
                    manual_list.append(fac_name)
                # else: 
                #     print ("Row Limit Reached.")

                print("-----------")
            
        print ("Leads Needing Manual Attention: ", manual)
        print ("Names of Leads Needing Manual Attention: ", manual_list)
        print ("Websites Extracted: ", automated)
        

        if not automated_list:
            print ("No Crawlable Websites found.")
        else:
            print ("Crawlable Websites found.")
            crawl_website(automated_list)
        
    except FileNotFoundError:
        # Exception Handling when CSV is not found.
        print ("The CSV file does not exist. Are you sure you specified the right path?")

def crawl_website(automated_list):
    print ("Websites Extracted: ", automated_list)
    for j in automated_list:
        print ("Currently looking at: ", j) #COME BACK TO THIS LATER, TESTING WITH A SINGLE WEBSITE RN.
        webpage = urlopen("HTTPS://WWW.NURSENEXTDOOR.COM")
        extracted_html = webpage.read().decode("utf-8")

        extracted_soup = BeautifulSoup(extracted_html,"html.parser")
        extracted_soup.get_text()
        print(extracted_soup)

        break

extract_website('src/PythonAutomationSource.csv')


# Using the Pandas module.
# import pandas as pd

# fac_name    = pd.read_csv('src/PythonAutomationSource.csv', usecols=['Facility Name'])
# fac_email   = pd.read_csv('src/PythonAutomationSource.csv', usecols=['Facility Email'])

# for i in fac_name:
#     print(i)
        