import sqlite3

def connect_db():
    conn = sqlite3.connect('school_manager.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        grade INTEGER NOT NULL,
                        address TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                        student_id TEXT,
                        subject TEXT,
                        marks REAL,
                        FOREIGN KEY (student_id) REFERENCES students (student_id))''')

    conn.commit()
    conn.close()
