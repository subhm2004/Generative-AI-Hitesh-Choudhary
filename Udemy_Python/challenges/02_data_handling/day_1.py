# ============================================================
# FILE: day_1.py
# TOPIC: CSV file handling, csv module, DictReader
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 1
# ============================================================
# Yeh challenge sikhata hai:
# - CSV = Comma Separated Values (Excel jaisa tabular data)
# - csv.writer / csv.reader / csv.DictReader use karna
# - File create karna agar exist nahi karti (os.path.exists)
# - CRUD operations: Add, View, Search contacts
# - __name__ == "__main__" = script directly run hone par hi main() chale
# ============================================================

"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv   # CSV files read/write karne ke liye built-in module
import os    # file system operations (exists check etc.)

FILENAME = "contacts.csv"

# Agar contacts.csv nahi hai to nayi file banao with header row
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header row = column names (pehli line CSV mein)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    #check for duplicates
    with open(FILENAME, 'r', encoding="utf-8") as f:
        # DictReader = har row ko dictionary banata hai (column name -> value)
        reader = csv.DictReader(f)
        for row in reader:
           # .lower() se case-insensitive duplicate check
           if row["Name"].lower() == name.lower():
               print("Contact name already exists")
               return
    
    # "a" mode = append - naya contact file ke end mein add karo
    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")


def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)  # saari rows ek list mein

        if len(rows) < 1:
            print("No contacts found")
            return
        
        print("\n Your contacts: \n")

        # rows[1:] = header skip karo, sirf data rows dikhao
        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False  # flag variable - kya koi match mila?

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # "in" operator = partial match (naam ka koi part bhi match ho)
            if term in row["Name"].lower():
                print(f"{row["Name"]} | 📞 {row["Phone"]}")
                found = True

    if not found:
        print("No matching contact found")



def main():
    # Menu-driven loop
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4)").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our software")
            break
        else:
            print("Invalid choice of number")


# Yeh check karta hai ki file directly run hui hai (import nahi hui)
if __name__ == "__main__":
    main()
