# ============================================================
# FILE: day_6.py
# TOPIC: JSON to CSV conversion, DictWriter
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 6
# ============================================================
# Yeh challenge sikhata hai:
# - JSON file se data read karna (API response jaisa format)
# - CSV mein convert karna (Excel mein open karne ke liye)
# - csv.DictWriter = dictionary rows ko CSV mein likho
# - data[0].keys() = pehle record se column names (headers) nikalo
# - File existence check aur error handling
# ============================================================

"""
 Challenge: JSON-to-CSV Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""
import json
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)  # JSON array of dicts -> Python list
        except:
            print("Invalid JSON format")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    
    # Pehle record ke keys = CSV column headers
    fieldname = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        # DictWriter = har dict ko ek CSV row banata hai
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()  # pehli line = column names
        for record in data:
            writer.writerow(record)  # har record ek row
    
    print(f"Converted {len(data)} records to {output_file}")


def main():
    print("Converting JSON to CSV....")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
