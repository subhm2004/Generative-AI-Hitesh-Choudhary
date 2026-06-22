# ============================================================
# FILE: 05_order_summary.py
# TOPIC: zip() - do lists ko parallel iterate karna
# FOLDER: 04_loops
# ============================================================
# zip(list1, list2) = dono lists ke items ko pair mein jodta hai
# (name1, bill1), (name2, bill2) ... jaise
# ============================================================

names = ["Shubham", "Meera", "Sandeep", "Alina"]
bills = [5_000, 70, 100, 55]

# zip se dono lists ek saath loop - har naam ke saath uska bill
for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
