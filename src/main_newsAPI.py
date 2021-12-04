from flask import Flask, render_template
import random
import time
from datetime import datetime, timezone, timedelta
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import html5lib
import lxml
import json

from textblob import TextBlob
import re

app = Flask(__name__)

cache = {}

def clean_html(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, ' ', raw_html)
	cleantext =  cleantext.replace('&nbsp;'," ")
	cleantext = cleantext.split('  ')
	for i in cleantext:
		if i:
			return i
	return -1


def genenrate_news_table(items):
	news_items = []

	for item in items:
		news_item = {}
		news_item['title'] = item.title.text
		news_item['description'] = clean_html(item.description.text)
		news_item['raw_description'] = item.description.text
		news_item['link'] = item.link.text
		news_item['pubDate'] = item.pubDate.text
		news_items.append(news_item)

	df = pd.DataFrame(news_items,columns=['title','description','raw_description','link','pubDate'])
	df['polarity'] = df.description.apply(lambda x: TextBlob(x).sentiment.polarity)
	df['subjectivity'] = df.description.apply(lambda x: TextBlob(x).sentiment.subjectivity)
	df = df[df.polarity != 0]
	return df.to_dict('records')

@app.route('/')
def home():
	q = 'google'
	if q in cache:
		print('HIT')
		return render_template("main.html", article_data=cache[q])

	url = "https://newsapi.org/v2/everything?q={}&from=2021-11-03&sortBy=popularity&apiKey=ee3e5dffa00d4444b086215f31e2577f".format(q)
	resp = requests.get(url)

	soup = BeautifulSoup(resp.content,'html.parser')

	site_json=json.loads(soup.text)

	articles = site_json['articles']

	for article in articles:
		article['polarity'] = TextBlob(article['description']).sentiment.polarity
	cache[q] = articles

	return render_template("main.html", article_data=articles)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True) # anyone can connect, and we're running on port 5000


# TODO:
# - add image 
# sources 
