# Mutualble ka example hai 

spice_mix = set() # empty set

print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")

spice_mix.remove("lemon")

print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")