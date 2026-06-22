# ============================================================
# FILE: chapter_10.py
# TOPIC: DICTIONARY (dict) - key-value pairs
# FOLDER: 02_datatypes
# ============================================================
# Dictionary = key: value pairs (jaise real dictionary word: meaning)
# Keys UNIQUE honi chahiye, values kuch bhi ho sakti hain
# MUTABLE hai - add, delete, update kar sakte ho
# Bahut fast lookup by key!
# ============================================================

# Dictionary in python (mutable hai dictionary bhi)

# dict() se ya {} se dictionary banao
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

# Khali dict banao, phir items add karo
chai_recipe = {}
chai_recipe["base"] = "black tea"    # key="base", value="black tea"
chai_recipe["liquid"] = "milk"

# Square brackets se value access karo by KEY
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

# del = key-value pair delete karo
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

# 'key' in dict = kya ye key exist karti hai?
print(f"Is sugar in the order? {'sugar' in chai_order}")  # True

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# .keys() = saari keys ki list
print(f"Order details (keys): {chai_order.keys()}")
# .values() = saari values ki list
print(f"Order details (values): {chai_order.values()}")
# .items() = (key, value) pairs ki list
print(f"Order details (items): {chai_order.items()}")

# .popitem() = LAST inserted item nikaal ke return karo
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

# .update() = doosri dict ki saari items is mein merge karo
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

# .get(key, default) = safe access - key nahi mili toh default return
customer_note = chai_order.get("size", "NO Note")  # "size" hai toh value, nahi toh "NO Note"
print(f"customer_note is: {customer_note}")

# ----- DICT ITERATION (loop) -----

my_dictionary = {
    "name ": "Shubham",
    "age": 22,
    "height": "5'9"
}
print(my_dictionary)

# .keys() par loop - har key ke liye
for i in my_dictionary.keys():
    # print(i, my_dictionary[i])           # key aur value
    # print(f"{i} : {my_dictionary[i]}")   # formatted
    # print(f"{i} : {my_dictionary.get(i)}")  # safe get
    print(i)

del my_dictionary["age"]  # "age" key delete
print(my_dictionary)

# my_dictionary.clear()  # POORI dict khali kar do - sab delete
print(my_dictionary)

# Do dicts merge karna
my_dictionary_2 = {
    "name_2 ": "hardik",
    "age": 22,
    "height_2": "5'8"
}
my_dictionary.update(my_dictionary_2)  # dict 2 ki items dict 1 mein add
print(my_dictionary)
print("\n")
