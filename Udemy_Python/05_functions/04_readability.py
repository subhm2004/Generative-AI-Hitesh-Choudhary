# ============================================================
# FILE   : 04_readability.py
# TOPIC  : Functions se code padhna aur samajhna aasaan hota hai
# FOLDER : 05_functions
# ============================================================
# Function ka naam hi bata deta hai ki kya ho raha hai.
# calculate_bill(3, 15) padh kar turant samajh aa jata hai — 3 cups, 15 rupaye each.

# 'cups' aur 'price_per_cup' parameters hain — function ko ye values chahiye
# 'return' keyword se function ek VALUE wapas bhejta hai caller ko
def calculate_bill(cups, price_per_cup):
    # cups × price_per_cup = total bill — ye result return hoga
    return cups * price_per_cup


# Function call karo aur result 'my_bill' variable mein store karo
# 3 cups × 15 = 45
my_bill = calculate_bill(3, 15)
print(my_bill)  # Output: 45

# Function ko seedha print() ke andar bhi use kar sakte ho — return value print hogi
# Table 2 ka order: 2 cups × 50 = 100
print("Order for table 2: ", calculate_bill(2, 50))
