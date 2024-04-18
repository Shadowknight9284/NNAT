import pandas as pd
import yfinance as yf
import time
import yahoo_fin 
from datetime import datetime, timedelta

class Stock:
    def __init__(self , ticker, open, high, low, close, volume, adj_close, date):
        self.ticker = ticker
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adj_close = adj_close
        self.date = date
        
    def __init__(self, ticker):
        self.ticker = ticker
        self.open = 0
        self.high = 0
        self.low = 0
        self.close = 0
        self.volume = 0
        self.adj_close = 0
        self.date = 0
        
    
        