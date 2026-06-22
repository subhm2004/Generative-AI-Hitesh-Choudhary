# ============================================================
# FILE: 03_gil_threading.py
# TOPIC: GIL (Global Interpreter Lock) + Threading demo
# FOLDER: 12_threads_concurrency
# ============================================================
# GIL = Python ka ek lock jo EK TIME par sirf EK thread ko
# Python bytecode execute karne deta hai
# Matlab: 2 threads CPU-heavy kaam par = speed BADHEGI NAHI!
# Dono threads time SHARE karenge, parallel nahi chalenge
# I/O kaam (network, file) mein GIL release hota hai - wahan threads useful
# ============================================================

import threading
import time

# CPU-heavy kaam - 100 million baar count badhao
# Ye pure Python loop hai - GIL is par lagta hai
def brew_chai():
    # current_thread().name se thread ka naam pata chalta hai
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):  # 10 crore iterations - bahut heavy!
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

# Do threads banao with custom names
thread1 =threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

# Time measure karo - dekho kitna time lagega
start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

# Expectation: ~2x time lagega single thread jitna (GIL ki wajah se)
# Kyunki dono threads EK SAATH CPU use NAHI kar sakte
print(f"total time taken: {end - start:.2f} seconds")
