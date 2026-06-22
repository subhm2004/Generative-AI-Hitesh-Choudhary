# ============================================================
# FILE: 04_multiple_exception.py
# TOPIC: Multiple except blocks - alag errors alag handle
# FOLDER: 11_exceptions
# ============================================================
# Ek try ke neeche kai except likh sakte ho
# KeyError = galat dictionary key
# TypeError = galat type (jaise string ko number se multiply)
# Python pehla matching except block use karta hai
# ============================================================

def process_order(item, quantity):
    try:
        # menu se item ka price nikalo
        price = {"masala": 20}[item]  # ginger nahi hai to KeyError
        cost = price * quantity         # quantity string ho to TypeError
        print(f"total cost is {cost}")
    except KeyError:
        # item menu mein nahi mila
        print("Sorry that chai is not on menu")
    except TypeError:
        # quantity number nahi thi (jaise "two" string)
        print("Quantity must be in number")

# ginger menu mein nahi - KeyError handle hoga
process_order("ginger", 2)
# masala hai par quantity "two" string hai - TypeError handle hoga
process_order("masala", "two")
