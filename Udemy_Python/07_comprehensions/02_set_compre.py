# ============================================================
# FILE: 02_set_compre.py
# TOPIC: SET COMPREHENSION - unique values ki set banana
# FOLDER: 07_comprehensions
# ============================================================
# Set Comprehension = list comprehension jaisa, par result SET {} hota hai
# Set = unordered collection jisme DUPLICATE values allowed nahi
# Syntax: {expression for item in iterable if condition}
# Nested comprehension = ek comprehension ke andar doosri loop
# ============================================================

# favourite_chais = list hai jisme kuch naam repeat ho rahe hain
favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

# Set comprehension - duplicates automatically hatt jaate hain
# {chai for chai in favourite_chais} ka matlab:
#   har chai ko set mein daalo, repeat wale sirf ek baar aayenge
# Curly braces {} = set (list ke square brackets [] se alag)
unique_chai = {chai for chai in favourite_chais }
print(unique_chai)

# recipes = dictionary (dict) - key: value pairs
# Key = chai ka naam, Value = us chai ke ingredients ki list
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

# NESTED set comprehension - do loops ek line mein
# {spice for ingredients in recipes.values() for spice in ingredients}
# Pehla loop: recipes.values() = saari ingredient lists (values only, keys nahi)
# Doosra loop: har list ke har spice ko set mein daalo
# Result = saare unique spices ek set mein (cardamom, ginger, clove, etc.)
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
