# ============================================================
# FILE: 02_batch_chai.py
# TOPIC: for loop basics (same as 01 - practice file)
# FOLDER: 04_loops
# ============================================================

n = int(input("Enter a number:"))

# Har batch ke liye chai prepare karo - 1 se n tak
for batch in range(1, n+1):
    print(f"Preparing chai for batch #{batch}")
