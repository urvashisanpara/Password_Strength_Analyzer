import sqlite3
import hashlib

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
id INTEGER PRIMARY KEY AUTOINCREMENT,
hash TEXT UNIQUE
)
""")

conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def password_exists(password):
    hashed = hash_password(password)
    cursor.execute("SELECT * FROM passwords WHERE hash=?", (hashed,))
    return cursor.fetchone() is not None

def save_password(password):
    hashed = hash_password(password)

    if not password_exists(password):
        cursor.execute("INSERT INTO passwords(hash) VALUES(?)", (hashed,))
        conn.commit()
