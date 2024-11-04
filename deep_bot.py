import requests
import pandas as pd
from datetime import datetime
import telegram_channel_bot

# Constants
BASE_URL = 'https://api.binance.com'
SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']  # List of currency pairs
INTERVAL = '1h'  # 1-hour intervals
LIMIT = 1000  # Maximum number of candlesticks
SMA_PERIOD = 20  # Simple Moving Average period

# Function to fetch candlestick data
def get_candlestick_data(symbol, interval, limit):
    url = f"{BASE_URL}/api/v3/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

# Function to calculate the Simple Moving Average (SMA)
def calculate_sma(df, period):
    df['sma'] = df['close'].rolling(window=period).mean()
    return df

# Function to suggest a trading deal
def suggest_deal(df, symbol):
    current_price = df['close'].iloc[-1]
    sma = df['sma'].iloc[-1]
    buy_range = (current_price * 0.98, current_price * 1.02)
    targets = [current_price * 1.05, current_price * 1.10, current_price * 1.15]
    stop_loss = current_price * 0.95

    if current_price > sma:
        suggestion = "Buy"
    else:
        suggestion = "Hold"

    message = (
        f"Suggestion: {suggestion}\n"
        f"Symbol: {symbol}\n"
        f"Buying Range: {buy_range[0]:.2f} - {buy_range[1]:.2f}\n"
        f"Target 1: {targets[0]:.2f}\n"
        f"Target 2: {targets[1]:.2f}\n"
        f"Target 3: {targets[2]:.2f}\n"
        f"Stop Loss: {stop_loss:.2f}"
    )
    return message

# Main function to fetch data, process, and send the recommendation for each currency
def main():
    for symbol in SYMBOLS:
        try:
            # Fetch candlestick data
            candlesticks = get_candlestick_data(symbol, INTERVAL, LIMIT)
            df = pd.DataFrame(candlesticks, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_asset_volume', 'number_of_trades',
                'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
            ])
            df['close'] = df['close'].astype(float)
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

            # Calculate SMA
            df = calculate_sma(df, SMA_PERIOD)

            # Get suggestion
            deal_message = suggest_deal(df, symbol)

            # Print the suggestion (or send via a bot)
            # print(deal_message)
            telegram_channel_bot.asyncio.run(telegram_channel_bot.ply(deal_message))

        except Exception as e:
            print(f"Error processing {symbol}: {e}")

if __name__ == "__main__":
    main()
