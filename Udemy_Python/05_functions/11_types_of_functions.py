# ============================================================
# FILE   : 11_types_of_functions.py
# TOPIC  : Pure vs Impure functions, Recursion, Lambda functions
# FOLDER : 05_functions
# ============================================================
# Functions ke alag types: PURE (side-effect free), IMPURE (global change),
# RECURSIVE (khud ko call karta hai), LAMBDA (chhota anonymous function).

# --- PURE FUNCTION ---
# Sirf input leke output deta hai — bahar ki koi cheez change NAHI karta
# Same input → hamesha same output (predictable)
def pure_chai(cups):
    return cups * 10  # 3 cups → 30, simple multiplication

total_chai = 0  # Global variable — impure function isko badlega

# --- IMPURE FUNCTION (not recommended) ---
# Global variable ko ANDAR se badalta hai — side effect hai
# Bahar ki state change ho jati hai — debugging mushkil ho sakti hai
def impure_chai(cups):
    global total_chai  # Global variable use/modify karne ke liye
    total_chai += cups  # Global mein cups add kar do


# --- RECURSIVE FUNCTION ---
# Function APNI KO HI call karta hai — base case tak
# Base case: jab n == 0, return kar do — warna infinite loop!
def pour_chai(n):
    print(n)  # Current number print karo
    if n == 0:
        return "All cups poured"  # BASE CASE — yahan ruk jao
    return pour_chai(n-1)  # RECURSION — khud ko n-1 ke saath call karo
    # Example: pour_chai(3) → print 3 → pour_chai(2) → print 2 → pour_chai(1) → print 1 → pour_chai(0) → return

print(pour_chai(3))



# --- LAMBDA FUNCTION ---
# Chhota, ek-line ka anonymous function — bina 'def' aur naam ke
# Syntax: lambda parameters: expression
chai_types = ["light", "kadak", "ginger", "kadak"]

# filter() list se items select karta hai — lambda batata hai kaunsa rakhna hai
# lambda chai: chai!="kadak" → sirf wo items jahan chai "kadak" NAHI hai
strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)  # ["light", "ginger"] — "kadak" hata diye
