# ============================================================
# FILE: 06_thread_two.py
# TOPIC: Thread with arguments - args parameter
# FOLDER: 12_threads_concurrency
# ============================================================
# Thread ko function ke saath VALUES bhi pass kar sakte ho
# args=(value1, value2) - tuple mein arguments do
# Same function alag-alag data ke saath parallel chal sakta hai
# ============================================================

import threading
import time

# type_ = chai ka type, wait_time = kitna time lagega
def prepare_chai(type_, wait_time ):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)  # alag-alag wait time har chai ke liye
    print(f"{type_} chai: Ready.")

# args=("Masala", 2) - pehla arg type_, doosra wait_time
t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

t1.start()
t2.start()
t1.join()
t2.join()

# Dono chai parallel ban rahi hain - Masala 2s, Ginger 3s
