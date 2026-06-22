# ============================================================
# FILE: 04_self_args.py
# TOPIC: self aur Instance Methods (methods jo object par chalte hain)
# FOLDER: 10_oops
# ============================================================
# self = current object ka reference (jo method call hua us instance ko)
# INSTANCE METHOD = class ke andar function jo pehla argument self leta hai
# Python automatically object ko self mein pass karta hai jab cup.describe() call karo
# ============================================================

# Chaicup class - chai cup ka blueprint
class Chaicup:
    size = 150  # ml - class attribute, default cup size

    # self is a reference to the current instance of the class (method hai ye)
    # describe ek INSTANCE METHOD hai - har object apna size use karega
    def describe(self):
        # self.size = is particular object ka size attribute
        return f"A {self.size}ml chai cup"
    

# cup object banaya - Chaicup() se instance create
cup = Chaicup()
# cup.describe() call par Python internally Chaicup.describe(cup) jaisa chalata hai
print(cup.describe())  # "A 150ml chai cup"

print("\nUsing class method without creating an instance:")
# Class se directly bhi call kar sakte ho - lekin self (instance) manually pass karna padta hai
print(Chaicup.describe(cup))  # class method ko call karne ke liye instance pass karna padta hai, self ke through access hota hai

print("\nCreating another instance of Chaicup:")
# Dusra alag object - apna alag data rakh sakta hai
cup_two = Chaicup()       # naya instance
cup_two.size = 100        # sirf cup_two ka size change - cup par asar nahi
print(Chaicup.describe(cup_two))  # "A 100ml chai cup" - cup_two ka size use hua
