# ============================================================
# FILE: day_8.py
# TOPIC: Recursive JSON flattening, isinstance()
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 8
# ============================================================
# Yeh challenge sikhata hai:
# - Nested JSON = dict ke andar dict, list ke andar items
# - Flatten = nested structure ko ek level par lao ("user.address.city")
# - Recursion = function khud ko call karta hai (nested data ke liye)
# - isinstance() = check karo data dict hai, list hai ya simple value
# - enumerate() = list items ke saath index number
# ============================================================

"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}


"""

import json
import os

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

# Recursive function = nested dict/list ko flat dict mein convert karta hai
def flatten_json(data, parent_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        # Agar data dictionary hai to har key-value par recurse karo
        for k, v in data.items():
            # parent_key.user jaisa full key banao
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            print(full_key)
            # items.update() = nested result ko merge karo
            items.update(flatten_json(v, full_key, sep=sep))

    elif isinstance(data, list):
        # Agar data list hai to index ke saath recurse karo
        for idx, item in enumerate(data):
            full_key =f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))
    else:
        # Base case = simple value (string, number, bool) - yahan ruk jao
        items[parent_key] = data

    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file found")
        return
    
    try:
        with open(INPUT_FILE, 'r', encoding="utf-8") as f:
            data = json.load(f)

        # User custom separator choose kar sakta hai (. ya -)
        sep = input("Enter your seperator like . or -: ").strip() or '.'

        flattened = flatten_json(data, sep=sep)
        with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
            json.dump(flattened, f, indent=2)

        print(f"Flattened JSON saved to {OUTPUT_FILE}")
    except Exception as e:
        print("Failed to faltten the data", e)

if __name__ == "__main__":
    main()
