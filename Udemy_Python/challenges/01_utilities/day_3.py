# ============================================================
# FILE: day_3.py
# TOPIC: Functions, for loop, list, try-except, round()
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 3
# ============================================================
# Yeh challenge sikhata hai:
# - Custom function banana jo valid number input ensure kare
# - try-except se invalid input handle karna (error handling)
# - for loop se multiple names collect karna
# - List mein items append karna
# - Division aur round() se bill split karna
# ============================================================

"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

# Custom function = valid float number input lene ke liye
# Jab tak user sahi number nahi deta, loop chalta rahega
def get_float(prompt):
    while True:  # infinite loop - tab tak chalega jab tak valid input na mile
        try:
            # float() = string ko decimal number mein convert karta hai
            return float(input(prompt))
        except ValueError:
            # ValueError = jab conversion fail ho (e.g. user ne "abc" type kiya)
            print("❌ Please enter a valid number. ")

# int() = string ko whole number (integer) mein convert karta hai
num_people = int(input("How many people are there in the group? "))
names = []  # khali list banayi - yahan sabke names store honge

# range(num_people) = 0 se num_people-1 tak numbers generate karta hai
# for loop = har person ka naam ek ek karke poocho
for i in range(num_people):
    # f-string mein {i+1} = 1 se start hoga (0 nahi) - user-friendly numbering
    name = input(f"Enter the name of persion #{i+1}").strip()
    names.append(name)  # list ke end mein naam add karo

total_bill = get_float("Enter the bill amount in number only")

# round(value, 2) = 2 decimal places tak round karo (e.g. 400.00)
share = round(total_bill / num_people, 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person owes {share}")

# for name in names = list ke har item par loop chalao
for name in names:
    print(f"{name} owes {share} rupees")

print("\n" + "*" * 40)
