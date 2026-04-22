def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

menu_ji = full_menu()
print(next(menu_ji))
print(next(menu_ji))   
print(next(menu_ji))   
print(next(menu_ji))   
# print(next(menu_ji))   # error dega ye

print("\n")


for chai in full_menu():
    print(chai)

print("\n")


#  try catch or try except syntax 

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
stall.close() #cleanup