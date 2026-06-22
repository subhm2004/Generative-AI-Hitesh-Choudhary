# ============================================================
# FILE: 04_gil_multiprocessing.py
# TOPIC: GIL bypass - Multiprocessing se real parallel CPU use
# FOLDER: 12_threads_concurrency
# ============================================================
# Multiprocessing mein har process ka ALAG GIL hota hai
# Isliye 2 processes = 2 CPU cores truly parallel use kar sakte hain
# Same CPU-heavy kaam jo threading mein slow tha, yahan FAST hoga
# Compare karo 03_gil_threading.py se - yahan time ~half hoga!
# ============================================================

from multiprocessing import Process
import time

# Wahi CPU-heavy counting kaam - 100 million iterations
def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

if __name__ == "__main__":
    start = time.time()

    # Do ALAG processes - har ek ka apna Python interpreter + apna GIL
    p1 = Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    # Yahan time threading wale se KAM hoga - real parallel execution!
    print(f"Total time with multi-processing is {end - start:.2f} seconds")
