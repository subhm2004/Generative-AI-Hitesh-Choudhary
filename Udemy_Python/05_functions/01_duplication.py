# ============================================================
# FILE   : 01_duplication.py
# TOPIC  : Functions se code duplication kam karna
# FOLDER : 05_functions
# ============================================================
# Ye file dikhati hai ki jab same kaam baar-baar likhna padta hai,
# toh function bana kar ek jagah likho aur baar-baar call karo.
# Matlab: DRY principle — Don't Repeat Yourself!

# 'def' keyword se function define (banate) hain
# Function ek reusable block hai — ek baar likho, jitni baar chaho chalao
# 'name' aur 'chai_type' yahan PARAMETERS hain (inputs jo function ko milte hain)
def print_order(name, chai_type):
    # f-string se message print hota hai — {name} aur {chai_type} ki jagah actual values aati hain
    # Example: print_order("Aman", "masala") → "Aman orderded masala chai!"
    print(f"{name} orderded {chai_type} chai!")


# Ab function ko CALL karte hain — matlab function ko chalate hain
# Pehla argument "Aman" → name parameter mein jayega
# Doosra argument "masala" → chai_type parameter mein jayega
print_order("Aman", "masala")

# Same function, alag values — code dubara likhne ki zaroorat nahi!
print_order("Hitesh", "Ginger")

# Ek aur call — sirf values badli, function wahi purana
print_order("Jia", "Tulsi")

