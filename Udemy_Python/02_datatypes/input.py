# ============================================================
# FILE: input.py
# TOPIC: User se input lena (input function)
# FOLDER: 02_datatypes
# ============================================================
# input() = user se keyboard se value maangta hai
# HAMESHA string return karta hai - number chahiye toh int() use karo
# Program run karo toh terminal mein type karna padega!
# ============================================================

# User se 3 numbers input lo (string aayega, int() se number banao)
a = int(input("Enter first number: "))   # pehla number
b = int(input("Enter second number: "))   # doosra number
c = int(input("Enter third number: "))    # teesra number

# Teenon ka sum nikalo
sum = a + b + c
print(f"sum of 3 number is : {sum}")
