import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT,
            email TEXT
        )
    ''')

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available INTEGER DEFAULT 1
        )
    ''')

    # Create Borrowing History table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrow_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            book_id INTEGER,
            borrowed_date TEXT,
            returned_date TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
    ''')

    # Optionally, add a sample student and book
    cursor.execute("INSERT OR IGNORE INTO students (username, password, name, email) VALUES (?, ?, ?, ?)",
                   ("student1", "password123", "John Doe", "john@example.com"))

    cursor.execute("INSERT OR IGNORE INTO books (title, author, available) VALUES (?, ?, ?)",
                   ("Introduction to Python", "Guido van Rossum", 1))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
