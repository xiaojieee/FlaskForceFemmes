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


# Gets all the book data from the database
def get_all_books():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "CALL book_tracker.get_books()"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    all_books_list = []

    for book in result_set:
        all_books_list.append({'book_id': book[0], 'title': book[1], 'author': book[2], 'genre': book[
            3], 'pages': book[4], 'reading_level': book[5], 'image_url': book[6], 'book_blurb': book[7]})

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


def insert_student(account_type_id, username, password):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "INSERT INTO Account_ (Account_type_id, Username, Password_) VALUES (%s, %s, %s)"
    val = (account_type_id, username, password.decode('utf-8'))
    cursor.execute(sql, val)
    mydb.commit()
    return True


if __name__ == '__main__':
    get_genres()
