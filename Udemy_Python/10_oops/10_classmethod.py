# ============================================================
# FILE: 10_classmethod.py
# TOPIC: @classmethod - cls parameter aur alternative constructors
# FOLDER: 10_oops
# ============================================================
# CLASS METHOD = pehla argument cls (class khud) hota hai, self nahi
# @classmethod se object banane ke alag tareeke bana sakte ho (factory methods)
# cls(...) = usi class ka naya object banata hai
# ============================================================

class ChaiOrder:
    # Normal constructor - direct arguments se object banata hai
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type      # masala, ginger, etc.
        self.sweetness = sweetness    # low, medium, high
        self.size = size              # Small, Medium, Large

    # @classmethod - dictionary se order banane ka alternate constructor
    @classmethod
    def from_dict(cls, order_data):
        # cls = ChaiOrder class khud - isse naya object banayenge
        return cls(
            order_data["tea_type"],   # dict se tea_type nikala
            order_data["sweetness"],  # dict se sweetness
            order_data["size"],       # dict se size
        )
    
    # @classmethod - string se order banane ka alternate constructor
    @classmethod
    def from_string(cls, order_string):
        # "Ginger-Low-Small" ko split karke teen parts
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)  # cls(...) = ChaiOrder(...) jaisa
    
class ChaiUtils:
    # staticmethod - validation helper, cls/self ki zaroorat nahi
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]  # True agar valid size


# Static method - class se directly call
print(ChaiUtils.is_valid_size("Medium"))  # True - Medium valid size hai

# Class method se object - dictionary se
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})

# Class method se object - string se
order2 = ChaiOrder.from_string("Ginger-Low-Small")

# Normal __init__ se object - direct arguments
order3 = ChaiOrder("Large", "Low", "Large")

# __dict__ se object ke saare attributes dictionary mein dikhte hain
print(order1.__dict__)  # order1 ke attributes
print(order2.__dict__)  # order2 ke attributes
print(order3.__dict__)  # order3 ke attributes
