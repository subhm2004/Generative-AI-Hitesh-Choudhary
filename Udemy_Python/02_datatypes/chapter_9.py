# ============================================================
# FILE: chapter_9.py
# TOPIC: SET - unordered unique collection + set operations
# FOLDER: 02_datatypes
# ============================================================
# Set = duplicate values allowed NAHI, order guaranteed NAHI
# Fast membership check: "item in set" bahut fast hai
# Union, Intersection, Difference - maths wale set operations
# ============================================================

# Sets - unique items ka collection

empty_Set = set()  # khali set ({} mat use karna - wo dict banega!)
print(type(empty_Set))  # <class 'set'>

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}  # ginger dono mein hai

# UNION (|) = dono sets ki SAARI unique items mila do
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# INTERSECTION (&) = sirf wo items jo DONO sets mein hain
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")  # {'ginger'} - sirf common

# DIFFERENCE (-) = pehle set mein hai, doosre mein NAHI
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

# Membership check - kya item set mein hai?
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")  # True
