# ============================================================
# FILE: 08_for_else.py
# TOPIC: for-else - loop poora chala BINA break ke toh else chalega
# FOLDER: 04_loops
# ============================================================
# for-else: else tab chalta hai jab loop NE break NAHI kiya
# Agar break hua = else SKIP
# Staff mein 18+ dhundhna - mila toh break, nahi mila toh else message
# ============================================================

staff = [("Amit", 19), ("Zara", 17), ("Raj", 15)]  # (naam, umar) tuples

for name, age in staff:
    if (age >= 18):
        print(f"{name} is eligible to manage the staff")
        break  # mil gaya eligible - loop band, else NAHI chalega
else:
    # Ye tab chalega jab loop mein break NAHI hua (koi eligible nahi mila)
    print(f"No one is eligible to manage the staff")
