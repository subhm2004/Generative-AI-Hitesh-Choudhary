# ============================================================
# FILE   : 09_input_params.py
# TOPIC  : Function parameters — immutable vs mutable, positional, keyword, *args, **kwargs
# FOLDER : 05_functions
# ============================================================
# Parameters ke alag-alag tarike hain values pass karne ke.
# Immutable (string) vs Mutable (list) — function mein change ka effect alag hota hai.

# --- Part 1: Immutable parameter (string) ---
chai = "Ginger chai"  # String IMMUTABLE hai — change nahi ho sakti andar se

def prepare_chai(order):
    # Sirf print karta hai — 'order' ek COPY/reference hai, original string safe hai
    print("Preparing ", order)


prepare_chai(chai)  # chai ki value 'order' parameter mein gayi
print(chai)  # Ab bhi "Ginger chai" — string change nahi hui

print("\n")  # Khali line

# --- Part 2: Mutable parameter (list) ---
chai = [1, 2, 3]  # List MUTABLE hai — andar se change ho sakti hai

def edit_chai(cup):
    cup[1] = 42 # update index 1 — list ka doosra element 42 ho jayega
    # 'cup' aur 'chai' SAME list ko point karte hain — dono jagah change dikhega!

edit_chai(chai)  # List pass ki — andar index 1 change hua
print(chai)  # Output: [1, 42, 3] — bahar bhi change dikha!

print("\n")

# --- Part 3: Positional aur Keyword arguments ---
# Teen parameters: tea, milk, sugar — order matter karta hai positional mein
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# POSITIONAL arguments — order se match hote hain: pehla=tea, doosra=milk, teesra=sugar
make_chai("Darjeeling", "Yes", "Low") #positional

# KEYWORD arguments — naam se pass karo, order matter nahi karta
make_chai(tea="Green", sugar="Medium", milk="No") #keywords

print("\n")

# --- Part 4: *args aur **kwargs ---
# *args = kitni bhi POSITIONAL values (tuple ban kar aati hain)
# **kwargs = kitni bhi KEYWORD values (dictionary ban kar aati hain)
def special_chai(*args, **kwargs):
    print("Ingredients", args)   # Tuple: ("Cinnamon", "Cardmom")
    print("Extras", kwargs)      # Dict: {"sweetener": "Honey", "foam": "yes"}
# tuples and dictionary
special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")

# --- Part 5: Default mutable argument ka trap (commented out) ---
# GALAT tarika — [] default EK BAAR banta hai, har call mein SAME list use hoti hai!
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# SAHI tarika — None use karo, har baar nayi list banao
def chai_order(order=None):
    if order is None:
        order = []  # Har call par NAYI khali list — pehli wali safe
    print(order)

chai_order()  # Khali list print
chai_order()  # Phir se khali — pehli call ki list affect nahi karti
