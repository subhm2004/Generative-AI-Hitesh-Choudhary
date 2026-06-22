# ============================================================
# FILE: 08_thread_lock.py
# TOPIC: Thread Lock - race condition se bachna
# FOLDER: 12_threads_concurrency
# ============================================================
# Race Condition = jab multiple threads EK HI variable ko
# ek saath badalte hain - result GALAT ho sakta hai
# Lock = ek thread ko variable access karne deta hai, baaki WAIT karte hain
# threading.Lock() + "with lock:" = safe way to update shared data
# Bina lock ke counter 1,000,000 hona chahiye tha, kam aayega!
# ============================================================

import threading

counter = 0  # shared variable - sab threads isko badalenge
lock = threading.Lock()  # Lock object banao - ek thread ek time access kare

def increament():
    global counter  # global keyword - bahar wala counter use karo
    for _ in range(100000):  # 1 lakh baar badhao
        # "with lock:" = lock acquire karo, kaam karo, phir release
        # Jab tak ek thread andar hai, doosra WAIT karega
        with lock:
            counter += 1  # safe increment - race condition nahi hogi

# 10 threads, har ek 1 lakh baar increment = total 10 lakh hona chahiye
threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]  # sab start karo
[t.join() for t in threads]   # sab khatam hone ka wait

print(f"Final counter: {counter}")  # Lock ke saath exactly 1000000 aayega
