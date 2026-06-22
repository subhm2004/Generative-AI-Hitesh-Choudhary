# ============================================================
# FILE: main.py
# TOPIC: MODULES & IMPORTS - dusre files se code use karna
# FOLDER: 06_chai_business
# ============================================================
# Module = ek .py file jisme functions/classes hoti hain
# Import = doosri file ka code apni file mein use karna
# Is project mein 'recipes' folder ek PACKAGE hai (folder with .py files)
# 'flavors.py' us package ka ek MODULE hai
# ============================================================

# ----- METHOD 1: Poora module import karo (dot notation se use karo) -----
# 'import recipes.flavors' ka matlab:
#   recipes folder ke andar flavors.py file ko load karo
#   Ab hume har cheez ke aage 'recipes.flavors.' likhna padega
import recipes.flavors

# recipes.flavors.ginger_chai() = flavors module ki ginger_chai function ko call karo
# () = function call - function chalega aur return value milegi
print(recipes.flavors.ginger_chai())
print(recipes.flavors.elachai_chai())

# ----- METHOD 2: Package se module import karo (thoda short path) -----
# 'from recipes import flavors' ka matlab:
#   recipes package se sirf flavors module lao
#   Ab sirf 'flavors.' likhna hai, 'recipes.' nahi
from recipes import flavors

print(flavors.ginger_chai())
print(flavors.elachai_chai())

# ----- METHOD 3: Sirf specific functions import karo (sabse short) -----
# 'from recipes.flavors import elachai_chai, ginger_chai' ka matlab:
#   flavors.py se SIRF ye do functions lao
#   Ab seedha function naam likh sakte ho - flavors. ya recipes. ki zaroorat nahi
from recipes.flavors import elachai_chai, ginger_chai

# Ab seedha function call - jaise apna khud ka function ho
print(ginger_chai())
