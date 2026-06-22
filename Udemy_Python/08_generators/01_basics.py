# ============================================================
# FILE: 01_basics.py
# TOPIC: GENERATORS - yield se values ek-ek karke dena
# FOLDER: 08_generators
# ============================================================
# Generator = special function jo values EK BAAR MEIN EK deta hai (lazy)
# 'yield' keyword = return jaisa, par function band nahi hota - pause ho jata hai
# next() = generator se agli value maango
# Generator memory efficient hai - poori list memory mein nahi rakhta
# Normal function 'return' karta hai aur khatam, generator 'yield' karke wait karta hai
# ============================================================

# serve_chai = generator function (andar yield hai, isliye generator hai)
# Har yield ek value deta hai aur function wahi ruk jata hai
def serve_chai():
    yield "Cup 1: Masala Chai"   # pehli value - pause
    yield "Cup 2: Ginger Chai"   # doosri value - pause
    yield "Cup 3: Elaichi Chai"  # teesri value - pause

# serve_chai() call karne se generator OBJECT banta hai (list nahi!)
# stall ab ek iterator hai jisse next() se values milengi
stall = serve_chai()

# for loop se bhi generator iterate kar sakte ho (har yield ek iteration)
# for cup in stall:
#     print(cup)

# ----- Normal function vs Generator function ka comparison -----

# Normal function - poori list EK SAATH return karta hai (sab memory mein)
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function (generator function me yield word ka use hota hai)
# yield = ek value do, baaki ke liye baad mein aana
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

# get_chai_gen() se generator object milega
chai = get_chai_gen()

# next(chai) = generator se agli value lo ("Cup 1")
print(next(chai))
# next(chai) = agli value lo ("Cup 2")
print(next(chai))
print("ab aage chalega cup 3 wala")
# next(chai) = teesri aur LAST value ("Cup 3")
print(next(chai))
# print(next(chai)) # gives error - generator khatam ho gaya, StopIteration error aayega
