import asyncio
import time 
import aiohttp
from aiohttp.client import ClientSession
from bs4 import BeautifulSoup
import metadata_parser
from textblob import TextBlob




class WebScraper(object):
	def __init__(self, urls):
		self.urls = urls
		self.all_data  = []
		self.master_dict = {}

		asyncio.run(self.main())

	async def fetch(self, session, url):
		try:
			async with session.get(url) as response:
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
			article = {}
			article['description'] = page.get_metadatas('description')[0]
			article['title'] = page.get_metadatas('title')[0]
			article['url'] = page.get_metadata_link('url')
			article['image'] = page.get_metadata_link('image')
			article['site_name'] = page.get_metadatas('site_name')[0]
			article['sentiment'] = round((TextBlob(article['title']).sentiment.polarity+TextBlob(article['description']).sentiment.polarity)/2,3)
			return article
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

urls = ['https://www.apple.com/newsroom/2021/12/apple-fitness-plus-will-feature-prince-william-on-time-to-walk-starting-december-6/',
 'https://www.apple.com/newsroom/2021/12/app-store-awards-honor-the-best-apps-and-games-of-2021/',
 'https://www.apple.com/newsroom/2021/12/apple-rosenthaler-strasse-opens-thursday-december-2-in-berlin/',
 'https://9to5mac.com/2021/12/03/poll-do-you-think-apple-will-replace-the-iphone-with-an-ar-device-in-10-years/',
]

scraper = WebScraper(urls = urls)
for key, val in scraper.master_dict.items():
	print(key, val)
	print('______')