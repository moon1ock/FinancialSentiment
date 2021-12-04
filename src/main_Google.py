# create certificate ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.9/etc/openssl 

from flask import Flask, render_template,request, redirect, url_for
from flask_cors import CORS
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

from wtforms import Form, BooleanField, StringField, PasswordField, validators


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

	url = "https://news.google.com/rss/search?q=intitle:{}+after:2021-11-01&ceid=US:en&hl=en-US&gl=US".format(q)

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
	url = "https://news.google.com/rss/search?q=intitle:{}+after:2021-11-01&ceid=US:en&hl=en-US&gl=US".format(q)

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
	if not query in cache:
		cache[query] = scrape_data(query)
	return {'data':cache[query]}

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



