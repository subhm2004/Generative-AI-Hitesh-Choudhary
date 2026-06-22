# ============================================================
# FILE: 11_table_of_a_number.py
# TOPIC: range() ke advanced uses - reverse, step
# FOLDER: 04_loops
# ============================================================
# range(start, end, step) - step = har kitne number jump
# step negative = reverse counting (ulta)
# NOTE: Loop [start, end) tak chalta hai - end include NAHI hota
# ============================================================

n = int(input("Enter a number:"))
# Normal table: 1 se 10 tak multiply
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("\n")

# ----- REVERSE table (10 se 1 tak) -----
m = int(input("Enter a number:"))
# range(10, 0, -1) = 10, 9, 8, ... 1 (step -1 = peeche jao)
for i in range(10, 0, -1):
    print(f"{m} x {i} = {m * i}")

print("\n")

# ----- Countdown from num to 1 -----
num = int(input("Enter a number:"))
for i in range(num, 0, -1):
    print(i)  # num, num-1, ... 2, 1

print("\n")

# ----- Skip numbers (step 2) -----
# range(1, 10, 2) = 1, 3, 5, 7, 9 - sirf odd numbers
for i in range(1, 10, 2):
    print(i)
