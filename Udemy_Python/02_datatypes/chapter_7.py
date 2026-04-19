# Tuples (Tuples are immutable)

masala_spices = ("cardamom", "cloves", "cinnamon")

print(type(masala_spices))
print(f"Masala spices: {masala_spices}")
print(len(masala_spices))

print("\n")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

print("\n")

# Loop laga kr access kr skte hai 
for i in masala_spices:
    print(i)

print("\n")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# values swap krke dikha di h 
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# membership testing

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}") # boolean answer aayega

print("\n")

# now lets swap 2 variables without third variable

a = 10 
b = 20 

a = a^b
b = a^b
a = a^b
print(f"a: {a} and b: {b}")