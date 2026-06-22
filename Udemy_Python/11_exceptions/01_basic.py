# ============================================================
# FILE: 01_basic.py
# TOPIC: Exception kya hai - bina handle kiye program crash
# FOLDER: 11_exceptions
# ============================================================
# EXCEPTION = error jo program chalate waqt aati hai (runtime error)
# IndexError = list mein jo index nahi hai us par access karne par
# Bina try/except ke Python program ruk jata hai (crash)
# ============================================================

# orders ek list hai - index 0 aur 1 par values hain
orders = ["masala", "ginger"]  # sirf 2 items - index 0, 1 valid hain

# Index 2 exist nahi karta - IndexError aayega aur program crash
print(orders[2])  # ERROR! list mein sirf index 0,1 hain - 2 invalid hai
