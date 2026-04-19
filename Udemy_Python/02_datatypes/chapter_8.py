#  List in python (Mutable hote hai list lekin ordered hote hai)

ingredients = ["water", "milk", "black tea"]
print(f"Ingredients are: {ingredients}")
print(type(ingredients))
print(len(ingredients))

ingredients.append("ginger")
ingredients.append("sugar") # values add kr dega ye list me

print(ingredients.reverse())
print(f"Ingredients are: {ingredients}")
ingredients.remove("water") # values hata dega ye list se

print(f"Ingredients are: {ingredients}")



spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options) # add kr dega sari values spice_options ki chai_ingredients me

print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea") # 2nd idx pr value add kr dega
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop() # last elemt remove krega

print(f"{last_added}")
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5, False]
print(f"Maximum sugar level: {max(sugar_levels)}") # max value dega
print(f"Minimum sugar level: {min(sugar_levels)}") # min value dega
print(sugar_levels.index(False))

# operator overloading

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")