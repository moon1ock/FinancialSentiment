from googlesearch import search
import yfinance as yf
import pandas as pd

def name_convert(a):

    searchval = 'yahoo finance '+a
    link = []
    #limits to the first link
    for url in search(searchval, tld='es', lang='es', stop=1):
        link.append(url)

    link = str(link[0])
    link=link.split("/")

    if link[-1]=='':
        ticker=link[-2]
    else:
        x=link[-1].split('=')
        ticker=x[-1]

    long_name = yf.Ticker(ticker).info['longName']
    return ticker, long_name


company_name=input("Enter a company name: ")
try:
  company_ticker, true_name = name_convert(company_name)
  # fixed typos
  print('The true name of the company:', true_name)
  print()
  # stock data
  df = yf.download(company_ticker, start='2021-09-01', progress=False)
#   df['Close'].plot(title="{}'s stock price".format(company_ticker))
  print(df)
except:
  print("Can't recognize the company")
