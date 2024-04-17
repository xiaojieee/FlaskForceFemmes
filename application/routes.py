from flask import render_template, request, session, url_for, redirect
from application import app
from application.data_access import (get_all_books, get_genres, insert_student, get_students_progress,
                                     get_reading_levels, delete_account, update_colour_level, insert_book)
from application.data_access import get_user
import bcrypt


@app.route('/')
@app.route('/home/')
def home():
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    return render_template('home.html', username=username, role=role, books_from_db=books_from_db, title='Home')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Perform login validation
    is_valid_login, role = False, None
    result_set = get_user(username, password)
    if result_set:
        is_valid_login, role = True, result_set[1]
    if is_valid_login:
        session['username'] = username
        session['role'] = role
        return redirect(url_for('home'))
    else:
        return render_template('home.html', error='Invalid username or password', title='Home')


@app.route('/logout/')
def logout():
    # session.clear()
    session.pop('username', None)
    session.pop('remember_me', None)  # Clear the "Remember me" flag from session
    return redirect(url_for('home'))


@app.route('/my_library/')
def my_library():
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    genres_from_db = get_genres()

    return render_template('my_library.html', title='Library', username=username, books_from_db=books_from_db,
                           role=role, genres_from_db=genres_from_db)


@app.route('/my_books/')
def my_books():
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    genres_from_db = get_genres()
    return render_template('my_books.html', title='My Books', username=username,
                           books_from_db=books_from_db, role=role, genres_from_db=genres_from_db)


@app.route('/recommended_books/')
def recommended_books():
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    genres_from_db = get_genres()
    reading_levels_db = get_reading_levels()
    return render_template('recommended_books.html', title='Add Recommended Books',
                           username=username, books_from_db=books_from_db, role=role, genres_from_db=genres_from_db,
                           reading_levels_db=reading_levels_db)


@app.route('/add_student/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        account_type_id = request.form.get('account_type_id')
        username = request.form.get('username')
        password = request.form.get('password')
        reading_level_id = request.form.get('Reading_Level_id')

        # hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if reading_level_id:
            success = insert_student(account_type_id, username, hashed_password, reading_level_id)
        else:
            success = insert_student(account_type_id, username, hashed_password, None)

        if success:
            account_type = "a student account" if account_type_id == '2' else "a teacher account"
            return render_template('201.html', account_type=account_type), 201
        else:
            return render_template('500.html'), 500

    username = session.get('username')
    role = session.get('role')
    return render_template('add_student.html', username=username, role=role, title='Add Student Account')


@app.route('/students/reading-progress/')
def students():
    username = session.get('username')
    role = session.get('role')
    students_progress = get_students_progress()
    reading_levels = get_reading_levels()

    confirm_colour = session.pop('confirm_colour_update', None)
    confirm_delete = session.pop('confirm_delete', None)

    return render_template('all_students.html', title='Students Reading Progress', username=username, role=role,
                           students_progress=students_progress, reading_levels=reading_levels,
                           confirm_colour=confirm_colour, confirm_delete=confirm_delete)


@app.route('/update_reading_level/<int:account_id>/<username>/<colour>')
def update_reading_level(account_id, username, colour):
    result = update_colour_level(account_id, colour)
    confirm_colour = f'{username}, Reading Level: {colour} – successfully updated.'

    if result is True:
        session['confirm_colour_update'] = confirm_colour  # Storing the update confirmation in a session
        return redirect(url_for('students'))


@app.route('/delete_account/<int:account_id>/<username>/')
def remove_account(account_id, username):

    result = delete_account(account_id)
    confirm_delete = f'{username} – account successfully deleted.'

    if result is True:
        session['confirm_delete'] = confirm_delete  # Storing the delete confirmation in a session
        return redirect(url_for('students'))


@app.route('/add_book/', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author_name = request.form.get('author')
        genre_id = request.form.get('genre_id')
        pages = request.form.get('pages')
        reading_level_id = request.form.get('reading_level')
        book_image = request.form.get('book_image')
        blurb = request.form.get('blurb')

        success = insert_book(title, author_name, genre_id, pages, reading_level_id, book_image, blurb)

        if success:
            return render_template('201.html', title=title), 201
        else:
            return render_template('500.html'), 500

    return render_template('add_book.html')

# if __name__ == '__main__':
