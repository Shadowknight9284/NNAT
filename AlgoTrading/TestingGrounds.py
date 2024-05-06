import pandas as pd
import yfinance as yf
import time
import yahoo_fin 
from datetime import datetime, timedelta
import numpy as np
import sqlite3
import csv
import matplotlib.pyplot as plt

start = time.time()
today_date = datetime.today()
previous_date = today_date - timedelta(days=100)
start_date = previous_date.strftime('%Y-%m-%d')
print("Today's Date: " + start_date)


class Stock:
    def __init__(self, ticker, closing, volume, high, low):
        self.ticker = ticker
        self.closing = closing
        self.volume = volume
        self.high = high
        self.low = low
        
    def __init__(self, ticker):
        self.ticker = ticker
        self.closing = [0]
        self.volume = [0]
        self.high = [0]
        self.low = [0]

    def calc(self):
        self.closing = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Close']
        self.volume = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Volume']
        self.open = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Open']
        self.high = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['High']
        self.low = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Low']
        
    
    def display_infoToday(self):
        print(f"Stock: {self.ticker}")
        print(f"Closing Price: {self.closing.iloc[-1]}")
        print(f"Volume: {self.volume.iloc[-1]}")
        print(f"Open Price: {self.open.iloc[-1]}")
        print(f"High Price: {self.high.iloc[-1]}")
        print(f"Low Price: {self.low.iloc[-1]}")

    def to_csv(self):
        data = pd.concat([self.high, self.low, self.closing, self.volume, self.open], axis=1)
        data.columns = ['High', 'Low', 'Closing', 'Volume', 'Open']
        data.to_csv('csvFolder/' + self.ticker + '_data.csv')
        
    def to_sql(self):
        conn = sqlite3.connect('') #add a path to the database
        data = pd.concat([self.high, self.low, self.closing, self.volume, self.open], axis=1)
        data.columns = ['High', 'Low', 'Closing', 'Volume', 'Open']
        data.to_sql(self.ticker, conn, if_exists='replace')
        
    def plotHigh(self):
        plt.plot(self.high)
        plt.title('High Price')
        plt.show()
        
    def plotLow(self):
        plt.plot(self.low)
        plt.title('Low Price')
        plt.show()
        
    def plotClosing(self):
        plt.plot(self.closing)
        plt.title('Closing Price')
        plt.show()
        
    def plotOpen(self):
        plt.plot(self.open)
        plt.title('Opening Price')
        plt.show()
        
    def plotVolume(self):
        plt.plot(self.volume)
        plt.title('Volume')
        plt.show()
        
# Test
stock_csv = "test.csv"
df = pd.read_csv(stock_csv)  
stocks = []
i = 0

for index in df.iterrows():
    stocks.append(Stock(df.iloc[i,0]))
    try:
        test = stocks[i]
        test.calc()
        test.display_infoToday()
        test.to_csv()

    except Exception as e:
        print(f"Skipping {test.ticker}. Error: {e} Index: {i}")
    i = i + 1
    
end = time.time()

print(f"Time taken: {end-start} seconds")

# Make a array of stock objects
# then make it 