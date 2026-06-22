# ============================================================
# FILE: 04_close_generator.py
# TOPIC: YIELD FROM, CLOSE & TRY-EXCEPT with generators
# FOLDER: 08_generators
# ============================================================
# yield from = doosre generator ki SAARI values delegate karo (shortcut)
# .close() = generator ko force band karo (GeneratorExit exception raise hota hai)
# try/except = errors handle karo gracefully
# for loop generator par automatically next() call karta hai
# ============================================================

# local_chai = local flavors ka chhota generator
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

# imported_chai = imported flavors ka generator
def imported_chai():
    yield "Matcha"
    yield "Oolong"

# full_menu = yield from se do generators ko EK mein jod do
# yield from local_chai() = local_chai ke saare yields yahan se niklenge
# yield from imported_chai() = phir imported ke saare yields
# Matlab: pehle Masala, Ginger, phir Matcha, Oolong - ek sequence mein
def full_menu():
    yield from local_chai()
    yield from imported_chai()

# full_menu() se generator object - 4 values denge total
menu_ji = full_menu()
print(next(menu_ji))  # "Masala Chai"
print(next(menu_ji))  # "Ginger Chai"
print(next(menu_ji))  # "Matcha"
print(next(menu_ji))  # "Oolong"
# print(next(menu_ji))   # error dega ye - 4 values ke baad StopIteration

print("\n")

# for loop generator par - har yield ek iteration
# Har baar full_menu() NAYA generator banata hai (fresh start)
for chai in full_menu():
    print(chai)

print("\n")

# ----- try/except syntax with generators -----

# chai_stall = generator jo orders leta hai aur close hone par message deta hai
def chai_stall():
    try:
        while True:  # infinite loop - orders aate rahenge
            order = yield "Waiting for chai order"  # har baar ye message + order input
    except:  # jab .close() call hoga to GeneratorExit aayega
        print("Stall closed, No more chai")

# Generator start karo
stall = chai_stall()
print(next(stall))  # "Waiting for chai order" milega

# .close() = generator ko band karo - except block chalega
stall.close() #cleanup
