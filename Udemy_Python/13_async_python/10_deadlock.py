# ============================================================
# FILE: 10_deadlock.py
# TOPIC: Deadlock - do locks, galat order = program ATAK jata hai
# FOLDER: 13_async_python
# ============================================================
# Deadlock = do threads ek-dusre ka wait kar rahe hain, koi aage nahi badh sakta
# Task1: pehle lock_a, phir lock_b
# Task2: pehle lock_b, phir lock_a  <-- OPPOSITE ORDER = DEADLOCK!
# Task1 ne lock_a liya, Task2 ne lock_b liya
# Ab Task1 lock_b chahta hai (Task2 ke paas), Task2 lock_a chahta hai (Task1 ke paas)
# Dono forever wait - program HANG!
# Fix: hamesha locks SAME ORDER mein lo
# ============================================================

import threading

lock_a = threading.Lock()  # pehla lock
lock_b = threading.Lock()  # doosra lock


def task1():
    with lock_a:  # lock_a acquire kiya
        print("Task 1 acquired lock a")
        with lock_b:  # lock_b chahta hai - lekin Task2 ke paas hai!
            print("Task 1 acquired lock b")

def task2():
    with lock_b:  # lock_b acquire kiya - OPPOSITE ORDER!
        print("Task 2 acquired lock b")
        with lock_a:  # lock_a chahta hai - lekin Task1 ke paas hai!
            print("Task 2 acquired lock a")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
# Program yahan HANG ho jayega - DEADLOCK!
# Ctrl+C se band karna padega
