# ============================================================
# FILE: 04_tea_menu.py
# TOPIC: enumerate() - index + value dono ek saath loop mein
# FOLDER: 04_loops
# ============================================================
# enumerate(list) = (index, item) pairs deta hai
# start=1 se indexing 1 se shuru (default 0 se hoti hai)
# Menu numbering jaisa use case!
# ============================================================

menu = ["Green", "Lemon", "Spiced", "Mint"]

# enumerate = index aur item dono ek saath - menu number chahiye ho toh
for idx, item in enumerate(menu):  # indexing 0 se start hogi
    print(f"{idx} : {item} chai")

print("\n")

# start=1 = customer-friendly numbering (1, 2, 3... not 0, 1, 2)
for index, item in enumerate(menu, start=1):
    print(f"{index} : {item} ")

print("\n")
