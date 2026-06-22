# ============================================================
# FILE: day_1.py
# TOPIC: User Input, f-strings, datetime, String Formatting
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 1
# ============================================================
# Yeh challenge sikhata hai:
# - User se input lena (input() function)
# - String ko clean karna (.strip() se extra spaces hatao)
# - f-string se dynamic message banana
# - datetime module se aaj ki date nikalna
# - Decorative border banana string multiplication se ("*" * 80)
# ============================================================

"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

# datetime module = dates aur time handle karne ke liye Python ka built-in module
import datetime

# input() = user se keyboard se text mangta hai
# .strip() = string ke start/end ki extra spaces hata deta hai
name = input("What is your name ? ").strip()
age = input("How old are you ? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("WHat is your favourite hobby? ").strip()

# f-string (f"...") = variables ko string ke andar directly embed karo
# Multi-line string banane ke liye parentheses () use kiye gaye hain
intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)

# datetime.date.today() = aaj ki date return karta hai
# .isoformat() = date ko "YYYY-MM-DD" format mein convert karta hai (e.g. 2025-06-14)
current_date = datetime.date.today().isoformat()
# += operator = existing string ke end mein naya text jod do (concatenate)
intro_message += f"\n Logged on: {current_date}"

# "*" * 80 = 80 baar star character repeat karo (decorative border)
border = "*" * 80
# Final output = border + message + border (neeche wala border)
final_output = f"{border}\n{intro_message}\n{border}"

# print("\n" + ...) = pehle ek blank line, phir output
print("\n" + final_output)
