# ============================================================
# FILE: 09_walrus.py
# TOPIC: Walrus operator (:=) - assign + use ek saath
# FOLDER: 04_loops
# ============================================================
# := walrus operator = value assign karo AUR usi expression mein use karo
# Python 3.8+ feature - code chhota aur readable ho sakta hai
# ============================================================

# Purana tareeka (commented):
# value = 13
# remainder = value % 5
# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13
# := se remainder calculate karo AUR if mein check ek hi line mein
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")  # 13 % 5 = 3

# ----- Walrus with input validation -----
available_sizes = ["small", "medium", "large"]

# input lo, lower karo, check karo list mein hai - sab ek line!
if (requested_size := input("Enter your chai cup size: ").lower()) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")

# ----- Walrus in while loop -----
flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

# Jab tak galat flavor choose kare, dobara poocho
while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")  # sahi flavor mil gaya
