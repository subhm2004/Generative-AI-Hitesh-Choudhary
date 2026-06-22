# ============================================================
# FILE: delivery_fees_waiver.py
# TOPIC: Simple if-else - order amount par delivery fee
# FOLDER: 03_conditionals
# ============================================================
# Business logic: 150 se zyada order = FREE delivery
# 150 ya kam = 30 rupees delivery charge
# ============================================================

# User se order amount lo (string ko int mein convert)
order_amount = int(input("Enter the order amount: "))

# Agar order 150 se BADA hai toh delivery FREE
if (order_amount > 150):
    delivery_charge = 0
else:
    delivery_charge = 30  # kam order par 30 rupees charge

print(f"Delivery fees is : {delivery_charge}")
