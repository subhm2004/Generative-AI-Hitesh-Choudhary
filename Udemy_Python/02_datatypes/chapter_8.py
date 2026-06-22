# ============================================================
# FILE: chapter_8.py
# TOPIC: LIST - mutable ordered collection + list methods
# FOLDER: 02_datatypes
# ============================================================
# List = ordered collection jo CHANGE ho sakti hai (mutable)
# Syntax: [item1, item2, ...] - square brackets
# Bahut saare useful methods: append, remove, pop, sort, etc.
# ============================================================

# List in python (Mutable hote hai, ordered bhi hote hai)

ingredients = ["water", "milk", "black tea"]  # chai ke ingredients
print(f"Ingredients are: {ingredients}")
print(type(ingredients))  # <class 'list'>
print(len(ingredients))   # 3 items

# .append() = list ke END mein nayi cheez add karo
ingredients.append("ginger")
ingredients.append("sugar")

# .reverse() = list ko ulta kar do (NOTE: None return karta hai, list khud badalti hai)
print(ingredients.reverse())  # None print hoga - list andar se reverse hui
print(f"Ingredients are: {ingredients}")

# .remove() = pehli baar mili value hata do
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

# ----- AUR LIST METHODS -----

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# .extend() = doosri list ki SAARI items is list mein add karo
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

# .insert(index, value) = specific position par value daalo
chai_ingredients.insert(2, "black tea")  # index 2 par "black tea"
print(f"chai: {chai_ingredients}")

# .pop() = LAST item nikaal ke return karo (list se hat jayega)
last_added = chai_ingredients.pop()
print(f"{last_added}")  # jo item nikala
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()  # ulta karo
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()  # alphabetically sort karo
print(f"chai: {chai_ingredients}")

# max() aur min() - sabse badi/chhoti value
sugar_levels = [1, 2, 3, 4, 5, False]  # False = 0 treat hota hai
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")
print(sugar_levels.index(False))  # False kis index par hai?

# ----- OPERATOR OVERLOADING (lists ke saath + aur *) -----

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# + operator = do lists jod do (concatenate)
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

# * operator = list ko repeat karo
strong_brew = ["black tea", "water"] * 3  # 3 baar repeat
print(f"String brew: {strong_brew}")

# bytearray = mutable bytes (binary data jo change ho sakti hai)
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")  # bytes replace
print(f"Bytes: {raw_spice_data}")
