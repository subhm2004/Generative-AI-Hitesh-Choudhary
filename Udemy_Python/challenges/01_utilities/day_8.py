# ============================================================
# FILE: day_8.py
# TOPIC: Password validation, getpass, random, any()
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 8
# ============================================================
# Yeh challenge sikhata hai:
# - Password strength rules check karna (length, upper, lower, digit, special)
# - any() function = kya koi bhi character condition satisfy karta hai?
# - getpass module = password type karte waqt screen par dikhta nahi
# - random.choice() se strong password generate karna
# - string.ascii_letters, digits, punctuation = character sets
# ============================================================

"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string   # letters, digits, punctuation ke ready-made sets
import random   # random values generate karne ke liye
import getpass  # password input hide karne ke liye (screen par nahi dikhega)

# Function jo password check kare aur problems ki list return kare
def check_password_strength(password):
    issues = []  # khali list - yahan sab problems store hongi
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
    # any(c.islower() for c in password) = kya KOI bhi character lowercase hai?
  # Generator expression = har character par check, efficient tarike se
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing a digit")
    if not any(c in string.punctuation  for c in password):
        issues.append("Missing a special character")
    return issues
    

# Random strong password generate karo
def generate_strong_password(length=12):
    # Teen character sets ko jod do = letters + digits + special chars
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # List comprehension + random.choice = har position par random char
    # _ = variable ki zaroorat nahi, sirf loop count ke liye
    return "".join(random.choice(chars) for _ in range(length))

# getpass.getpass = input jaisa but typing screen par nahi dikhti (security)
password = getpass.getpass("Enter a password: ")
issues = check_password_strength(password)

# not issues = agar list khali hai matlab password strong hai
if not issues:
    print("Strong password! you are good to go")
else:
    print("You got weak password")
    for issue in issues:
        print(f"- {issue}")

suggestion = generate_strong_password()
print("\n suggesting you a strong password")
print(suggestion)      
