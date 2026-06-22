# ============================================================
# FILE: 05_thread_one.py
# TOPIC: Threading example - breakfast parallel banwana
# FOLDER: 12_threads_concurrency
# ============================================================
# Real life example: doodh boil karo AUR bun toast karo EK SAATH
# Bina threads: pehle doodh (2s) + phir bun (3s) = 5 seconds
# Threads se: dono parallel = ~3 seconds (jo zyada time le, wahi decide karega)
# ============================================================

import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)  # 2 second - doodh ubalega
    print(f"Milk Boiled...")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)  # 3 second - bun toast hoga
    print(f"Done with bun toast...")
    
start = time.time()  # timer start

# Do threads - ek doodh, ek bun
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()  # doodh thread start
t2.start()  # bun thread start - DONO ek saath!
t1.join()   # doodh khatam hone ka wait
t2.join()   # bun khatam hone ka wait

end = time.time()

# ~3 seconds hoga (max of 2 and 3), 5 nahi!
print(f"Breakfast is ready in {end - start:.2f} seconds")
