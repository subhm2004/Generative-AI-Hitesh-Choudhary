# ============================================================
# FILE: chapter_4.py
# TOPIC: BOOLEAN - True/False aur Logical Operators
# FOLDER: 02_datatypes
# ============================================================
# Boolean = sirf 2 values: True (1) ya False (0)
# and, or, not - logic ke operators
# Python mein True/False capital T/F se likhte hain!
# ============================================================

# Boolean (True = 1 aur False = 0 internally)

is_boiling = True   # paani ubal raha hai? Haan!
stri_count = 5      # kitni baar stir kiya

# True ko number mein use karo toh 1 ban jata hai (upcasting)
total_actions = stri_count + is_boiling  # 5 + 1 = 6
print(f"Total actions: {total_actions}")

milk_present = 0  # 0 = falsy value (False jaisa treat hota hai)
# bool() = kisi value ko True/False mein convert karta hai
print(f"Is there milk? {bool(milk_present)}")  # False aayega

water_hot = True   # paani garam hai?
tea_added = True   # chai patti daal di?

# and = DONO True hon toh hi True (sab conditions pass honi chahiye)
can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")       # True
print(f"Can serve chai? {int(can_server)}")  # True ko int mein = 1


# AND operator - table yaad rakho:
print("AND operator examples:")
print(True and True)    # True  - dono sahi
print(True and False)   # False - ek galat
print(False and True)   # False - ek galat
print(False and False)  # False - dono galat

print("\nOR operator examples:")
# OR operator - KOI EK bhi True ho toh True
print(True or True)     # True
print(True or False)    # True  - ek sahi kaafi hai
print(False or True)    # True
print(False or False)   # False - dono galat toh False

print("\nNOT operator examples:")
# NOT operator - ulta kar deta hai (True -> False, False -> True)
print(not True)         # False
print(not False)        # True
