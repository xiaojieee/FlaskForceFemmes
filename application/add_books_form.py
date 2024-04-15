from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="book_tracker"
)
cursor = db.cursor()


@app.route('/')
def index():
    return render_template('add_book_form.html')


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author']
    genre_id = request.form['genre']
    pages = request.form['pages']
    reading_level_id = request.form['reading_level']
    image_url = request.form['image_url']
    blurb = request.form['blurb']

    # Insert the book into the database
    insert_query = "INSERT INTO Book_List (Title, Author_ID, Genre_ID, Pages, Reading_Level_ID, Book_image, Blurb) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (title, author_id, genre_id, pages, reading_level_id, image_url, blurb)
    cursor.execute(insert_query, data)
    db.commit()

    return "Book added successfully!"


if __name__ == '__main__':
    app.run(debug=True)
