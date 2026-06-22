# ============================================================
# FILE: day_7.py
# TOPIC: CSV to JSON conversion, DictReader
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 7
# ============================================================
# Yeh challenge sikhata hai:
# - CSV file ko JSON mein convert karna (reverse of day_6)
# - csv.DictReader = har CSV row ek dictionary ban jati hai
# - list(reader) = saari rows ek list mein collect karo
# - json.dumps() = dict ko formatted JSON string mein (preview ke liye)
# - json.dump() = Python data ko JSON file mein save
# ============================================================

"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import os
import json
import csv

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        # DictReader = header row se column names leta hai, har row = dict
        reader = csv.DictReader(f)
        data = list(reader)  # saari rows ek list of dicts mein
        print(data)
        return data
    
def save_as_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)  # pretty JSON file save
    print(f"✅ Converted {len(data)} records to {filename}")

def preview_data(data, count=3):
    # Pehle 3 records preview dikhao (json.dumps = readable format)
    for row in data[:count]:
        print(json.dumps(row, indent=2))
    print(".......")


def main():

    data = load_csv_data(INPUT_FILE)
    if not data:
        return
    save_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main()
