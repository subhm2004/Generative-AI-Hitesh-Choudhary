# ============================================================
# FILE: 03_tea_orders.py
# TOPIC: for loop on LIST - har item par iterate karna
# FOLDER: 04_loops
# ============================================================
# List par loop = har element ek-ek karke process karo
# Variable name (name, item) mein current element aata hai
# ============================================================

# loops on list
orders = ["Shubham", "Aman", "Becky", "Carlos"]

# Har customer ke naam par loop - name mein current naam aayega
for name in orders:
    print(f"Order ready for {name}")

print("\n")

# Mixed type list - numbers aur strings dono
food = [1, 2, 3, 4, "Shubham", "Aman", "Becky"]

for item in food:
    print(item)  # har item print - type matter nahi karta

print("\n")
