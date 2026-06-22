# ============================================================
# FILE: day_5.py
# TOPIC: matplotlib, data visualization, defaultdict
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 5
# ============================================================
# Yeh challenge sikhata hai:
# - matplotlib.pyplot = graphs aur charts banane ke liye
# - CSV se data read karke graphs plot karna
# - plt.plot() = line graph, plt.bar() = bar chart
# - defaultdict(int) = missing keys ke liye auto 0 value
# - plt.show() = graph window mein dikhana
# ============================================================

"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data


"""
import csv
from collections import defaultdict  # auto-default value wala dictionary
import matplotlib.pyplot as plt  # plotting library (pip install matplotlib)

FILENAME = "weather_logs.csv"

def visualize_weather():
    dates = []    # x-axis ke liye dates
    temps = []    # y-axis ke liye temperatures
    # defaultdict(int) = agar key nahi hai to automatically 0 se start
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(row["Temperature"])
                # Har condition ka count badhao (kitni baar aayi)
                conditions[row["Condition"]] += 1
            except:
                continue  # corrupt row skip karo
    if not dates:
        print("NO data is available")
        return
    
    # ----- LINE GRAPH: Temperature over time -----
    plt.figure(figsize=(10, 7))  # graph ka size (width, height inches mein)
    plt.plot(dates, temps, marker='o')  # line graph with circle markers
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()  # labels overlap na karein
    plt.grid(True)  # background grid lines
    plt.show()  # graph window open karo

    # ----- BAR CHART: Weather conditions count -----
    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.show()



visualize_weather()
