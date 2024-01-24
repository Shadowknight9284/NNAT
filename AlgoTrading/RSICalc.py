import pandas as pd
import yfinance as yf
import time
import yahoo_fin 
from datetime import datetime, timedelta

def calculate_rsi(ticker, start_date, end_date, period=14):
    # Download historical data
    data = yf.download(ticker, start_date, end_date , progress=False)['Close']

    # Calculate daily price changes
    data['Price Change'] = data['Close'].diff()

    # Separate gains and losses
    data['Gain'] = data['Price Change'].apply(lambda x: x if x > 0 else 0)
    data['Loss'] = data['Price Change'].apply(lambda x: abs(x) if x < 0 else 0)

    # Calculate average gain and average loss over the specified period
    avg_gain = data['Gain'].rolling(window=period, min_periods=1).mean()
    avg_loss = data['Loss'].rolling(window=period, min_periods=1).mean()

    # Calculate relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))

    # Add RSI to the DataFrame
    data['RSI'] = rsi

    return data[['Close', 'RSI']]

# Example usage
ticker_symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2022-12-31'

rsi_data = calculate_rsi(ticker_symbol, start_date, end_date)
print(rsi_data)
