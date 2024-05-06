import pandas as pd
import yfinance as yf
import time
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
    def __init__(self, ticker, closing, volume, SMA_5, SMA_50, RSI ):
        self.ticker = ticker
        self.closing = closing
        self.volume = volume
        self.SMA_5 = SMA_5
        self.SMA_50 = SMA_50
        self.RSI = RSI
        
    def __init__(self, ticker):
        self.ticker = ticker
        self.closing = [0]
        self.volume = [0]
        self.SMA_5 = [0]
        self.SMA_50 = [0]
        self.RSI = [0]
        
    def calcRSI(self):
        data = self.closing
        daily_change = data.diff()
        gain = daily_change.apply(lambda x: x if x > 0 else 0)
        loss = -daily_change.apply(lambda x: x if x < 0 else 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        relative_strength = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + relative_strength))
        return rsi

    def calcSMA_N(self, n):
        SMA_N = self.closing.rolling(window=n).mean()
        return SMA_N

    def calc(self):
        self.closing = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Close']
        self.volume = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Volume']
        self.open = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Open']
        self.high = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['High']
        self.low = yf.download(self.ticker, start= start_date, end=today_date, progress=False)['Low']
        self.SMA_5 = self.calcSMA_N(5)
        self.SMA_50 = self.calcSMA_N(50)
        self.RSI = self.calcRSI()
    
    def display_info(self):
        closing = self.closing
        volume = self.volume
        SMA_5 = self.SMA_5
        SMA_50 = self.SMA_50
        RSI = self.RSI
        print("This is A Stock named: " + self.ticker + "\nToday's Closing: " + str(closing.iloc[-1]) + "\nToday's Volume: " + str(volume.iloc[-1]) + "\nToday's SMA_5: " + str(SMA_5.iloc[-1]) + "\nToday's SMA_50: " + str(SMA_50.iloc[-1]) +"\nToday's RSI: "+ str(RSI.iloc[-1]))
        
    def extended_info(self):
        print(self.ticker + "\n" + str(self.RSI))
        # Print the latest 10 Days of Data for all stocks 

    def to_csv(self):
        data = pd.concat([self.high, self.low, self.closing, self.volume, self.open], axis=1)
        data.columns = ['High', 'Low', 'Closing', 'Volume', 'Open']
        data.to_csv('csvFolder/' + self.ticker + '_data.csv')
        
    def to_sql(self):
        conn = sqlite3.connect('sqlFolder/' + self.ticker + '_data.csv') #add a path to the database
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
        
    def plotRSI(self):
        plt.plot(self.RSI)
        plt.title('RSI')
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
        test.display_info()
        test.to_csv()

    except Exception as e:
        print(f"Skipping {test.ticker}. Error: {e} Index: {i}")
    i = i + 1
    
stocks[0].extended_info()

end = time.time()

print(f"Time taken: {end-start} seconds")



# Make a array of stock objects
# then make it 