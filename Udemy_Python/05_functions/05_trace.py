# ============================================================
# FILE   : 05_trace.py
# TOPIC  : Function ko loop ke saath use karna (tracing/debugging)
# FOLDER : 05_functions
# ============================================================
# Functions ko lists aur loops ke saath mila kar kaam aasaan ho jata hai.
# Har item par same calculation — function ek baar likho, loop mein call karo.

# 'price' aur 'vat_rate' parameters — VAT (tax) calculate karne ke liye
# Formula: price × (100 + vat_rate) / 100
# Example: price=100, vat_rate=10 → 100 × 110/100 = 110
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


# Ek list hai jisme alag-alag order ki prices hain
orders = [100, 150, 200]

# Total VAT track karne ke liye variable — shuru mein 0
total_vat = 0

# Har price ke liye loop chalega — 'price' variable har baar list ki next value lega
for price in orders:
    # Function call — VAT ke saath final amount milega
    final_amount = add_vat(price, 10)  # 10% VAT lag raha hai

    # Sirf VAT ka hissa nikalo: final - original = kitna extra tax laga
    total_vat += final_amount - price  # += matlab pehle wali value mein add karo

    # Har order ka detail print karo
    print(f"Original: {price}, Final with VAT: {final_amount}")

# Sab orders ke baad total VAT dikhao
print(f"Total VAT: {total_vat}")
