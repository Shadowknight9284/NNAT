import yfinance as yf
import pandas as pd

def calculate_rsi(symbol, start_date, end_date):
    # Fetch historical stock closing prices
    data = yf.download(symbol, start=start_date, end=end_date, progress=False)['Close']

    # Calculate daily price changes
    daily_change = data.diff()

    # Calculate average gain and average loss
    gain = daily_change.apply(lambda x: x if x > 0 else 0)
    loss = -daily_change.apply(lambda x: x if x < 0 else 0)

    # Calculate rolling average over a specified period (e.g., 14 days)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    # Calculate relative strength (RS)
    relative_strength = avg_gain / avg_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + relative_strength))

    # Create a new DataFrame with Date and RSI columns
    rsi_values = rsi.tolist()

    return rsi_values

# Example usage
symbol = 'AAPL'  # Replace with the desired stock symbol
start_date = '2022-01-01'
end_date = '2022-12-31'

rsi_result = calculate_rsi(symbol, start_date, end_date)
print(rsi_result)
