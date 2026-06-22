# ============================================================
# FILE: day_4.py
# TOPIC: Functions, while loop, try-except, tuple unpacking
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 4
# ============================================================
# Yeh challenge sikhata hai:
# - Function jo calculation kare aur multiple values return kare
# - Constants (DAYS_IN_YEAR etc.) use karna
# - while True loop = program tab tak chale jab tak user exit na kare
# - Tuple unpacking: days, hours, minutes = function()
# - Age ko days, hours, minutes mein convert karna
# ============================================================

"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""

# Function jo age (years) ko days, hours, minutes mein convert karta hai
def calculate_minutes(age_years):
    # Constants = fixed values jo program mein change nahi hote (UPPERCASE naming convention)
    DAYS_IN_YEAR = 365.25   # leap years account karne ke liye 365.25 use kiya
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR

    # return = teen values ek saath return (tuple ban jata hai)
    return round(total_days), round(total_hours), round(total_minutes)

# while True = loop tab tak chalega jab tak hum manually break na karein
while True:
    try:
        age = float(input("Enter your age in years: "))
        # Tuple unpacking = function se 3 values ek saath variables mein store
        days, hours, minutes = calculate_minutes(age)

        print("\n You are approx:")
        print(f"  -  {days} days old")
        print(f"  -  {hours} hours old")
        print(f"  -  {minutes} minutes old\n")

        again = input("Would you like to try again? (y/n)").strip().lower()

        # Agar user 'y' nahi bola to loop se bahar niklo
        if again != 'y':
            print("Good bye!")
            break  # while loop ko tod do
    except:
        # Bare except = koi bhi error aaye to yeh message dikhao
        print("Please enter a valid number for age")
