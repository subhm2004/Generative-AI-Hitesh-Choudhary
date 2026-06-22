# ============================================================
# FILE: chapter_1.py
# TOPIC: Variables, Memory (id), aur IMMUTABILITY
# FOLDER: 02_datatypes
# ============================================================
# Variable = ek naam jisse value yaad rakhte hain (jaise dabba ka label)
# Immutable = value change NAHI ho sakti, sirf naya reference ban sakta hai
# Integer (int) Python mein IMMUTABLE hai
# ============================================================

# sugar_amount naam ka variable banaya, value = 2
sugar_amount = 2
# f-string = string ke andar variable ki value daal sakte ho {variable}
print(f"Initial sugar: {sugar_amount}")

# Ab sugar_amount ko 12 assign kiya - PURANI value 2 change nahi hui!
# Python ne nayi value 12 ko point kiya, purani 2 memory mein ab bhi hai
sugar_amount = 12  # ek naya reference bana hai (naya pointer)
print(f"Second Initial sugar: {sugar_amount}")

# id() = memory mein object ka unique address number deta hai
# Har value ka apna id hota hai - same value = same id (usually)
print(f"ID of 2: {id(2)}")    # number 2 ka memory address
print(f"ID of 12: {id(12)}")  # number 12 ka memory address - alag hoga

# IMPORTANT CONCEPT:
# Hum is code mein reference change kar rahe hain, value change nahi!
# Integer IMMUTABLE hai - 2 ko 12 mein convert nahi kar sakte
# Sirf variable ko nayi value ki taraf point kar sakte hain

# The numbers are immutable we cannot change them only the reference can be changed not the values
