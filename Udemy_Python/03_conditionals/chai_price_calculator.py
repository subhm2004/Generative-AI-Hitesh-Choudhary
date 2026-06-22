# ============================================================
# FILE: chai_price_calculator.py
# TOPIC: if / elif / else - conditions se decision lena
# FOLDER: 03_conditionals
# ============================================================
# if = agar condition True hai toh ye karo
# elif = agar pehli False, ye condition check karo
# else = kuch bhi match nahi hua toh ye karo (default)
# ============================================================

# User se cup size input lo, .lower() se chhote letters mein convert
# Method chaining: input() -> .lower() ek line mein
cup = input("Choose your cup size (small/medium/large): ").lower()

# Pehli condition check - small cup?
if (cup == "small"):
    print("Price is 10 rupees")
# Pehli False thi, ab medium check karo
elif (cup == "medium"):
    print("Price is 15 rupees")
# medium bhi nahi, large check karo
elif (cup == "large"):
    print("price is 20 rupees")
# Koi bhi match nahi hua - galat input
else:
    print("Unknown cup size")
