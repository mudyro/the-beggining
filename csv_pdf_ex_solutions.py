#Exercise one: CSVs
#find a hidden link to google drive in a csv file.

import csv
import re #import re for searching through the files

#open the file
data = open("find_the_link.csv", encoding="utf-8") 

csv_data = csv.reader(data)
data_list = list(csv_data)

link = ''

# for n in range(len(data_list)):
#     print(data_list[n])
#link is hidden in diagonal from left top to right down (if we look at it as a table)

for x in range(len(data_list)):
    link +=data_list[x][x]

print(link) #The link that we were looking for

#Exercise 2: PDFs
import PyPDF2

#open the file
file = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(file)

#create a pattern to find any number on the page
pattern = re.compile('\d+')

#create a loop that will check each and every page for the pattern
for n in range(pdf_reader.numPages):
    all_digits = re.findall(pattern,pdf_reader.getPage(n).extractText())
    
    possible_phone_numbers = "".join(all_digits)
    if len(possible_phone_numbers) >= 10:
        print(possible_phone_numbers)
    
 #This prints every pattern that is on the page.
 #The pattern to be a phone number must have at least 10 characters and 10 digits in it.
 #luckily there is no more 10 += digit patterns on the site, so this has to be the one:
