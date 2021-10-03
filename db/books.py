import sqlite3
from sqlite3 import Error
from .connection import create_Connection


def insert_Book(data):
    conn = create_Connection()
    sql = """ INSERT INTO books (title, category, page_qty, book_path, description)
                VALUES(?,?,?,?,?) """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print('New Book Added')
        return True, cur.lastrowid
    except Error as e:
        print('Error inserting new book: ' + str(e))

    finally: 
        if conn:
            cur.close()
            conn.close()



def update_Book(_id, data):
    conn = create_Connection()

    sql = f""" UPDATE books SET  
                    title = ?,
                    category = ?,
                    page_qty = ?,
                    page_qty_read = ?,
                    book_path = ?,
                    description = ?
            WHERE book_id = {_id}
     """ 

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print('Book Updated')
        return True 
    except Error as e:
        print('Error editing book: ' + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_Book(_id):
    conn = create_Connection()

    sql = f"DELETE FROM books WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print('Book deleted')
        return True 
    except Error as e:
        print('Error deleting book: ' + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()       
    

def select_All_Books():
    conn = create_Connection()
    sql = "SELECT * FROM books"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books 
    except Error as e:
        print('Error selecting all books: ' + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_Book_By_Id(_id):
    conn = create_Connection()
    sql = f"SELECT * FROM books WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book 
    except Error as e:
        print('Error selecting book by id: ' + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_Book_By_Title(title):
    conn = create_Connection()
    sql = f"SELECT * FROM books WHERE title LIKE '%{title}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books 
    except Error as e:
        print('Error selecting book by title: ' + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_Book_By_Category(category):
    conn = create_Connection
    sql = f"SELECT * FROM books WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        book = cur.fetchall()
        return book 
    except Error as e:
        print('Error selecting book by category: ' + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
