# ============================================================
# FILE: 02_namespace.py
# TOPIC: Namespace aur Class Attributes (class-level data)
# FOLDER: 10_oops
# ============================================================
# NAMESPACE = naam se value ka scope (kahan variable dikhega)
# CLASS ATTRIBUTE = sabhi objects ke liye shared data (class par define)
# INSTANCE ATTRIBUTE = sirf us ek object ka apna data
# ============================================================

# Chai class - isme class-level attribute hai
class Chai:
    origin = "India"  # class attribute - sab objects share karenge

# Class se directly attribute access - Chai.origin class ka hai
print(Chai.origin)  # "India" print hoga

# Runtime par class mein naya attribute add kar sakte hain
Chai.is_hot = True  # ab Chai class par is_hot = True hai
print(Chai.is_hot)  # True

# creating objects from class Chai
# masala ek OBJECT (instance) hai Chai class ka
masala = Chai()  # naya object ban gaya

# Object se class attribute access - pehle class mein dhundta hai
print(f"Masala {masala.origin}")  # "Masala India" - class se mila
print(f"Masala {masala.is_hot}")  # "Masala True" - class se mila

# Instance par attribute set kiya - ye sirf masala object ka hai
# Class attribute ko SHADOW nahi karta class level par, sirf object level par
masala.is_hot = False  # masala ka apna is_hot = False

# Class ka is_hot ab bhi True hai - object change se class change nahi hoti
print("Class: ", Chai.is_hot)  # Class: True
print(f"Masala {masala.is_hot}")  # Masala False - object ka apna value

# Naya instance-only attribute - class mein ye define nahi tha
masala.flavor = "Masala"  # sirf masala object par flavor hai
print(masala.flavor)  # "Masala"
