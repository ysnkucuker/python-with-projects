import requests
import time

# Trading pair symbol
SYMBOL = "BTCUSDT"

# Binance public API endpoint
API_URL = "https://api.binance.com/api/v3/ticker/price"

# List to store recent prices
prices = []

# Number of prices used for moving average
WINDOW_SIZE = 5


def get_price(symbol):
    """
    Sends a GET request to Binance API and returns the current price.

    Example API response (JSON):
    {
        "symbol": "BTCUSDT",
        "price": "43215.12000000"
    }

    Explanation:
    - symbol: Trading pair (BTC/USDT)
    - price: Current market price as a STRING
    """

    response = requests.get(API_URL, params={"symbol": symbol})

    # Convert JSON response to Python dictionary
    data = response.json()

    # Convert price from string to float
    return float(data["price"])


def moving_average(price_list):
    """
    Calculates the simple moving average of given prices.
    """
    return sum(price_list) / len(price_list)


while True:
    try:
        # Fetch current market price
        current_price = get_price(SYMBOL)

        # Store price in the list
        prices.append(current_price)

        # Keep only the last WINDOW_SIZE prices
        if len(prices) > WINDOW_SIZE:
            prices.pop(0)

        print(f"Current Price: {current_price:.2f}")

        # Calculate strategy only if enough data exists
        if len(prices) == WINDOW_SIZE:
            avg_price = moving_average(prices)

            # Simple trading strategy
            if current_price < avg_price:
                print("📉 SIGNAL: BUY")
            elif current_price > avg_price:
                print("📈 SIGNAL: SELL")
            else:
                print("⏸️ SIGNAL: HOLD")

            print(f"Moving Average: {avg_price:.2f}")

        print("-" * 40)

        # Wait 5 seconds before next request
        time.sleep(5)

    except Exception as error:
        print("Error occurred:", error)
        time.sleep(5)
