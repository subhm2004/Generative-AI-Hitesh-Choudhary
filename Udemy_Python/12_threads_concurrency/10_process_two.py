# ============================================================
# FILE: 10_process_two.py
# TOPIC: CPU-heavy task with MULTIPROCESSING (GIL bypass)
# FOLDER: 12_threads_concurrency
# ============================================================
# Same CPU-heavy kaam jo 09_process_one.py mein threads se slow tha
# Yahan multiprocessing se TRULY PARALLEL chalega
# Har process ka apna GIL = dono CPU cores use ho sakte hain
# Time ~half hoga compared to single process!
# ============================================================

from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):  # 100 crore iterations - bahut heavy!
        total += i
    print("DONE ✅")

if __name__ == "__main__":
    start = time.time()
    # 2 alag PROCESSES - har ek alag CPU core par chalega
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken: {time.time() - start:.2f} seconds")
