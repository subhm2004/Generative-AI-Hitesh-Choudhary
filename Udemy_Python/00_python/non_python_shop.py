# ============================================================
# FILE: non_python_shop.py
# TOPIC: Python mein CLASS aur OBJECT kya hota hai? (OOP basics)
# ============================================================
# Class = Blueprint / Template (jaise cake ka mould)
# Object = Us blueprint se bani cheez (jaise mould se bana cake)
# Example: Chai class = chai ka design, my_chai = ek actual chai object
# ============================================================


# class = ek naya type banana (apna khud ka data type)
# Chai = class ka naam
class Chai:
    # __init__ = constructor - jab naya object banta hai tab ye chalta hai
    # self = khud ka object (har object apne aap ko self se refer karta hai)
    # sweetness, milk_level = object banate waqt values leni padengi
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness      # kitni meethi chai (1-5 scale)
        self.milk_level = milk_level    # kitna doodh (1-5 scale)

    # sip = chai peene ka method (function jo class ke andar hota hai)
    def sip(self):
        print("Sipping chai")  # screen pe message print hoga

    # add_sugar = cheeni add karne ka method
    # amount = kitni cheeni daalni hai
    def add_sugar(self, amount):
        print("added the sugar")


# Object banana = class se ek real instance create karna
# my_chai = ek Chai object jisme sweetness=3 aur milk_level=2 hai
my_chai = Chai(sweetness=3, milk_level=2)

# Method call = object par function chalana
# my_chai.add_sugar(3) = is chai mein 3 spoon cheeni daalo
my_chai.add_sugar(3)
