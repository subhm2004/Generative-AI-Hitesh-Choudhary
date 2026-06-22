# ============================================================
# FILE: 10_dictionary_case.py
# TOPIC: Loop on list of dicts + dict lookup for discounts
# FOLDER: 04_loops
# ============================================================
# List of dictionaries = har user ek dict hai
# discounts dict se coupon code se discount rules nikalo
# .get(key, default) = key nahi mili toh (0, 0) use karo
# ============================================================

# List of dictionary - har user ki info alag dict mein
users = [
    {"id": 1, "total": 100, "coupon": "P20"},   # P20 = 20% percent off
    {"id": 2, "total": 150, "coupon": "F10"},   # F10 = 50% (example)
    {"id": 3, "total": 80, "coupon": "P50"},    # P50 = flat 10 rupees
]

# Coupon code -> (percent_discount, fixed_discount)
discounts = {
    "P20": (0.2, 0),    # 20% off, 0 fixed
    "F10": (0.5, 0),    # 50% off
    "P50": (0, 10),     # 0%, 10 rupees flat
}

for user in users:
    # user["coupon"] se discount rules nikalo, nahi mila toh (0, 0)
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    # Total ka percent + fixed amount = total discount
    discount = user["total"] * percent + fixed
    print(f"user_id {user['id']} paid {user['total']} and got discount for next visit of rupees {discount}")
