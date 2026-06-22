# ============================================================
# FILE: 07_thread_download.py
# TOPIC: Threading for I/O - parallel file downloads
# FOLDER: 12_threads_concurrency
# ============================================================
# Network requests (I/O) mein threads BAHUT useful hain
# Jab ek thread network ka wait kar raha hai, doosra kaam kar sakta hai
# GIL I/O ke time RELEASE hota hai - isliye downloads parallel hote hain
# requests.get() blocking hai - thread mein daalne se main program free rehta hai
# ============================================================

import threading
import requests  # HTTP requests ke liye third-party library
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)  # blocking call - network se data aane tak wait
    # len(resp.content) = kitne bytes download hue
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

# Teen alag images download karni hain
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []  # saare threads yahan store karenge

# Har URL ke liye ek naya thread banao aur start karo
for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)  # baad mein join ke liye list mein rakho

# Sab downloads khatam hone ka wait karo
for t in threads:
    t.join()

end = time.time()

# Teen downloads parallel hue - total time ek download jitna (~same), teen ka nahi!
print(f"All downloads done in {end - start:.2f} seconds")
