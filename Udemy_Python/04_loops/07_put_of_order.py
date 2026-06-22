# ============================================================
# FILE: 07_put_of_order.py (out of order)
# TOPIC: continue aur break - loop control statements
# FOLDER: 04_loops
# ============================================================
# continue = current iteration skip karo, agli par jao
# break = loop poora band kar do, bahar nikal jao
# ============================================================

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    # Out of Stock mile toh skip karo, agla flavour check karo
    if (flavour == "Out of Stock"):
        continue  # is iteration ko chhod do, loop continue

    # Discontinued mile toh loop POORA band kar do
    if (flavour == "Discontinued"):
        print(f"{flavour} item found")
        break  # loop yahin khatam - Tulsi tak nahi pahunchega

    print(f"{flavour} item found")

# break se bahar aane ke baad ye line chalegi
print(f"Out side of loop")
