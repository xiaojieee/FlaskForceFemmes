import mysql.connector


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Pa$$w0rd < for windows, please don't delete
        database=""
    )
    return mydb
