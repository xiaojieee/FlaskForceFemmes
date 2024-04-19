import sys
import bcrypt
import mysql.connector


def get_db_connection():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="book_tracker",
            password="Pa$$w0rd" if sys.platform == 'win32' else ""
        )
        return mydb
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


def get_user(username, password):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    try:
        sql = "SELECT * FROM Account_ WHERE USERNAME = %s"
        cursor.execute(sql, (username,))
        user_info = cursor.fetchone()

        if user_info:
            hashed_password = user_info[3]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return user_info

        return None

    except mysql.connector.Error as e:
        return None
    finally:
        cursor.close()
        mydb.close()


# LIBRARY PAGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Gets all the book data from the database
def get_all_books():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "CALL book_tracker.get_books()"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    all_books_list = []

    for book in result_set:

        number = book[8]
        if not number:
            number = 0

        all_books_list.append({'book_id': book[0], 'title': book[1], 'author': book[2], 'genre': book[
            3], 'pages': book[4], 'reading_level': book[5], 'image_url': book[6], 'book_blurb': book[7],
                               'recommended': number})

    return all_books_list


def get_genres():
    mydb = get_db_connection()  # Establishes a connection to our local database
    cursor = mydb.cursor()  # Gives the ability to perform sql commands

    sql = "SELECT * from genre"  # Sql command
    cursor.execute(sql)  # Executes the sql command
    result_set = cursor.fetchall()  # fetches all rows of query result set - [(1, 'Adventure), (2, 'Fantasy')]

    all_genres = []

    for genre in result_set:
        all_genres.append({'genre_id': genre[0], 'genre_name': genre[1]})
        # Adding dictionaries - [{'genre_id': 1, 'genre_name': 'Adventure'}, {'genre_id': 2, 'genre_name': 'Fantasy'}]

    return all_genres


# MY BOOKS PAGE | STUDENT ACCOUNT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def add_reading_progress(username, book_id, start_date=None, current_page=None, completed_date=None, rating=None):
    # start_date, current_page, completed_date and rating parameters are not required
    # date format should be 2024-03-09

    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = f"CALL book_tracker.add_reading_progress(%s, %s, %s, %s, %s, %s)"
    values = (username, book_id, start_date, current_page, completed_date, rating)

    try:
        cursor.execute(sql, values)
        mydb.commit()  # Commit changes
        return True

    except mysql.connector.Error as duplicate_error:

        if duplicate_error.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            return "Book tracking already recorded"

    cursor.close()  # Close cursor
    mydb.close()  # Close database connection


def get_student_books(username):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = f"CALL book_tracker.get_student_books('{username}')"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    student_books = []

    for book in result_set:
        student_books.append({'account_id': book[0], 'username': book[1], 'book_id': book[2],
                             'start_date': book[3], 'current_page': book[4], 'completed_date': book[5], 'rating': book[
                6]})

    return student_books


# ALL STUDENTS PAGE | TEACHER ACCOUNT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def get_students_progress():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "CALL book_tracker.get_students_progress()"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    all_students = []

    for student in result_set:
        all_students.append({'account_id': student[0], 'username': student[1], 'reading_level': student[2],
                             'current_books': student[3], 'books_week': student[4], 'total_books': student[5]})

    return all_students


def delete_account(account_id):  # Deletes account history on reading_progress table too
    mydb = get_db_connection()
    cursor = mydb.cursor()
    account_id = int(account_id)

    sql = f"CALL book_tracker.remove_account({account_id})"
    cursor.execute(sql)

    mydb.commit()  # Commit changes
    cursor.close()  # Close cursor
    mydb.close()  # Close database connection

    return True


def get_reading_levels():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "SELECT * from reading_level order by level"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    all_reading_levels = []

    for level in result_set:
        all_reading_levels.append({'level_id': level[0], 'colour': level[1]})

    return all_reading_levels


def update_colour_level(account_id, colour):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = f"CALL book_tracker.update_reading_level({account_id}, '{colour}')"
    cursor.execute(sql)

    mydb.commit()  # Commit changes
    cursor.close()  # Close cursor
    mydb.close()  # Close database connection

    return True


def update_recommended(book_id_parameter, boolean):
    # boolean value needs to be 0 for false or 1 for true in sql
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = f"UPDATE book_list SET recommended = {boolean} WHERE book_id = {book_id_parameter}"
    cursor.execute(sql)

    mydb.commit()  # Commit changes
    cursor.close()  # Close cursor
    mydb.close()  # Close database connection

    return True


# ADD STUDENT PAGE | TEACHER ACCOUNT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def insert_student(account_type_id, username, password, reading_level_id):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "INSERT INTO Account_ (Account_type_id, Username, Password_, Reading_Level_id) VALUES (%s, %s, %s, %s)"
    val = (account_type_id, username, password.decode('utf-8'), reading_level_id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()  # Close cursor
    mydb.close()  # Close database connection
    return True


def check_username(username):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    # Check if the username already exists
    cursor.execute("SELECT Username FROM Account_ WHERE Username = %s", (username,))
    existing_username = cursor.fetchone()

    cursor.close()  # Close cursor
    mydb.close()  # Close database connection

    return existing_username


# ADD BOOK PAGE | TEACHER ACCOUNT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def insert_book(title, author_name, genre_id, pages, reading_level_id, book_image, blurb):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    # insert the author name into the author table first
    cursor.execute("SELECT Author_ID FROM Author WHERE Name = %s", (author_name,))
    author_row = cursor.fetchone()

    # if the author already exist it will no longer need inserting
    if author_row:
        author_id = author_row[0]
    else:
        cursor.execute("INSERT INTO Author (Name) VALUES (%s)", (author_name,))
        mydb.commit()
        author_id = cursor.lastrowid

    # insert book and the author id that was just created/already created
    sql = ("INSERT INTO Book_List (Title, Author_ID, Genre_ID, Pages, Reading_Level_ID, Book_image, Blurb) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    val = (title, author_id, genre_id, pages, reading_level_id, book_image, blurb)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()  # Close cursor
    mydb.close()  # Close database connection

    return True


def check_book(title, author_name):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    # check based on title and author if the book is already in the database or not
    cursor.execute("SELECT Book_ID FROM Book_List WHERE Title = %s AND Author_ID IN "
                   "(SELECT Author_ID FROM Author WHERE Name = %s)", (title, author_name))
    existing_book = cursor.fetchone()

    cursor.close()
    mydb.close()

    return existing_book

#
# if __name__ == '__main__':

    # result = add_reading_progress('cat', 5)
    # print(result)

    # result = update_recommended(4, 1)
    # print(result)

    # print(get_student_books('cat'))
