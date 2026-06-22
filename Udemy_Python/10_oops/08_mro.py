# ============================================================
# FILE: 08_mro.py
# TOPIC: MRO - Method Resolution Order (multiple inheritance mein order)
# FOLDER: 10_oops
# ============================================================
# MULTIPLE INHERITANCE = ek class do ya zyada parents se inherit kare
# MRO = Python decide karta hai method/attribute kis class se lena hai
# __mro__ ya mro() se pura resolution order dekh sakte ho
# Rule: left-to-right, depth-first (C3 linearization)
# ============================================================

# Base class A - sabse upar wala parent
class A:
    label = "A: Base class"  # class attribute

# B inherits from A - B is child of A
class B(A):
    label = "B: Masala blend"  # B ne A ke label ko override kiya

# C bhi A se inherit karti hai - A ka dusra child
class C(A):
    label = "C: Herbal blend"  # C ka apna label

# D multiple inheritance - C aur B dono se inherit (order matter karta hai!)
# class D(C, B) matlab pehle C check, phir B, phir A
class D(C, B):
    pass  # apna kuch nahi - parents se sab lega

# D ka object banaya
cup = D()  # instance of D
# label dhundte waqt MRO follow hoga - D mein nahi mila to C mein, phir B, phir A
print(cup.label)  # "C: Herbal blend" - C pehle MRO mein hai isliye C ka label
# Poora MRO order print karo - kaunsi class pehle search hogi
print(D.__mro__)  # (<class 'D'>, <class 'C'>, <class 'B'>, <class 'A'>, <class 'object'>)
