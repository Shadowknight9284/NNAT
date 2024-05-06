import pandas as pd
import yfinance as yf
import time
import yahoo_fin 
from datetime import datetime, timedelta
import numpy as np
import sqlite3
import csv
import matplotlib.pyplot as plt

class StockMomentum:
    def __init__(self): 
        self.stock = None
        self.RSI = None
        self.SMA_5 = None
        self.SMA_50 = None
        
    def __init__(self, stock):
        self.stock = stock
        self.RSI = stock.calcRSI()
        self.SMA_5 = stock.calcSMA_N(5)
        self.SMA_50 = stock.calcSMA_N(50)
        
    def calc(self):
        self.RSI = self.calcRSI()
        self.SMA_5 = self.calcSMA_N(5)
        self.SMA_50 = self.calcSMA_N(50)
        
    def calcRSI(self):
        data = self.stock.closing
        daily_change = data.diff()
        gain = daily_change.apply(lambda x: x if x > 0 else 0)
        loss = -daily_change.apply(lambda x: x if x < 0 else 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        relative_strength = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + relative_strength))
        return rsi

    def calcSMA_N(self, n):
        SMA_N = self.stock.closing.rolling(window=n).mean()
        return SMA_N
    
    
    
        
    
        
    
        

        
        
    