from flask import render_template, request, session, url_for, redirect
from application import app
from application.data_access import (get_all_books, get_genres, insert_student, get_students_progress,
                                     get_reading_levels, delete_account, update_colour_level, insert_book,
                                     check_username, check_book, update_recommended, get_student_books)
from application.data_access import get_user, update_student_book
from application.data_access import add_reading_progress, delete_reading_progress
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
    # app.logger.debug("Username is: " + username)
    role = session.get('role')
    books_from_db = get_all_books()
    genres_from_db = get_genres()

    return render_template('my_library.html', title='Library', username=username, books_from_db=books_from_db,
                           role=role, genres_from_db=genres_from_db)


@app.route('/my_books/', methods=['GET', 'POST'])
def my_books():
    selected_books = request.form.getlist('selected_books')
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    genres_from_db = get_genres()
    saved_books_db = get_student_books(username)
    confirm_update = session.pop('confirm_book_update', None)

    # Pass the reading progress data to the template for rendering
    return render_template('my_books.html', title='My Books', username=username,
                           books_from_db=books_from_db, role=role, genres_from_db=genres_from_db,
                           selected_books=selected_books, saved_books_db=saved_books_db, confirm_update=confirm_update)


@app.route('/update_student_book/<int:book_id>/', methods=['POST'])
def update_account_book(book_id):
    username = session.get('username')
    start_date = request.form.get("start_date")
    current_page = request.form.get("current_page")
    completed_date = request.form.get("completed_date")
    rating = request.form.get("rating")

    if start_date == '':
        start_date = None

    if current_page == '':
        current_page = None

    if completed_date == '':
        completed_date = None

    if rating == '':
        rating = None

    confirm_update = 'Your book tracking update has been saved.'
    result = update_student_book(username, book_id, start_date, current_page, completed_date, rating)

    if result is True:
        session['confirm_book_update'] = confirm_update  # Storing the update confirmation in a session
        return redirect(url_for('my_books'))


@app.route('/students/recommended-books/')
def recommended_books():
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    genres_from_db = get_genres()
    reading_levels_db = get_reading_levels()
    return render_template('recommended_books.html', title='Select Books for Students',
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

        existing_username = check_username(username)

        if existing_username:
            error_message = "This username is taken. Please choose a different username."
            return render_template('add_student.html', error_message=error_message,
                                   username=session.get('username'), role=session.get('role'),
                                   title='Add Student Account')

        if reading_level_id:
            success = insert_student(account_type_id, username, hashed_password, reading_level_id)
        else:
            success = insert_student(account_type_id, username, hashed_password, None)

        if success:
            account_type = "a student account" if account_type_id == '2' else "a teacher account"
            return render_template('201.html', account_type=account_type,
                                   username=session.get('username'), role=session.get('role')), 201
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
    confirm_colour = f'{username} – Reading Level: {colour} – successfully updated.'

    if result is True:
        session['confirm_colour_update'] = confirm_colour  # Storing the update confirmation in a session
        return redirect(url_for('students'))


@app.route('/update_recommended/<int:book_id>/<int:boolean_num>')
def update_recommended_book(book_id, boolean_num):
    if boolean_num == 0:
        result = update_recommended(book_id, 1)
    else:
        result = update_recommended(book_id, 0)

    if result is True:
        return redirect(url_for('recommended_books'))


@app.route('/delete_account/<int:account_id>/<username>/')
def remove_account(account_id, username):
    result = delete_account(account_id)
    confirm_delete = f'{username} – account successfully deleted.'

    if result is True:
        session['confirm_delete'] = confirm_delete  # Storing the delete confirmation in a session
        return redirect(url_for('students'))


@app.route('/students/add-book/', methods=['GET', 'POST'])
def add_book():
    username = session.get('username')
    role = session.get('role')

    if request.method == 'POST':
        title = request.form.get('title')
        author_name = request.form.get('author')
        genre_id = request.form.get('genre_id')
        pages = request.form.get('pages')
        reading_level_id = request.form.get('reading_level')
        book_image = request.form.get('book_image')
        blurb = request.form.get('blurb')

        existing_book = check_book(title, author_name)

        if existing_book:
            error_message = "This book is already in the catalogue, try adding a different book."
            return render_template('add_book.html', error_message=error_message, username=username, role=role)

        success = insert_book(title, author_name, genre_id, pages, reading_level_id, book_image, blurb)

        if success:
            return render_template('201.html', title=title, username=username, role=role), 201
        else:
            return render_template('500.html'), 500

    return render_template('add_book.html', username=username, role=role)


@app.route('/save_book/', methods=['GET', 'POST'])
def save_book():
    if request.method == 'POST':
        # Extract the book ID from the request form data
        book_id = request.form.get('book_id')
    elif request.method == 'GET':
        # Extract the book ID from the URL query string
        book_id = request.args.get('book_id')

    # Get the username of the current user from the session
    username = session.get('username')

    # Check if the user is logged in
    if username:
        # Call the stored procedure to save the book for the user
        success = add_reading_progress(username, book_id, start_date=None, current_page=None, completed_date=None,
                                       rating=None)
        if success:
            msg = "Book saved successfully!"
        else:
            msg = "Failed to save book."

        return redirect(url_for('my_books'))  # Return a valid response


@app.route('/remove_book', methods=['POST'])
def remove_from_reading_list():
    username = request.form.get('username')
    book_id = request.form.get('book_id')

    # function call to delete the book from the reading list
    success = delete_reading_progress(username, book_id)
    confirm_update = 'Book removed from reading list' if success else 'Failed to remove book from reading list'
    session['confirm_book_update'] = confirm_update

    return redirect(url_for('my_books'))

# if __name__ == '__main__':
