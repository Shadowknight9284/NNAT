import pandas as pd
import yfinance as yf
import time
import yahoo_fin 
start = time.time()

# Initial Data
today_date = '2024-01-17'
start_date = '2023-01-01'
# Date Time implimentation

# Read the CSV
file = pd.read_csv('stocks.csv')

stock_5over50 = []
i = 0
for index in file.iterrows() :
    try:
        # Call the index of the csv
        current_stock =  file.iloc[i, 0]

        # Stock Data
        stock_data = yf.download(current_stock, start= start_date, end=today_date, progress=False)['Close']

        # Calculate the 5-day moving average
        stock_data_5_SMA = stock_data.rolling(window=5).mean()

        # Calculate the 50-day moving average
        stock_data_50_SMA = stock_data.rolling(window=50).mean()

        # Extract today's and yesterday's 5-day moving average
        today_5_day_MA = stock_data_5_SMA.iloc[-1]
        yesterday_5_day_MA = stock_data_5_SMA.iloc[-2]
        today_50_day_MA = stock_data_50_SMA.iloc[-1]
        yesterday_50_day_MA = stock_data_50_SMA.iloc[-2]

        # Check if today's 5_day is greater than 50_day and yesterdays 50_day is greater than 5_day
        if (today_5_day_MA > today_50_day_MA) & (yesterday_50_day_MA > yesterday_5_day_MA):
            stock_5over50 = [i] + stock_5over50
            # ADD STOCK TICKER INSTEAD OF NUMBER
    except Exception as e:
        print(f"Skipping {current_stock}. Error: {e} Index: {i}")
    
    i = i + 1
    
    
end = time.time()

# Print the results
print(stock_5over50) 
print((end-start))

