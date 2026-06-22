# =============================================================================
# FILE    : models.py
# TOPIC   : Database Layer — SQLite se URLs save/read/delete karna
# FOLDER  : challenges/06_url_shortner/
# CHALLENGE DAY : URL Shortener Challenge
# =============================================================================
#
# Yeh file sirf database se baat karti hai — app.py UI handle karta hai.
# SQLite = file-based database, alag server install karne ki zaroorat nahi.
# Har function ek kaam karta hai: create table, insert, get, update count, delete.

import sqlite3  # Python built-in — SQLite database ke liye


# Database file ka naam — same folder mein database.db ban jayegi
DB_NAME = 'database.db'


def init_db():
    """
    App pehli baar chalne par urls table create karta hai.
    IF NOT EXISTS = table pehle se hai toh dubara mat banao.
    """
    # with sqlite3.connect() = connection open + automatically close (safe!)
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     original_url TEXT NOT NULL,
                     short_code TEXT UNIQUE NOT NULL,
                     visit_count INTEGER DEFAULT 0
                     )
        ''')
        # id = auto-increment primary key
        # original_url = lambi URL
        # short_code = chhoti link ka code, UNIQUE = duplicate nahi
        # visit_count = kitni baar link khuli, default 0


def insert_url(original_url, short_code):
    """
    Nayi URL + short code database mein insert karta hai.
    ? placeholders = SQL injection se bachne ke liye safe parameterized query
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO urls (original_url, short_code)
                     VALUES (?, ?)
        ''', (original_url, short_code))


def get_url(short_code):
    """
    Short code se poori row dhundhta hai.
    fetchone() = ek row ya None — mila toh tuple return (id, url, code, visits)
    """
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
        return cur.fetchone()


def increment_visit_count(short_code):
    """
    Jab koi short link click kare, visit_count 1 se badha deta hai.
    UPDATE query — existing row modify hoti hai, nayi row nahi.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            UPDATE urls
            SET visit_count = visit_count + 1
            WHERE short_code = ?         
        ''', (short_code,))


def get_all_urls():
    """
    Homepage par dikhane ke liye saari URLs list karta hai.
    ORDER BY id DESC = nayi entries pehle (latest first)
    fetchall() = saari matching rows ki list
    """
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('SELECT original_url, short_code, visit_count FROM urls ORDER by id DESC')
        return cur.fetchall()


def delete_url_by_code(short_code):
    """
    Short code se URL entry database se hata deta hai.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE from urls WHERE short_code = ?', (short_code,))
