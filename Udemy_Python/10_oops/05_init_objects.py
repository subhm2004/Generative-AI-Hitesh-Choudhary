# ============================================================
# FILE: 05_init_objects.py
# TOPIC: __init__ Constructor aur Object Initialization
# FOLDER: 10_oops
# ============================================================
# __init__ = CONSTRUCTOR method - object banate hi automatically call hota hai
# self = naya banne wala object
# Isme attributes set karte hain taaki har object apna data rakhe
# ============================================================

class ChaiOrder:
    
    # constructor method, it is called when we create an instance of the class
    # __init__ = magic/dunder method - ChaiOrder(...) likhte hi ye chalega
    def __init__(self, type_, size):
        # self.type = is object ka chai type store karo
        self.type = type_    # instance attribute - masala, ginger, etc.
        # self.size = is object ka size (ml mein) store karo
        self.size = size     # instance attribute - 200, 220, etc.

    # summary ek instance method hai - object ke data se string banata hai
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
# Object banate waqt __init__ ko arguments pass hote hain
order = ChaiOrder("Masala", 200)  # type_="Masala", size=200
print(order.summary())  # "200ml of Masala chai"

print("\nCreating another order:")
# Har naya object alag __init__ call karta hai - alag data
order_two = ChaiOrder("Ginger", 220)  # dusra order - alag type aur size
print(order_two.summary())  # "220ml of Ginger chai"
