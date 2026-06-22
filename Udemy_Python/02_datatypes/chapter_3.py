# ============================================================
# FILE: chapter_3.py
# TOPIC: INTEGER (Numbers) - Math operations in Python
# FOLDER: 02_datatypes
# ============================================================
# Python mein numbers se calculation karna bahut easy hai
# +, -, *, /, //, %, ** - ye sab operators hain
# ============================================================

# Integer (Numbers) - whole numbers without decimal

black_tea_grams = 14   # kaali chai ki quantity grams mein
ginger_grams = 3       # adrak ki quantity

# Addition (+) - dono ko jod do
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")  # 14 + 3 = 17

# Subtraction (-) - peeche wale se aage wala minus
remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")  # 14 - 3 = 11

# Division (/) - hamesha FLOAT result deta hai (decimal ke saath)
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")  # 7/4 = 1.75

# Integer Division (//) - sirf POORA number, decimal kaat deta hai
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")  # 7//4 = 1 (1.75 nahi!)

# Modulus (%) - BACHA hua number (remainder) deta hai
total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")  # 10 % 3 = 1 (3+3+3=9, 1 bacha)

# Multiplication (*) - number ko kitni baar multiply karo
a = 14
b = 15
print(a * b)  # 14 * 15 = 210

# Power (**) - number ko power mein uthao (exponent)
base_flavor_strength = 2
scale_factor = 3
powerful_falvour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strenght {powerful_falvour}")  # 2**3 = 2*2*2 = 8

# Underscore (_) numbers mein padhne ke liye - value same rehti hai
total_tea_leaves_harvested = 1_000_000_000  # 1 billion - padhna easy
print(f"tea leaves: {total_tea_leaves_harvested}")
