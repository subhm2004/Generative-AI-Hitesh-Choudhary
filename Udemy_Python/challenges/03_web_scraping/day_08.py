# ============================================================
# FILE: day_08.py
# TOPIC: schedule library, automated hourly jobs
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 08
# ============================================================
# Yeh challenge sikhata hai:
# - schedule library = tasks ko time par automatically run karna
# - schedule.every().hour.at(":00") = har ghante ke :00 par run karo
# - schedule.run_pending() = due tasks check karo aur run karo
# - while True + time.sleep(60) = har minute check karo
# - Day 07 ka code reuse karke automated tracker banana
# ============================================================

"""
depends on:
 - Day 7 of web scraping

Fetch crypto data every hour automatically

"""

import os
import csv
from datetime import datetime
import requests
import schedule  # pip install schedule - task scheduling ke liye
import time

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin['current_price']])
    print("✅ data saved to csv")


# Yeh function har ghante automatically chalega
def job():
    print("Fetching data hourly...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

# Schedule setup: har ghante ke :00 minute par job() run karo
schedule.every().hour.at(":00").do(job)

# Infinite loop - program tab tak chalega jab tak manually band na karo
while True:
    schedule.run_pending()  # koi scheduled task due hai to run karo
    time.sleep(60)  # 60 seconds wait, phir dobara check karo
