import sqlite3
 
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, year integer, read integer)')
    connection.commit()


def add_db(book, author, year):
    cursor.execute("INSERT INTO books VALUES(?, ?, ?, 0)", (book, author, year))
    connection.commit()
    

def retrive_db():
    cursor.execute('SELECT * from books')
    books_db = [{"BOOK": row[0], "AUTHOR": row[1], "YEAR": str(row[2]), "READ": row[3] } for row in cursor.fetchall()]
    if not books_db:
        return [{"BOOK": 0, "AUTHOR": 0, "YEAR": 0, "READ": 0}]
    return books_db


def _check_book(book_info):
        books_found = [book for book in retrive_db() if book_info in book.values()]
        return books_found


def mark_db(book):
    if [book_name for book_name in _check_book(book) if book_name["BOOK"] == book]:
        cursor.execute("UPDATE books SET read = 1 WHERE name = ?", (book,))
        connection.commit()
        return f"Marked Book:'{book}' as 'Read' "
    return f"Book '{book}'' doesn't exist in Book Store"


def delete_db(book):
    if _check_book(book) and _check_book(book)[0]["BOOK"] == book:
       cursor.execute("DELETE FROM books WHERE name = ?",(book,))
       connection.commit()
       return f"'{book}' is removed from database"
    return f"Book '{book}' doesn't exist in Book Store"
