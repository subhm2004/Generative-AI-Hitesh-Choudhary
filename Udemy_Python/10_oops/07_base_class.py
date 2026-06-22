# ============================================================
# FILE: 07_base_class.py
# TOPIC: Base Class Constructor aur super() ka use
# FOLDER: 10_oops
# ============================================================
# Child class ka __init__ parent ka __init__ call karna chahiye
# super().__init__() = recommended tareeka parent constructor call karne ka
# Bina super() ke parent ki initialization miss ho sakti hai
# ============================================================

# Parent/Base class - basic Chai blueprint
class Chai:
    def __init__(self, type_, strength):
        # object banate hi type aur strength set ho jayenge
        self.type = type_          # chai ka type
        self.strength = strength   # kitni strong hai

#  In the above implementation, we have a base class `Chai` with an `__init__` method that initializes the `type` and `strength` attributes.

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        
# In the above implementation, we are not calling the base class constructor, which means that if there is any initialization logic in the base class, it will not be executed. This can lead to issues if the base class has important setup code.

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

# Using super() is the recommended way to call the base class constructor, as it is more maintainable and works well with multiple inheritance.
# GingerChai = Chai se inherit karti hai (child class)
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # super() parent class (Chai) ka __init__ call karta hai
        # pehle parent ki initialization, phir child ki extra cheezein
        super().__init__(type_, strength)  # parent constructor - type_ aur strength set
        self.spice_level = spice_level   # child class ka extra attribute
