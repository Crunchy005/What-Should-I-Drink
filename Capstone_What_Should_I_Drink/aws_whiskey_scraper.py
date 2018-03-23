import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

def cleaner(string):
    string = re.sub(',', '', string)
    string = re.sub(' %', '', string)
    string = re.sub('\$', '', string)
    string = re.sub('\n', ' ', string)
    return string

grade_grabber = lambda x: re.search('images\/letters\/(.*)_', x).group(1)

def get_whiskey_reviews(url):
    sleep(2)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    
    w_name  = cleaner(soup.find('div', {'class': 'titlePopup'}).text)
    bottler = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[0].text)
    age     = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[1].text)
    w_type  = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[2].text)
    vint    = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[3].text)
    subt    = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[4].text)
    abv     = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[5].text)
    region  = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[6].text)
    price   = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[7].text)
    avaib   = cleaner(soup.find_all('td', {'class': 'textValuePopup'})[8].text)

    username = []
    for i in soup.find_all('td', {'class':'contentCell2Popup', 'width':'40'}):
        username.append(cleaner(i.text))

    grade = []
    for i in soup.find_all('td', {'class':'contentCell2Popup'}):
        for x in i.find_all('img',{'src':True}):
            grade.append(grade_grabber(x.attrs['src']))

    review = []
    for i in soup.find_all('td', {'class':'contentCell2Popup', 'align':'left'}):
        review.append(cleaner(i.text))
    

    for i in range(0,len(username)):        
        master_list = [username[i], grade[i], review[i], w_name, bottler, age, w_type, vint, subt, abv, region, price, avaib, url]
        with open('./aws_whiskey_reviews.csv', 'a+') as f:
            print(','.join(master_list), file=f)


df_whiskey = pd.read_csv('./df_whiskey.csv')
df_whiskey['url'][0:2].apply(get_whiskey_reviews)
