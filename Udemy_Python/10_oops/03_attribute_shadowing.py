# ============================================================
# FILE: 03_attribute_shadowing.py
# TOPIC: Attribute Shadowing (instance vs class attribute)
# FOLDER: 10_oops
# ============================================================
# SHADOWING = jab object apna attribute banata hai jo class wale
#             naam ka hai - object wala class wale ko "chhupa" deta hai
# del se instance attribute hata sakte hain - phir class wala wapas dikhega
# ============================================================

# Chai class mein do class-level attributes define kiye
class Chai:
    temperature = "hot"   # class attribute - default temperature
    strength = "Strong"   # class attribute - default strength


# cutting naam ka ek object banaya
cutting = Chai()  # instance create

# Pehle class attribute dikhega kyunki object par abhi override nahi hai
print(cutting.temperature)  # "hot" - class se aaya

# Ab object par apna attribute set kiya - SHADOWING ho gayi
cutting.temperature = "Mild"  # instance attribute - class wale ko chhupa diya
cutting.cup = "small"         # naya instance-only attribute

print("After changing ", cutting.temperature)  # "Mild" - object ka apna
print("cup size is  ", cutting.cup)            # "small" - instance attribute
# Class ka temperature ab bhi "hot" hai - object change se class change nahi
print("Direct look into the class ", Chai.temperature)  # "hot" - class unchanged

# Instance attributes delete karo
del cutting.temperature  # object se temperature hata diya
del cutting.cup          # object se cup bhi hata diya

# Ab cutting.temperature phir CLASS se milega (shadowing khatam)
print(cutting.temperature)  # "hot" - wapas class attribute dikhega
# cup sirf instance par tha - delete ke baad error aayega agar access karo
print(cutting.cup)  # AttributeError - cup ab exist nahi karta
