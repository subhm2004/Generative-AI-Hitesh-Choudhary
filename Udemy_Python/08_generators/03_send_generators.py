# ============================================================
# FILE: 03_send_generators.py
# TOPIC: SEND - generator ko values bhejna (two-way communication)
# FOLDER: 08_generators
# ============================================================
# Normal generator sirf values DETA hai (yield se)
# .send(value) = generator ko value BHEJ sakte ho (two-way communication)
# Pehli baar next() ya send(None) se generator START karna padta hai
# yield bina value ke = generator ko input lene ki jagah deta hai
# Pattern: next() start karo -> send() se values bhejo -> yield wapas value le
# ============================================================

# chai_customer = generator jo customer se order LETA hai
def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield  # pehla yield - yahan se order aayega (abhi None hai)
    while (True):  # har order ke baad dobara ready
        print(f"Preparing: {order}")  # jo order mila us chai ko banao
        order = yield  # agla order yahan aayega (.send() se)

# Generator object banao
stall = chai_customer()

# next(stall) = generator ko START karo (pehle yield tak pahunchao)
# Pehli baar next() zaroori hai - tab tak generator "Welcome" print karega
# aur order = yield par ruk jayega
next(stall) # start the generator

# .send("Masala Chai") = generator ko value BHEJO
# Ye value 'order = yield' mein jaayegi, phir "Preparing: Masala Chai" print hoga
stall.send("Masala Chai")

# Doosra order bhejo - while loop chalega, phir yield par rukega
stall.send("Lemon Chai")
