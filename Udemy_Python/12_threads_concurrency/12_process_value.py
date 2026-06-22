# ============================================================
# FILE: 12_process_value.py
# TOPIC: Multiprocessing Value - shared counter across processes
# FOLDER: 12_threads_concurrency
# ============================================================
# Value = processes ke beech EK shared variable share karne ka tarika
# Value('i', 0) = integer type shared value, starting value 0
# .get_lock() = Value ke saath built-in lock milta hai - race condition se bachao
# Normal variable processes mein share NAHI hota - Value use karna padta hai
# ============================================================

from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        # counter.get_lock() = shared value par lock lagao
        # Bina lock ke multiple processes galat count karenge
        with counter.get_lock():
            counter.value += 1  # .value se actual number access karo


if __name__ == "__main__":
    # 'i' = integer type, 0 = starting value
    # Ye counter SABHI processes ke beech share hoga
    counter = Value('i', 0)
    # 4 processes, har ek 1 lakh baar increment
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    # 4 x 100000 = 400000 hona chahiye (lock ki wajah se sahi aayega)
    print("Final counter value: ",counter.value )
