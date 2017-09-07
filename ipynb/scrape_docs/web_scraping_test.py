## Web scraping program
##

## https://github.com/douglasmiranda/splinter-examples/blob/master/another_examples/screenshot.py
## http://splinter.readthedocs.io/en/latest/tutorial.html

from splinter import Browser
import csv
from bs4 import BeautifulSoup 
import time

# browser = Browser('chrome')
# browser = Browser('firefox')

with Browser() as browser:
    # Visit URL
    #url = "https://www.similarweb.com/website/" 
    #url_suffix = "#overview"
    
    # loop thru the urls in data frame
    counter = 0
    #for index, row in companies_df.iterrows():
    for i in range(0,1):
        counter += 1
        if counter == 2:
            break
        try:
            # temp url for testing
            t_url = "https://www.similarweb.com/website/shotput.com#overview"
            # Use url from data frame
            #url = row["Company Name URL"]
            print(t_url)
            browser.visit(t_url)
            time.sleep(30)
            html = browser.html
            soup = BeautifulSoup(html, "html.parser")
            
            print("Before the soup.prettify")
            
            print(soup.prettify())
            
            #span class="rankingItem-value js-countable"
            print("********  Start for loop to read soup  ********")
            #for line in soup.findAll('a', class_="rankingItem-subTitle is-link"):
            for line in soup.findAll('div', class_="rankingItem-underTitle"):
                # Append to a file or write to a data frame
                print("********  in soup for loop line first read is  ********")
                print(line)
                # Write to a file
                with open('mystats.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(line)
            
            for line in soup.findAll('div', class_="rankingItem-rank js-editable"): 
            #for line in soup.findAll('span', class_="rankingItem-value js-countable"):
                # Append to a file or write to a data frame
                print("********  in soup for loop line second read is  ********")
                print(line)
                # Write to a file
                with open('mystats.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(line)
            
            for line in soup.findAll('span', class_="rankingItem-value js-countable"):
                # Append to a file or write to a data frame
                print("********  in soup for loop line second read is  ********")
                print(line)
                # Write to a file
                with open('mystats.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(line)
            
            line = soup.find('span', class_="engagementInfo-param engagementInfo-param--large u-text-ellipsis")
            # Write to a file
            with open('mystats.csv', 'a') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(line)
        
            # Grab a tag from the html 
            for line in soup.findAll('span', class_="engagementInfo-param u-text-ellipsis"):
            #for line in soup.findAll('span', class_="engagementInfo-valueNumber"):
                # Append to a file or write to a data frame
                print("********  in soup for loop line third read is  ********")
                # Write to a file
                with open('mystats.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(line)
                    
              # Grab a tag from the html 
            for line in soup.findAll('span', class_="engagementInfo-valueNumber"):
                # Append to a file or write to a data frame
                print("********  in soup for loop line fourth read is  ********")
                print(line)
                # Write to a file
                with open('mystats.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(line)       
        
#                     # Write to the the data frame                
#                     # Save the json info into variables
#                     html_tag  = user_account["tag_name"]
#                     html_text = user_account["tag_text"]
               
#                     # Set the data frame info 
#                     companies_df.set_value(index, "col1", html_tag)
#                     companies_df.set_value(index, "col2", html_text)
        except:
            print("Error with url: ", t_url)
## https://www.similarweb.com/website/shotput.com#overview 