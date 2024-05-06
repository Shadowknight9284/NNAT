import csv 
import pandas as pd
import yfinance as yf
import time
import yahoo_fin
import edgar
from datetime import datetime, timedelta
import sqlite3
from sec_api import RenderApi
import os
import multiprocessing

# This is the SQL class that will be getting the stock data from yfinance and from edgar and storing it in a SQL database
# I wish to put each day's stock data in a table with the name of the table being the date of the stock data
# Stock data is open, closing, high, low, volume. 
# Each stock also has information from the 10-K report.
# This database has 2 parts, the daily info and the 10-K info
# I want the data for the past ten years for each day and the past 10 years of 10-K reports
# https://stackoverflow.com/questions/74225258/downloading-all-10-k-filings-for-sec-edgar-in-python

renderApi = RenderApi(api_key="d26ded3e0bab10bba3857deaf9a482e6e497e258fd6b4f40096defb753e5e9de")

# download filing and save to "filings" folder
def download_filing(url):
  try:
    filing = renderApi.get_filing(url)
    # file_name example: 000156459019027952-msft-10k_20190630.htm
    file_name = url.split("/")[-2] + "-" + url.split("/")[-1] 
    download_to = "./filings/" + file_name
    with open(download_to, "w") as f:
      f.write(filing)
  except Exception as e:
    print("Problem with {url}".format(url=url))
    print(e)

# load URLs from log file
def load_urls():
  log_file = open("filing_urls.txt", "r")
  urls = log_file.read().split("\n") # convert long string of URLs into a list 
  log_file.close()
  return urls

def download_all_filings():
  print("Start downloading all filings")

  download_folder = "./filings" 
  if not os.path.isdir(download_folder):
    os.makedirs(download_folder)
    
  # uncomment next line to process all URLs
  urls = load_urls()
  urls = load_urls()[1:40]
  print("{length} filing URLs loaded".format(length=len(urls)))

  number_of_processes = 20

  with multiprocessing.Pool(number_of_processes) as pool:
    pool.map(download_filing, urls)
  
  print("All filings downloaded")
  
  
  

