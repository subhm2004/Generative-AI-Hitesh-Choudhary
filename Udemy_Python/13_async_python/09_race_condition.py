# ============================================================
# FILE: 09_race_condition.py
# TOPIC: Race Condition - bina Lock ke galat result
# FOLDER: 13_async_python
# ============================================================
# Race Condition = do threads EK SAATH same variable badal rahe hain
# counter += 1 actually 3 steps hai: READ, ADD, WRITE
# Do threads beech mein interfere kar sakte hain - kuch increments LOST ho jate hain
# Expected: 2 threads x 100000 = 200000
# Actual: 200000 se KAM aayega (random har baar alag!)
# Solution: 08_thread_lock.py dekho - Lock use karo
# ============================================================

import threading

chai_stock = 0  # shared variable - BINA protection ke!

def restock():
    global chai_stock
    for _ in range(100000):
        # YE UNSAFE HAI! Do threads ek saath yahan aa sakte hain
        # Ek thread read kare, doosra bhi read kare, dono write kare = data loss
        chai_stock += 1

# 2 threads, har ek 1 lakh baar increment
threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

# 200000 hona chahiye tha, lekin kam aayega - race condition!
print("Chai stock: ", chai_stock)
