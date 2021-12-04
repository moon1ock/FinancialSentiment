import asyncio
import time 
import aiohttp
from aiohttp.client import ClientSession
from bs4 import BeautifulSoup



class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls

        self.all_data  = []
        self.master_dict = {}
        # Run The Scraper:
        asyncio.run(self.main())

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                # 1. Extracting the Text:
                text = await response.text()
                # 2. Extracting the  Tag:
                title_tag = await self.extract_title_tag(text)
                return text, url, title_tag
        except Exception as e:
            print(str(e))

    async def extract_title_tag(self, text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            return soup.title
        except Exception as e:
            print(str(e))

    async def main(self):
        tasks = []
        headers = {
            "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        async with aiohttp.ClientSession(headers=headers) as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            # Storing the raw HTML data.
            for html in htmls:
                if html is not None:
                    url = html[1]
                    self.master_dict[url] = {'Raw Html': html[0], 'Title': html[2]}
                else:
                    continue

# urls = ['https://www.apple.com/newsroom/2021/12/apple-fitness-plus-will-feature-prince-william-on-time-to-walk-starting-december-6/',
#  'https://www.apple.com/newsroom/2021/12/app-store-awards-honor-the-best-apps-and-games-of-2021/',
#  'https://www.apple.com/newsroom/2021/12/apple-rosenthaler-strasse-opens-thursday-december-2-in-berlin/',
#  'https://9to5mac.com/2021/12/03/poll-do-you-think-apple-will-replace-the-iphone-with-an-ar-device-in-10-years/',
#  'https://www.macrumors.com/2021/12/03/apple-nso-group-state-department-notifications/',
#  'https://www.bloomberg.com/news/articles/2021-12-02/apple-tells-suppliers-iphone-demand-has-slowed-as-holidays-near',
#  'https://www.macrumors.com/2021/12/03/apple-executive-talk-apple-watch-bands/']

# scraper = WebScraper(urls = urls)
# print(scraper.master_dict[urls[0]]['Title'])