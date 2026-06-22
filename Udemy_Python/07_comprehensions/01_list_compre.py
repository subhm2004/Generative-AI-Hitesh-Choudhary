# ============================================================
# FILE: 01_list_compre.py
# TOPIC: LIST COMPREHENSION - ek line mein nayi list banana
# FOLDER: 07_comprehensions
# ============================================================
# List Comprehension = shortcut jo for loop + append ki jagah use hota hai
# Syntax: [expression for item in list if condition]
#   - expression = har item ke liye kya banana hai
#   - for item in list = loop chalao
#   - if condition = optional filter (sirf matching items lo)
# Result hamesha LIST [] hoti hai
# ============================================================

# menu = ek list jisme chai ke naam stored hain (strings)
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

# List comprehension se sirf "Iced" wali teas filter karo
# [my_tea for my_tea in menu if "Iced" in my_tea] ka matlab:
#   menu ki har tea ko check karo
#   agar "Iced" us tea ke naam mein hai to list mein daal do
# "in" operator = check karta hai ki substring string ke andar hai ya nahi
# Ye normal for loop likhne se zyada clean aur fast hai
iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

# iced_tea ab nayi list hai: ["Iced Lemon Tea", "Iced Peach Tea"]
print(iced_tea)
