# ============================================================
# FILE: 09_process_one.py
# TOPIC: CPU-heavy task with THREADS (GIL problem demo)
# FOLDER: 12_threads_concurrency
# ============================================================
# Ye file dikhati hai ki CPU-heavy kaam mein threads HELP NAHI karte
# GIL ki wajah se dono threads time share karenge, parallel nahi chalenge
# Compare karo 10_process_two.py se - wahan multiprocessing use hoga
# ============================================================

import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**7):  # 1 crore iterations - CPU intensive
        total += i
    print("DONE ✅")

start = time.time()
# 2 threads same CPU-heavy kaam - GIL se parallel nahi honge
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

# Time lagbhag 2x hoga jaise ek thread chala ho
print(f"Time taken: {time.time() - start:.2f} seconds")
