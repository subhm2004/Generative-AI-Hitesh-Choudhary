# ============================================================
# FILE   : 10_return.py
# TOPIC  : return keyword — function se value wapas bhejna
# FOLDER : 05_functions
# ============================================================
# 'return' se function caller ko value deta hai.
# Bina return ke function None return karta hai.
# Multiple values return = tuple ban kar wapas aate hain.

# --- Part 1: Bina return — None milta hai ---
def make_chai():
    # return "Here is your masal chai"  # Agar ye uncomment karo toh string milegi
    print("Here is your masala chai")  # Sirf print — kuch RETURN nahi ho raha

# Function call ka result store karo
return_value = make_chai()  # Screen par message dikhega

print(return_value)  # Output: None — kyunki return nahi tha!

# --- Part 2: pass — khaali function body ---
def idle_chaiwala():
    pass  # Kuch nahi karta — bas placeholder, error nahi aayega

print(idle_chaiwala())  # None print hoga

# --- Part 3: Simple return ---
def sold_cups():
    return 120  # Number 120 wapas bhej do caller ko

total = sold_cups()  # Return value 'total' mein store
print(total)  # Output: 120

# --- Part 4: Early return — if ke andar ---
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"  # Jaldi return — neeche wali lines NAHI chalengi
    return "Chai is ready"  # cups_left > 0 ho toh ye return hoga
    print("chai")  # KABHI nahi chalega — return ke baad code dead hai (unreachable)

print(chai_status(0))  # "Sorry, chai over"
print(chai_status(5))  # "Chai is ready"


# --- Part 5: Multiple values return — tuple ban kar aate hain ---
def chai_report():
    return 100, 20, 10 # sold, remaining (tuple return krega)
    # Python automatically (100, 20, 10) tuple bana deta hai

# Tuple unpacking — teen values alag-alag variables mein
sold, remaining, not_paid = chai_report()
print("Sold: ", sold)           # 100
print("Remaining: ", remaining) # 20
print("Not paid: ", not_paid)   # 10

# Poora tuple ek saath print
print(chai_report())  # (100, 20, 10)
print(type(chai_report()))  # <class 'tuple'> — multiple return = tuple type
