import requests
from bs4 import BeautifulSoup as soup

f = open('TNEPolitics.csv','w')
f.write('Politics\n')


tne = requests.get('http://thenigerianexpression.com/category/politics')
page = soup(tne.content,'html.parser')
bigcategory = page.find_all('div',class_='post-content-area')

try:
    x=1
    while x%2!=0:
        politics = bigcategory[x].find_all('a')[2].text
        f.write(politics + "\n")
        x+=2
except IndexError:
    print ("Complete")
    
                
        

    