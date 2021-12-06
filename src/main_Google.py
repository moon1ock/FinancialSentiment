# create certificate ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.9/etc/openssl 

from flask import Flask, render_template,request, redirect, url_for
from flask_cors import CORS
import random
import time
from statistics import mean
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
from datetime import datetime
from googlesearch import search as gsearch


from wtforms import Form, BooleanField, StringField, PasswordField, validators

from urllib.parse import urlparse
import yfinance as yf
import asyncio
import time
import aiohttp
from aiohttp.client import ClientSession
from bs4 import BeautifulSoup
import metadata_parser
from textblob import TextBlob

app = Flask(__name__)
CORS(app)
cache = {}
symbols = {}
companyinfo = {}
pricedict = {}

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 

#### FORM for QUERY #####

class QueryForm(Form):
	 query = StringField('Company', [validators.Length(min=3, max=30)])


#### WEB SCRAPER OBJECT ####

class WebScraper(object):
	def __init__(self, urls):
		self.urls = urls
		self.all_data  = []
		self.master_dict = {}
		asyncio.run(self.main())

	async def fetch(self, session, url):
		try:
			async with session.get(url, timeout = 10) as response:
				# 1. Extracting the Text:
				text = await response.text()
				# 2. Extracting the  Data:
				article = await self.extract_data(text)
				return url, article
		except Exception as e:
			return

	async def extract_data(self, text):
		try:
			page = metadata_parser.MetadataParser(html=text,search_head_only = True)
			if (page is not None) and (page.get_metadatas('title')[0] is not None):
				article = {}
				article['description'] = page.get_metadatas('description')[0]
				article['title'] = page.get_metadatas('title')[0]
				article['url'] = page.get_metadata_link('url')
				article['image'] = page.get_metadata_link('image')
				article['site_name'] = page.get_metadatas('site_name')[0]
				article['sentiment'] = round((TextBlob(article['title']).sentiment.polarity+TextBlob(article['description']).sentiment.polarity)/2,3)
				return article
			return
		except Exception as e:
			return

	async def main(self):
		tasks = []
		headers = {
			"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

		async with aiohttp.ClientSession(headers=headers) as session:
			for url in self.urls:
				tasks.append(self.fetch(session, url))

			htmls = await asyncio.gather(*tasks)
			self.all_data.extend(htmls)

			for html in htmls:
				if html is not None:
					url = html[0]
					self.master_dict[url] = html[1]
				else:
					continue


def scrape_data(query):
	form = QueryForm(request.form)
	q = "-1"
	if request.method == 'POST' and form.validate():
		q = form.query.data
		return redirect(url_for('search', query = q))

	q = query

	url = "https://news.google.com/rss/search?q=intitle:{}%20stock+after:2021-11-01&ceid=US:en&hl=en-US&gl=US".format(q)

	resp = requests.get(url)

	soup = BeautifulSoup(resp.content, features="xml")
	items = soup.findAll('item')

	links_and_times = {link.link.text: link.pubDate.text for link in items }

	urls = [link.link.text for link in items ]

	scraper = WebScraper(urls = urls[:]) # HOW many URLs would you want?
	article_data  = list(a for a in scraper.master_dict.values() if a)

	for story in article_data:
		if story['url'] in links_and_times:
			story['pubDate'] = links_and_times[story['url']]

	return article_data


def name_convert(a):

    searchval = 'yahoo finance '+a
    link = []
    #limits to the first link
    for url in gsearch(searchval, tld='es', lang='es', stop=1):
        link.append(url)

    link = str(link[0])
    link=link.split("/")

    if link[-1]=='':
        ticker=link[-2]
    else:
        x=link[-1].split('=')
        ticker=x[-1]
    try:
    	long_name = yf.Ticker(ticker).info['longName']
    except:
    	return '', ''
    return ticker, long_name



@app.route('/search/<query>', methods=['GET', 'POST'])
def search(query):
	form = QueryForm(request.form)
	q = "-1"
	if request.method == 'POST' and form.validate():
		q = form.query.data
		return redirect(url_for('search', query = q))


	q = query

	if q in cache:
		return render_template("main_Google.html", article_data=cache[q])
	url = "https://news.google.com/rss/search?q=intitle:{}%20stock+after:2021-11-01&ceid=US:en&hl=en-US&gl=US".format(q)

	resp = requests.get(url)

	soup = BeautifulSoup(resp.content, features="xml")
	items = soup.findAll('item')

	links_and_times = {link.link.text: link.pubDate.text for link in items }

	urls = [link.link.text for link in items ]

	scraper = WebScraper(urls = urls[:]) # HOW many URLs would you want?
	article_data  = list(a for a in scraper.master_dict.values() if a)

	for story in article_data:
		if story['url'] in links_and_times:
			story['pubDate'] = links_and_times[story['url']]

	cache[q] = article_data
	return render_template("main_Google.html", article_data=cache[q])

@app.route('/api/<query>', methods=['GET'])
def api(query):
	if not query in symbols:
	    symbol, full_name = name_convert(query)
	    company_name = full_name
	    if not full_name:
	    	full_name = query
	    symbols[full_name] = symbol
	symbol = symbols[full_name]
	if not symbol in companyinfo:
	   ticker = yf.Ticker(symbol)
	   companyinfo[symbol] = (
	    ticker.info['currentPrice'] if 'currentPrice' in ticker.info else -1,
	    ticker.info['logo_url']
	    )
	currprice, logo_url = companyinfo[symbol]
	if not full_name in cache:
		cache[full_name] = scrape_data(full_name)
	if len(cache[full_name])==0:
		 return {'data':[], 'sentiment':0, 'symbol':'', 'price':-1, 'logo_url':'', 'prediction':-1,'pricematrix':[]}
	mean_sentiment = mean([article['sentiment'] for article in cache[full_name]]) if len(cache[full_name])>0 else 0
	prediction = currprice+currprice*mean_sentiment
	if not symbol in pricedict:
		try:
			df = yf.download(symbol, start='2021-09-01', progress=False)
			pricelist = df['Close'].tolist()
			timelist = [int(datetime.timestamp(time)) for time in df.index]
			pricematrix = [[time,price] for time,price in zip(timelist, pricelist)]
			pricedict[symbol] = pricematrix
		except:
			pricedict[symbol] = []
	return {
		'data':cache[full_name], 
		'sentiment':mean_sentiment, 
		'symbol':symbol, 
		'price':currprice, 
		'logo_url':logo_url, 
		'prediction':prediction,
		'pricematrix':pricedict[symbol],
		'company_name':company_name
	}

@app.route('/', methods=['GET', 'POST'])
def home():
	form = QueryForm(request.form)
	q = "-1"
	if request.method == 'POST' and form.validate():
		q = form.query.data
		return redirect(url_for('search', query = q))
	# if not q then flash that it's wrong
	return render_template('landing.html', form=form)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True) # anyone can connect, and we're running on port 5000



