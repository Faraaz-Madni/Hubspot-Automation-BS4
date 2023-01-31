

"""
Functions 1 of 3 implemented.
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
                # if i < 10 and i > 2: # In case you need to specify select rows.   #+
                # Assigning the values from the fields in the CSV to variables. You may replace the field names to suit your CSV.
                fac_name, fac_email = row['Facility Name'], row['Facility Email'] 

                print ("Facility Name is ", fac_name)
                print ("Facility E-mail is ", fac_email)

                fac_website = fac_email[fac_email.index('@') + 1 :]
                email_providers_list = ["GMAIL.COM","YAHOO.COM","AOL.COM","HOTMAIL.COM","PROTONMAIL.COM"] #Filter out email providers, leaving just the website URLS of the agencies.
                if (fac_website not in email_providers_list):
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
                #     print ("Row Limit Reached.")                                  #+

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
        j = "HTTPS://WWW." + j
        print ("Currently looking at: ", j) #COME BACK TO THIS LATER, TESTING WITH A SINGLE WEBSITE RN.
        webpage = urlopen("HTTPS://WWW.NURSENEXTDOOR.COM")
        extracted_html = webpage.read().decode("utf-8")

        soup = BeautifulSoup(extracted_html,"html.parser")
        soup.get_text()
        soup_filter = re.findall(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', soup.text)
        print(soup_filter)
        
        break

        
extract_website('src/PythonAutomationSource.csv')

"""                                                     TO DO

1.  Function to check extracted website's robots.txt to see if website can be scraped.
2.  Check the website's terms of service to see whether scraping the website has been explicitly prohibited.
3.  Check if the website offers an API.                                                                       - no scraping required then, but highly unlikely.
4.  Use a rotating Residential IP.                                                                            - costly!
5.  Crawl to find page that has a specified branch's detail.
6.  Extract address of the branch.
7.  Extract contact number.
8.  Extract company name. 
9.  Store extracted website data in a CSV.
10. Upload data row by row into Hubspot.

"""
