# ============================================================
# FILE: chapter_2.py
# TOPIC: SET - Mutable data type (value change ho sakti hai)
# FOLDER: 02_datatypes
# ============================================================
# Set = unordered collection, duplicate values allowed NAHI
# MUTABLE = andar ki cheezein add/remove kar sakte ho
# id() same rahega = same object hai, sirf andar ka data badla
# ============================================================

# Mutable ka example hai ye file

# set() = khali set banana (empty set)
# {} se khali dict banta hai, isliye set() use karte hain
spice_mix = set()

print(f"Initial spice mix id: {id(spice_mix)}")  # memory address
print(f"Initial spice mix id: {spice_mix}")       # abhi khali set: set()

# .add() = set mein nayi cheez daalo (duplicate ignore hoga)
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")

# .remove() = set se cheez hatao (nahi mili toh error)
spice_mix.remove("lemon")

print(f"Initial spice mix id: {spice_mix}")   # ab {'Ginger', 'cardamom'}
print(f"After spice mix id: {id(spice_mix)}")  # id SAME hai! Object wahi, data badla
