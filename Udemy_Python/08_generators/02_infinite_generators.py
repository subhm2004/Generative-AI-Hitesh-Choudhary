# ============================================================
# FILE: 02_infinite_generators.py
# TOPIC: INFINITE GENERATORS - kabhi khatam na hone wale generators
# FOLDER: 08_generators
# ============================================================
# Infinite Generator = while True loop + yield = unlimited values
# Normal list infinite nahi ho sakti (memory full ho jayegi)
# Generator sirf CURRENT value rakhta hai - isliye infinite possible hai
# Har generator call = NAYA independent generator object (alag state)
# '_' variable = jab value ki zaroorat nahi, sirf loop count ke liye
# ============================================================

# infinite_chai = generator jo kabhi band nahi hota
def infinite_chai():
    count = 1  # counter shuru 1 se
    while (True):  # True = hamesha chalta rahega (infinite loop)
        yield f"Refil #{count}"  # current count ki value do, pause
        count += 1  # count badhao (1, 2, 3, 4, ...)

# Har call par NAYA generator banta hai - apna alag count rakhta hai
refill = infinite_chai()   # User 1 ka generator
user2 = infinite_chai()    # User 2 ka generator (alag count se shuru)

# for _ in range(5) = 5 baar loop chalao, _ matlab value ignore karo
# next(refill) = refill generator se agli value lo
for _ in range(5):
    print(next(refill))

print("\nUser 2 \n")

# user2 ka apna alag generator - count phir se 1 se shuru hoga
for _ in range(6):
    print(next(user2))
