# ============================================================
# FILE: 01_threading.py
# TOPIC: Threading basics - parallel tasks with threads
# FOLDER: 12_threads_concurrency
# ============================================================
# Threading = ek hi process ke andar multiple kaam EK SAATH chalana
# Jab kaam mein WAITING hoti hai (jaise time.sleep, file download)
# tab threads bahut useful hain - CPU idle nahi rehta
# threading.Thread() se naya thread banao, .start() se chalao, .join() se wait karo
# ============================================================

import threading  # Python ka built-in threading module
import time       # time.sleep() ke liye - simulate karta hai slow kaam

# Ye function order leta hai - har order ke liye 2 second wait
def take_orders():
    for i in range(1, 4):  # 1, 2, 3 - teen orders
        print(f"Taking order for #{i}")
        time.sleep(2)  # 2 second wait - jaise customer soch raha ho

# Ye function chai banata hai - har chai ke liye 3 second wait
def brew_chai():
    for i in range(1, 4):  # 1, 2, 3 - teen chai
        print(f"Brewing chai for #{i}")
        time.sleep(3)  # 3 second wait - chai banne mein time lagta hai
        
# ----- THREADS BANAO -----
# target= function ka naam jo thread run karega
# Thread apne aap nahi chalta - .start() call karna padta hai
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# Dono threads EK SAATH start karo - ab parallel chalenge!
order_thread.start()
brew_thread.start()

# .join() = main program yahan RUK jayega jab tak thread khatam na ho
# Bina join ke main program pehle khatam ho sakta hai
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")
