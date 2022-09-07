import os
import re
from os import listdir

#There are 5 folders :One, Two, ..., Five", each folder contains several .txt files filled with some text.
#The job was to find a phone number in form of a pattern: ###-###-#### in one of the mentioned files.

#directories to each folder
file_one = "C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content\\One"
file_two = "C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content\\Two"
file_three = "C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content\\Three"
file_four = "C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content\\Four"
file_five = "C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content\\Five"

folders_list = [file_five,file_four,file_one,file_three,file_two] #list of folder names
folder_names = listdir("C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content") #extract folder names

#pattern that we are looking for: 3 digits - 3 digits - 4 digits
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

#check each txt file in each folder for the pattern and print it's location
for folder_name in folders_list: 
    for txt_name in listdir(folder_name):
        for line in open("C:\\Users\\michal.sapula\\Desktop\\pomocnicze\\apm_extract\\extracted_content\\"+folder_names[folders_list.index(folder_name)]+"\\"+txt_name):
            for match in re.finditer(pattern, line):

                #Let's print the file directory and phone number itself.
                print(f"The phone number was found in {folder_name} folder in {txt_name} file")
                with open(folder_name +"\\"+ txt_name) as the_one_file:
                    lines = the_one_file.readlines()
                
                result = re.search(pattern, lines[0])            
                print(f"The phone number that we were looking for is: {result.group()}")
