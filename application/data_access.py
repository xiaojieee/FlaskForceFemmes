import mysql.connector


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",  # Pa$$w0rd < for windows, please don't delete #todo: mac you do not need password
        database="book_tracker"
    )
    return mydb


# todo: fix this
def get_user(username, password):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "SELECT * FROM Account_ WHERE USERNAME = %s AND password_ = %s"
    cursor.execute(sql, (username, password))
    result_set = cursor.fetchall()

    cursor.close()
    mydb.close()

    return result_set


# todo: I do not have a clue if this works or not
def get_book(title, author, genre):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "SELECT * FROM Book_List WHERE TITLE = %s AND AUTHOR = %s AND GENRE = %s"
    cursor.execute(sql, (title, author, genre))
    all_books = cursor.fetchall()

    cursor.close()
    mydb.close()

    return all_books
