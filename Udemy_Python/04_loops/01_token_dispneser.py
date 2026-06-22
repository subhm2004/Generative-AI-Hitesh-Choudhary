# ============================================================
# FILE: 01_token_dispneser.py (token dispenser)
# TOPIC: for loop + range() - numbers ki sequence par loop
# FOLDER: 04_loops
# ============================================================
# for loop = kisi sequence par baar-baar code chalao
# range(start, end) = start se end-1 tak numbers deta hai [start, end)
# ============================================================

n = int(input("Enter a number:"))

# range(1, n+1) = 1 se n tak (n include hoga kyunki n+1 end hai)
for batch in range(1, n+1):
    print(f"Preparing chai for batch #{batch}")

print("\n")
