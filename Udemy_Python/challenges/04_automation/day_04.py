# =============================================================================
# FILE    : day_04.py
# TOPIC   : Real-Time System Resource Monitor (CPU, RAM, Disk check karna)
# FOLDER  : challenges/04_automation/
# CHALLENGE DAY : Day 04
# =============================================================================
#
# Yeh script aapke computer ki CPU, RAM aur Disk usage live dikhati hai.
# Har 3 second mein screen refresh hoti hai — jaise terminal dashboard!
# psutil library system ki health check karti hai.

"""
 Challenge: Real-Time System Resource Monitor

Goal:
- Monitor your system's CPU, RAM, and Disk usage
- Print updates every few seconds
- Warn user if CPU or RAM usage exceeds 80%
- Runs in terminal as a live dashboard

Teaches: psutil, formatting, real-time monitoring, conditional logic
Tools: psutil, time
"""

# psutil = Process and System Utilities — CPU, RAM, disk info deta hai
import psutil

# time module — program ko rukne ke liye (sleep)
import time

# os module — screen clear karne ke liye
import os


def clear_screen():
    """
    Terminal screen ko saaf karta hai taaki purana output hat jaye.
    Windows par 'cls', Mac/Linux par 'clear' command chalti hai.
    """
    # os.name == 'nt' matlab Windows hai
    os.system('cls' if os.name == 'nt' else 'clear')


def show_stats():
    """
    CPU, RAM aur Disk ka usage print karta hai — ek baar ka snapshot.
    """
    print("🔥" * 30)  # "*" se string repeat hoti hai — decorative line
    print("⭐️ System Resource Monitor ⭐️")

    # cpu_percent(interval=1) = 1 second wait karke CPU usage % batata hai
    cpu = psutil.cpu_percent(interval=1)

    # virtual_memory() = RAM ki details — .percent se usage % milta hai
    ram = psutil.virtual_memory()

    # disk_usage('/') = root disk ki info (Mac/Linux); Windows par bhi kaam karta hai
    disk = psutil.disk_usage('/')

    print(f"CPU USAGE: {cpu}")
    # ram.used / 1e9 = bytes ko GB mein convert (1e9 = 1 billion)
    # round(..., 2) = 2 decimal places tak round karo
    print(f"RAM USAGE: {ram.percent}% ( {round(ram.used / 1e9, 2)} GB used of {round(ram.total / 1e9, 2)} GB)")
    print(f"DISK USAGE: {disk.percent}% ( {round(disk.used / 1e9, 2)} GB used of {round(disk.total / 1e9, 2)} GB)")
    print("🔥" * 30)


# Script run hone par live monitoring shuru
if __name__ == "__main__":
    try:
        # Har baar: screen clear → stats dikhao → 3 second ruko → repeat
        while True:
            clear_screen()
            show_stats()
            time.sleep(3)  # 3 second wait — phir dubara refresh
    except KeyboardInterrupt:
        # Ctrl+C se band karo
        print("Monitoring Stopped.....")
