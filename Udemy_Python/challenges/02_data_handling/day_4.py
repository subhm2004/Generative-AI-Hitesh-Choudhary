# ============================================================
# FILE: day_4.py
# TOPIC: REST API, requests library, CSV logging
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 4
# ============================================================
# Yeh challenge sikhata hai:
# - API = Application Programming Interface (internet se data lena)
# - requests.get() = website/API se data fetch karna
# - response.json() = API response ko Python dict mein convert
# - response.status_code = request successful thi ya nahi (200 = OK)
# - CSV mein API data log karna with duplicate prevention
# ============================================================

"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests  # HTTP requests bhejne ke liye (pip install requests)

FILENAME = "weather_logs.csv"
API_KEY = "Get Your own key here" 
# keys are usually hidden in .env file but that is for later

# CSV file create karo agar nahi hai
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
   city = input("Enter your city name: ").strip()
   # Aaj ki date "YYYY-MM-DD" format mein
   date = datetime.now().strftime("%Y-%m-%d")

   # Duplicate check - same city + same date pehle se logged hai?
   with open(FILENAME, "r", newline='', encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          if row["Date"] == date and row['City'].lower() == city.lower():
              print("Entry for this city and date exists")
              return
          
   try:
       # API URL banao - city name aur API key query parameters mein
       url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
       response = requests.get(url)  # GET request bhejo
       data = response.json()  # JSON response -> Python dictionary

       # status_code 200 nahi hai to error (404 = city not found, 401 = bad API key)
       if response.status_code != 200:
           print(f"API Error ")
           return
       # Nested dict se temperature aur condition nikalo
       temp = data["main"]["temp"]
       condition = data["weather"][0]["main"]

       # CSV mein naya row append karo
       with open(FILENAME, "a", newline='', encoding="utf-8") as f:
           writer = csv.writer(f)
           writer.writerow([date, city.title(), temp, condition])
           print(f"Logged: {temp} {condition} in {city.title()} on {date}")
   except Exception as e:
       print("Failed to make API call")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No Entries")
            return
        # reader[1:] = header row skip
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")


def main():
    while True:
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View weather log")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case _: print("Invalid choice")


if __name__ == "__main__":
    main()
