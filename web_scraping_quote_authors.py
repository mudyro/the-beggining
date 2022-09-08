#The challange was to get all the unique authors of quotes on the website
#Website link: http://quotes.toscrape.com/
import bs4
import requests

authors = [] 
countdown = [] #I do not know how many pages with quotes are there, so I've made a countdown that stops after no more quotes appear on next page
n = 1

while len(authors) == len(countdown):
        unique_url = 'http://quotes.toscrape.com/page/{}/' #url link to each page 
        res = requests.get(unique_url.format(n)) #n is the number of each page

        soup = bs4.BeautifulSoup(res.text,'lxml') #Html code of the site

        authors_class_list = soup.select(".author") #find all class = 'author' in the HTML code
        
        for author_class in authors_class_list: #Create a list that collets author names (they may repeat)
            authors.append(author_class.text)
#         print(f"Lenght of authors list is {len(authors)}")
            
        for i in range(10): # If this counter len is bigger than authors list len then it means that no more new authors appear on next pages
            countdown.append('author count')
#         print(f"Lenght of countdown is {len(countdown)}")
        n += 1
        
print(set(authors)) #The author repeat so i have to make set


