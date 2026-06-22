# ============================================================
# FILE: 01_simple_class.py
# TOPIC: Simple Class - OOP ki shuruaat (class aur object)
# FOLDER: 10_oops
# ============================================================
# CLASS = blueprint/template jisse OBJECTS banate hain
# OBJECT = class ka ek real instance (jaise ek specific cup of chai)
# type() se pata chalta hai koi cheez class hai ya object
# ============================================================

# Chai naam ki ek CLASS define kar rahe hain
# 'class' keyword se naya blueprint banate hain
# 'pass' matlab abhi is class mein kuch nahi hai - khali class
class Chai:
    pass  # placeholder - body empty hai abhi

# Ek aur class - ChaiTime (alag blueprint hai)
class ChaiTime:
    pass  # ye bhi abhi empty class hai

# Chai class ka TYPE check karo
# type(Chai) = <class 'type'> kyunki Python mein class bhi ek object hai!
print(type(Chai))  # class hai lekin internally ye ek object hai

# Chai() se OBJECT (instance) banaya - ginger_tea naam ka
# () lagane se class call hoti hai aur naya object milta hai
ginger_tea = Chai()  # object of Chai class

# ginger_tea ka type dekho - ye Chai class ka instance hai
print(type(ginger_tea))  # <class '__main__.Chai'> aayega

# kya ginger_tea exactly Chai class ka object hai?
# 'is' se identity check hoti hai - True matlab same class ka instance
print(type(ginger_tea) is Chai)  # True - ye Chai class ka object hai

# kya ginger_tea ChaiTime class ka hai? - False, alag class hai
print(type(ginger_tea) is ChaiTime)  # False - ChaiTime alag class hai
