# ============================================================
# FILE: chapter_7.py
# TOPIC: TUPLE - immutable ordered collection
# FOLDER: 02_datatypes
# ============================================================
# Tuple = ordered list jaisa, lekin IMMUTABLE (change nahi ho sakta)
# Syntax: (item1, item2, item3) - round brackets
# Use case: fixed data jo change nahi hona chahiye (coordinates, RGB)
# ============================================================

# Tuples (Tuples are immutable - ek baar bana toh badal nahi sakte)

masala_spices = ("cardamom", "cloves", "cinnamon")  # 3 masale ka tuple

print(type(masala_spices))  # <class 'tuple'>
print(f"Masala spices: {masala_spices}")
print(len(masala_spices))   # 3 items hain

print("\n")

# Tuple UNPACKING - ek saath saari values alag variables mein daal do
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

print("\n")

# Loop se har item access karo
for i in masala_spices:
    print(i)

print("\n")

# Multiple assignment - ek line mein 2 variables set karo
ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# SWAP trick! Bina third variable ke 2 values swap karo
# Python internally temporary tuple banata hai
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")  # ab 1, 2

# Membership testing - kya ye item tuple mein hai?
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")  # True

print("\n")

# XOR swap trick (advanced - rarely use karte hain, upar wala better hai)
a = 10
b = 20
a = a ^ b   # XOR operation - bits level par kaam karta hai
b = a ^ b
a = a ^ b
print(f"a: {a} and b: {b}")  # ab a=20, b=10 - swap ho gaya!
