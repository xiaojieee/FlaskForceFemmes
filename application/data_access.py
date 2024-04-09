import mysql.connector


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Pa$$w0rd < for windows, please don't delete
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
