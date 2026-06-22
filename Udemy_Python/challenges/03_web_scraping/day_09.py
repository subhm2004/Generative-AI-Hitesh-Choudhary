# ============================================================
# FILE: day_09.py
# TOPIC: SQLite database, SQL queries in Python
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 09
# ============================================================
# Yeh challenge sikhata hai:
# - SQLite = lightweight database (ek file mein poora DB)
# - sqlite3.connect() = database file se connect karo
# - cursor.execute() = SQL query run karo
# - CREATE TABLE IF NOT EXISTS = table banao agar nahi hai
# - INSERT / SELECT queries with parameterized values (?)
# - conn.commit() = changes permanently save karo
# ============================================================

"""
 Challenge: Store & Search Crypto Prices in SQLite

Goal:
- Save hourly top 10 crypto prices into a local SQLite database
- Each record should include timestamp, coin ID, and price
- Allow the user to search for a coin by name and return the latest price

Teaches: SQLite handling in Python, data storage, search queries, API + DB integration
"""
import os
import csv
from datetime import datetime
import requests
import schedule
import time
import sqlite3  # built-in SQLite database module

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

DB_NAME = 'crypto.db'  # database ek file ban jayegi

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

# Database table create karo (agar pehle se nahi hai)
def create_table():
    conn = sqlite3.connect(DB_NAME)  # connect = file open/create
    cursor = conn.cursor()  # cursor = SQL commands run karne ke liye
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   coin TEXT,
                   price REAL
                   )
''')
    conn.commit()  # changes save karo
    conn.close()   # connection band karo (important!)

def save_to_database(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data:
        # ? = parameterized query (SQL injection se bachne ke liye)
        cursor.execute('''
            INSERT INTO crypto_prices (timestamp, coin, price)
                       VALUES (?, ?, ?)
''', (timestamp, coin['id'], coin['current_price']))
        
    conn.commit()
    conn.close()
    print("Price saved to database")

def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # ORDER BY timestamp DESC = newest pehle, LIMIT 1 = sirf latest
    cursor.execute('''
        SELECT timestamp, price FROM crypto_prices
                   WHERE coin = ?
                   ORDER BY timestamp DESC
                   LIMIT 1
''', (coin_name, ))
    result = cursor.fetchone()  # ek row return (tuple)
    conn.close()
    # print("RESULT RAW", result)
    if result:
        print(f"${result[1]} - {result[0]}")  # result[1]=price, result[0]=timestamp
    

def main():
    create_table()
    print("1. Fetch and store crypto data")
    print("2. Search latest price for a coin")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        data = fetch_crypto_data()
        save_to_database(data)
    elif choice == "2":
        coin_name = input("Enter coin name: ").strip().lower()
        search_coin(coin_name)
    else:
        print("Invalid option")


main()
