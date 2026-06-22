# ============================================================
# FILE: non_python_code.py
# TOPIC: Python mein FUNCTION kya hota hai? (Pseudo-code / Fake code)
# ============================================================
# Ye file ACTUAL Python code NAHI hai - ye sirf dikhane ke liye hai
# ki real life mein kaam ko chhote-chhote steps mein kaise todte hain.
# Jaise chai banane ka process - har step ek alag kaam hai.
# Python mein in steps ko "functions" kehte hain.
# ============================================================


# def = define karna, matlab ek function (kaam karne wala block) banana
# make_chai = function ka naam - ye poori chai banane ka kaam karega
def make_chai():
    # if not = agar NAHI hai toh (condition check)
    # kettle_has_water() = ye function check karega kettle mein paani hai ya nahi
    if not kettle_has_water():
        fill_kettle()  # paani nahi hai toh kettle bharo

    plug_in_kettle()   # kettle ko plug mein lagao (bijli connect karo)
    boil_water()       # paani ubalo

    # cup saaf nahi hai toh dho lo
    if not is_cup_clean():
        wash_cup()

    add_to_cup("tea_leaves")  # cup mein chai patti daalo
    add_to_cup("sugar")       # cup mein cheeni daalo
    pour("boiled water")      # ubla hua paani daalo
    stie("cup")               # cup ko hilao/mix karo (stir ka typo hai yahan)
    serve("chai")             # chai serve karo customer ko


# Function ko CALL karna = use chalana / run karna
# Sirf likhne se kaam nahi hota - call karna padta hai!
make_chai()
