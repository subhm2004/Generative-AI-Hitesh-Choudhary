# ============================================================
# FILE: snak_suggestion.py (snack suggestion)
# TOPIC: or operator - multiple conditions mein se koi ek True
# FOLDER: 03_conditionals
# ============================================================
# or = agar KOI BHI condition True hai toh poora True
# snack cookies YA samosa ho toh serve karo
# ============================================================

snack = input("Enter your preferred snack: ").lower()

# or operator - cookies YA samosa dono mein se koi bhi ho toh OK
if (snack == "cookies" or snack == "samosa"):
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")
