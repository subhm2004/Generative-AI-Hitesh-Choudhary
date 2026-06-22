# ============================================================
# FILE: 03_dict_compre.py
# TOPIC: DICTIONARY COMPREHENSION - ek line mein naya dict banana
# FOLDER: 07_comprehensions
# ============================================================
# Dict Comprehension = shortcut se naya dictionary banana
# Syntax: {key: value for item in iterable}
# Dictionary = key-value pairs store karta hai (jaise real dictionary mein word: meaning)
# .items() = dict ki har key AUR value dono ek saath deta hai (tuple ki tarah)
# ============================================================

# tea_prices_inr = dictionary jisme chai ka naam (key) aur price in INR (value)
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

# Dict comprehension se INR prices ko USD mein convert karo
# {tea: price / 80 for tea, price in tea_prices_inr.items()} ka matlab:
#   tea_prices_inr.items() = har pair ko (key, value) ke roop mein do
#   tea = key (chai ka naam), price = value (INR mein price)
#   price / 80 = INR ko USD mein convert (80 INR = 1 USD assume kiya)
#   Naya dict banega same keys ke saath, values USD mein hongi
tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
