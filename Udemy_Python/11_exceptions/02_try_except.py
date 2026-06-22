# ============================================================
# FILE: 02_try_except.py
# TOPIC: try aur except - error ko pakad kar handle karna
# FOLDER: 11_exceptions
# ============================================================
# try = risky code yahan likho jo error de sakta hai
# except = agar error aayi to ye block chalega, program crash nahi hoga
# except KeyError = sirf KeyError pakdega (dict mein key nahi mili)
# ============================================================

# Dictionary - chai flavor aur uska price
chai_menu = {"masala": 30, "ginger": 40}

# try block - yahan error ho sakti hai
try:
    # "elaichi" key menu mein nahi hai - KeyError aayegi
    chai_menu["elaichi"]  # invalid key access
except KeyError:
    # KeyError aayi to ye message print - program crash nahi hua
    print("The key that you are tying to access does not exists")


# except ne error handle kar li - program aage chalta rahega
print("Hello chai code")  # ye line zaroor chalegi - crash nahi hua
