# ============================================================
# FILE: chapter_5.py
# TOPIC: FLOAT problems + Decimal module (accuracy ke liye)
# FOLDER: 02_datatypes
# ============================================================
# Float = decimal numbers, lekin computer mein exact nahi hote!
# 0.1 + 0.2 != 0.3 kabhi kabhi - isliye Decimal use karte hain
# jab paise, temperature jaise exact values chahiye hon
# ============================================================

import sys
from fractions import Fraction   # fractions ke liye (optional yahan)
from decimal import Decimal as deci  # exact decimal math ke liye

ideal_temp = 95.5
current_temp = 95.49999999999999  # computer ki float galti dikha raha hai

print("\n")
print(f"Ideal temp { ideal_temp }")
print("\n")
print(f"Current temp { current_temp }")
print("\n")

# Float subtraction mein chhoti si galti aa sakti hai!
print(f"Difference temp { ideal_temp - current_temp }")
print("\n")

# sys.float_info = float ki limits dikhata hai (kitna bada/chhota number)
print(sys.float_info)  # package/module hai ye - Python ki built-in info
print("\n")

# Decimal use karo jab exact result chahiye (paise, science, etc.)
print(deci(175) / deci(18))  # 175/18 exact decimal mein
