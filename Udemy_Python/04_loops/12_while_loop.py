# ============================================================
# FILE: 12_while_loop.py
# TOPIC: while loop se multiplication table
# FOLDER: 04_loops
# ============================================================
# while loop = condition check karo, True hai toh chalao, phir dubara check
# i += 1 = har iteration mein i badhao (warna infinite loop!)
# ============================================================

n = int(input("Enter a number:"))

i = 1  # counter shuru 1 se
while (i < 11):  # jab tak i 11 se chhota hai (1 se 10 tak)
    print(f"{n} * {i} = {n * i}")
    i += 1  # i = i + 1 - agla number

print("\n")
