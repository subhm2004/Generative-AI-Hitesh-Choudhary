# ============================================================
# FILE: day_07.py
# TOPIC: CoinGecko API, CSV logging, matplotlib graphs
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 07
# ============================================================
# Yeh challenge sikhata hai:
# - Public API se live crypto prices fetch karna
# - API params dictionary = query parameters pass karna
# - CSV mein timestamped data append karna (time series data)
# - os.path.isfile() = file pehle se hai ya nahi (header likhne ke liye)
# - Matplotlib se price vs time graph plot karna
# ============================================================

"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""
import os
import csv
from datetime import datetime
import requests
import matplotlib.pyplot as plt


API_URL = "https://api.coingecko.com/api/v3/coins/markets"

# API query parameters - CoinGecko ko batate hain kya data chahiye
PARAMS = {
    'vs_currency': 'usd',        # prices in US dollars
    'order': 'market_cap_desc',  # market cap ke hisaab se sort
    'per_page':10,               # top 10 coins
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    # params=PARAMS automatically URL mein query string banata hai
    response = requests.get(API_URL, params=PARAMS)
    return response.json()  # list of coin dictionaries

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        # Pehli baar file bana rahe hain to header row likho
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        # Har coin ke liye ek row append karo
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin['current_price']])
    print("✅ data saved to csv")


def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Sirf selected coin ka data filter karo
            if row["coin"] == coin_id:
                times.append(row['timestamp'])
                prices.append(float(row['price']))

    if not times:
        print(f"No data found for {coin_id}")
        return
    
    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()


def main():
    print("Fetching live crypto data....")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['id']} - ${coin['current_price']}")
    print("-" * 30)

    choice = input("Enter the coinname to get graph: ").strip().lower()

    if choice:
        plot_graph(choice)


if __name__ == "__main__":
    main()
