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


# Gets all the book data from the database
def get_all_books():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "Select * FROM book_list"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    all_books_list = []

    for book in result_set:
        all_books_list.append({'book_id': book[0], 'title': book[1], 'author': book[2], 'genre': book[
            3], 'pages': book[4], 'reading_level': book[5], 'image_url': book[6], 'book_blurb': book[7]})

    return all_books_list
