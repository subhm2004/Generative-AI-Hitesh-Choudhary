# ============================================================
# FILE: flavors.py
# TOPIC: FUNCTIONS - reusable code blocks jo value return karte hain
# FOLDER: 06_chai_business/recipes
# ============================================================
# Function = ek naam diya hua code block jo baar-baar use ho sakta hai
# 'def' keyword se function banate hain
# 'return' = function se value wapas bhejna (yahan string return ho rahi hai)
# Ye file ek MODULE hai - main.py isse import karke use karta hai
# ============================================================

# elachai_chai naam ka function - koi input nahi leta (empty parentheses)
# Jab call hoga to "Elachai chai is ready" string return karega
def elachai_chai():
    return "Elachai chai is ready"

# ginger_chai naam ka function - same pattern, alag chai flavor
# Har function apna kaam karta hai aur result return karta hai
def ginger_chai():
    return "Ginger chai is ready"
