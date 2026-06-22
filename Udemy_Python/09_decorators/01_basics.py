# ============================================================
# FILE: 01_basics.py
# TOPIC: DECORATORS - function ke upar extra behavior lagana
# FOLDER: 09_decorators
# ============================================================
# Decorator = ek function jo doosre function ko "wrap" karta hai
# @decorator_name = shortcut syntax - function ke upar likho
# functools.wraps = wrapper function ka naam/metadata original se match rakhta hai
# Wrapper pattern: pehle kuch karo -> original function chalao -> baad mein kuch karo
# Decorator function ko MODIFY nahi karta, USKE AROUND extra code lagata hai
# ============================================================

# functools module se wraps import karo
# wraps = decorator jo wrapper function ka __name__ etc. original jaisa rakhta hai
from functools import wraps

# my_decorator = ek decorator function (jo function leta hai, wrapper return karta hai)
def my_decorator(func):
    @wraps(func)  # wrapper ka naam greet jaisa dikhega (warna 'wrapper' dikhta)
    def wrapper():
        print("Before function runs")  # original se PEHLE ye chalega
        func()  # asli function (greet) yahan call hoga
        print("After function runs")   # original ke BAAD ye chalega
    return wrapper  # wrapper function return - ye greet ko replace karega

# @my_decorator = greet function ko my_decorator se wrap karo
# Matlab: greet() call karoge to actually wrapper() chalega
# Wrapper andar greet() ko call karega extra print ke saath
@my_decorator
def greet():
    print("Hello from decorators class from chaicode")

# greet() call = wrapper chalega -> Before print -> greet() -> After print
greet()

# __name__ = function ka asli naam
# @wraps ki wajah se 'greet' dikhega, 'wrapper' nahi
print(greet.__name__)
