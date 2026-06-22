# ============================================================
# FILE: 03_async_three.py
# TOPIC: aiohttp - async HTTP requests (real-world I/O)
# FOLDER: 13_async_python
# ============================================================
# aiohttp = async version of requests library
# async with = context manager jo automatically cleanup karta hai
# ClientSession = connection pool - multiple requests ke liye reuse karo
# asyncio.gather(*tasks) = * se list unpack hoti hai as separate arguments
# 3 URLs parallel fetch = ek request ka wait time mein baaki bhi chal sakti hain
# ============================================================

import asyncio
import aiohttp  # async HTTP library - pip install aiohttp

async def fetch_url(session, url):
    # async with = session automatically close hogi block ke baad
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3  # 3 URLs, har ek 2 sec delay
    # ClientSession = ek baar banao, sab requests isi se karo
    async with aiohttp.ClientSession() as session:
        # Har URL ke liye ek coroutine (task) banao
        tasks = [fetch_url(session, url) for url in urls]
        # tasks = [t1, t2, t3]
        # *tasks = list ko unpack karke alag arguments banao
        await asyncio.gather(*tasks)  # teeno parallel fetch!
        

asyncio.run(main())
