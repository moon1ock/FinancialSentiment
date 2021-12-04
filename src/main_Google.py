# create certificate ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.9/etc/openssl 

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
import metadata_parser
from textblob import TextBlob
import re

app = Flask(__name__)


def genenrate_news_table(items):
	links_and_times = [(link.link.text, link.pubDate.text) for link in items ]
	article_data = []

	for i in links_and_times:

		article = {}
		article['pubDate'] = i[1]
		try:
			page = metadata_parser.MetadataParser(url=i[0],search_head_only = True)
		except:
			continue
		try:
			article['description'] = page.get_metadatas('description')[0]
			article['title'] = page.get_metadatas('title')[0]
			article['url'] = page.get_metadata_link('url')
			article['image'] = page.get_metadata_link('image')
			article['site_name'] = page.get_metadatas('site_name')[0]
			article['sentiment'] = round((TextBlob(article['title']).sentiment.polarity+TextBlob(article['description']).sentiment.polarity)/2,3)
		except:
			continue
		article_data.append(article)
		if len(article_data)>25:
			break
	return article_data

@app.route('/')
def home():

	q = 'Google'
	url = "https://news.google.com/rss/search?q=intitle:{}+after:2021-11-01&ceid=US:en&hl=en-US&gl=US".format(q)

	resp = requests.get(url)

	soup = BeautifulSoup(resp.content, features="xml")
	items = soup.findAll('item')

	article_data = genenrate_news_table(items)

	return render_template("main_Google.html", article_data=article_data)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True) # anyone can connect, and we're running on port 5000


# TODO:
# - add image 
# sources 
