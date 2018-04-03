import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import re

def get_new_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/google/chrome/google-chrome'
    options.add_argument('headless')
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    return driver

review_grabber = lambda x: re.search('overall:\s\d\.\d*(.*[\s\S]*\d characters)', x).group(1)

def review_cleaner(string):
    x = review_grabber(string)
    x = re.sub('\d* characters', '', x)
    x = re.sub('\n', ' ', x)
    x = re.sub(',', '', x)
    return x

def get_user_reviews_csv(url):
    counter = 0
    review_number = 1
    for i in range(0,101):
        driver.get(f'https://www.beeradvocate.com{url}?view=beer&sort=&start={i*25}')
        sleep(2)
        beer_page = driver.page_source
        beer_page_soup = BeautifulSoup(beer_page, 'lxml')
        
        reviews = beer_page_soup.find_all('div', {'id':'rating_fullview_content_2'})
        
        counter += 1
        print(f'{url} -- page {counter}')
        
        for count, review in enumerate(reviews):
            score = review.find('span', {'class': 'BAscore_norm'}).text
            breakdown = review.find('span', {'class': 'muted'}).text
            u_names = review.find('a', {'class':'username'}).text
            try:
                r_text = review_cleaner(reviews[count].text)
            except:
                r_text = "No Review"
                
            master_list = [str(review_number), url, score, breakdown, u_names, r_text]
            with open('./aws_user_reviews.csv', 'a+') as f:
                print(','.join(master_list), file=f)
            
            review_number += 1
    
    sleep(2)


sleep(50)

driver = get_new_driver()
df_beer = pd.read_csv('./df_beer.csv', encoding = "latin1")
df_beer['url'].apply(get_user_reviews_csv)