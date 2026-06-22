# ============================================================
# FILE: day_9.py
# TOPIC: Base64 encoding, password strength, file vault
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 9
# ============================================================
# Yeh challenge sikhata hai:
# - Base64 = text ko encoded format mein convert (simple obfuscation)
# - base64.b64encode() / b64decode() = encode/decode functions
# - Password strength scoring system
# - File mein encoded credentials save karna (|| separator)
# - match-case menu driven program
# ============================================================

"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64  # encoding/decoding ke liye built-in module
import os

VAULT_FILE = "vault.txt"

# Text ko Base64 encoded string mein convert karo
def encode(text):
    # .encode() = string -> bytes, b64encode = encode, .decode() = bytes -> string
    return base64.b64encode(text.encode()).decode()

# Base64 string ko wapas original text mein convert karo
def decode(text):
    return base64.b64decode(text.encode()).decode()

# Password ki strength check karo aur label return karo
def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)

    # Har condition True hai to 1 point - total score 0-4
    score = sum([length >= 8, has_upper, has_digit, has_special])
    # Score ke hisaab se label return (min cap at index 3)
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    # || separator se fields jod do, phir encode karo
    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    # Encoded line file mein append karo (har credential ek line)
    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encoded_line + "\n")

    print("✅ Credential saved")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())  # decode karke original text
            website, username, password = decoded.split("||")
            hidden_password = '*' * len(password)  # mask password with stars
            print(f"{website} | {username} | {password}")


def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "4": break
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()
