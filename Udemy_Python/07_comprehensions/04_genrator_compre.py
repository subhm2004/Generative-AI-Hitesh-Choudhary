# ============================================================
# FILE: 04_genrator_compre.py
# TOPIC: GENERATOR EXPRESSION - memory-efficient lazy iteration
# FOLDER: 07_comprehensions
# ============================================================
# Generator Expression = comprehension jaisa dikhta hai par () use hota hai
# List [] sab values EK SAATH memory mein store karta hai
# Generator () values EK-EK KARKE deta hai (lazy) - kam memory use
# sum() function generator expression ke saath bahut common hai
# Syntax: (expression for item in iterable if condition)
# ============================================================

# daily_sales = list of integers - har din kitni cups chai biki
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# Generator expression + sum() function
# sum(sale for sale in daily_sales if sale > 5) ka matlab:
#   daily_sales se sirf wo sales lo jahan sale > 5 (5 se zyada cups biki)
#   Un sab ka total jodo
# Parentheses () = generator expression (list [] nahi banega, seedha sum ke liye iterate)
# Ye memory efficient hai kyunki poori list banane ki zaroorat nahi
total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
