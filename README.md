# Capstone Project
The goal of this project was to develop and deploy a working recommender to help people choose what whiskey or beer you should drink based on your preferences.  

In order to get reviews, to run natural language processing on, I scraped Beer Advocate and the LA Whiskey Society. After cleaning the data, I built a model using Count Vectorizer with a ngram of (2, 2) and then passed the data through Truncated SVD in order to reduce the dimensionality to 5 features. Once I had this reduced feature space, I performed cosine similarity to determine which whiskies and beers are most similar to each other. My recommender then goes through this list and pulls out the top 3 most similar whiskies or beers for your selection.  

If you would like to get a recommendation on what whiskey or beer you should drink next, feel free to head to [whatshouldidrink.xyz](http://www.whatshouldidrink.xyz/).  
--> A whiskey recommendation will be based on the beer you select and your beer recommendation will be based on the whiskey you select.


## Scraping
I ran my scrapers on an AWS EC2 instance.  
The beer scraper can be found [here](https://github.com/markorland/What-Should-I-Drink/blob/master/Scraping/aws_scraper.py) and the whiskey scraper can be found [here](https://github.com/markorland/What-Should-I-Drink/blob/master/Scraping/aws_whiskey_scraper.py).

## EDA
My exploratory data analysis on both the whiskey and beer reviews can be found [here](https://github.com/markorland/What-Should-I-Drink/tree/master/EDA).

## Model
The code for testing and building out my model is [here](https://github.com/markorland/What-Should-I-Drink/blob/master/Model.ipynb).

## Recommender
The code for testing and building my recommender is [here](https://github.com/markorland/What-Should-I-Drink/blob/master/Recommender.ipynb).

## Flask Application
All the files for the flask application can be found [here](https://github.com/markorland/What-Should-I-Drink/tree/master/FlaskApp).  
The python code is [here](https://github.com/markorland/What-Should-I-Drink/blob/master/FlaskApp/recommender.py).  
The html files are [here](https://github.com/markorland/What-Should-I-Drink/tree/master/FlaskApp/templates).

## PowerPoint Presentation
If you would like to check out the PowerPoint presentation click [here](https://github.com/markorland/What-Should-I-Drink/blob/master/Presentation/What%20Should%20I%20Drink.pptx).