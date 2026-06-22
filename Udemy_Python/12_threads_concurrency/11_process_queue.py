# ============================================================
# FILE: 11_process_queue.py
# TOPIC: Multiprocessing Queue - processes ke beech data share
# FOLDER: 12_threads_concurrency
# ============================================================
# Processes ki ALAG memory hoti hai - directly variable share NAHI kar sakte
# Queue = thread-safe / process-safe data structure
# Ek process Queue mein data DAALE (put), doosra NIKAALE (get)
# multiprocessing.Queue() - processes ke beech messages bhejne ke liye
# ============================================================

from multiprocessing import Process, Queue

# Child process ye function chalayega aur result queue mein daalega
def prepare_chai(queue):
    queue.put("Masala chai is ready")  # queue mein message daalo



if __name__ == '__main__':
    queue = Queue()  # shared queue banao - processes isse communicate karenge

    # Child process ko queue pass karo as argument
    p = Process(target=prepare_chai, args=(queue,))
    p.start()   # child process start - chai banayega
    p.join()    # child khatam hone ka wait karo
    print(queue.get())  # queue se message nikalo - "Masala chai is ready"
