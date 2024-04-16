from flask import render_template, request, session, url_for, redirect
from application import app
from application.data_access import (get_all_books, get_genres, insert_student, get_students_progress,
                                     get_reading_levels, delete_account)
from application.data_access import get_user
import bcrypt


@app.route('/')
@app.route('/home/')
def home():
    username = session.get('username')
    role = session.get('role')
    books_from_db = get_all_books()
    return render_template('home.html', username=username, role=role, books_from_db=books_from_db)


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
        return render_template('home.html', error='Invalid username or password')


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

    return render_template('my_library.html', title='my_library', username=username, books_from_db=books_from_db,
                           role=role, genres_from_db=genres_from_db)


@app.route('/my_books/')
def my_books():
    username = session.get('username')
    role = session.get('role')
    return render_template('my_books.html', title='my_books', username=username, role=role)


@app.route('/add_student/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        account_type_id = request.form.get('account_type_id')
        username = request.form.get('username')
        password = request.form.get('password')

        # hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        success = insert_student(account_type_id, username, hashed_password)

        if success:
            account_type = "student" if account_type_id == '2' else "teacher"
            return render_template('201.html', account_type=account_type), 201
        else:
            return render_template('500.html'), 500

    username = session.get('username')
    role = session.get('role')
    return render_template('add_student.html', username=username, role=role)


@app.route('/students/reading-progress')
def students():
    username = session.get('username')
    role = session.get('role')
    students_progress = get_students_progress()
    reading_levels = get_reading_levels()
    confirm_delete = session.pop('confirm_delete', None)
    return render_template('all_students.html', title='Students', username=username, role=role,
                           students_progress=students_progress,
                           reading_levels=reading_levels, confirm_delete=confirm_delete)


@app.route('/delete_account/<account_id>/<username>')
def remove_account(account_id, username):

    result = delete_account(account_id)
    confirm_delete = f'Account ID: {account_id}, Username: {username} – successfully deleted.'

    if result is True:
        session['confirm_delete'] = confirm_delete  # Storing the delete confirmation in a session
        return redirect(url_for('students'))


# todo: check get_book function in data access
# @app.route('/my_library/', methods=['GET'])
# def my_library():
#     books = get_book(None, None, None)
#     return render_template('my_library.html', title='my_library', books=books)

# TODO: test this further
# todo: we already have this in the errors.py, is it possible to update that instead?
@app.errorhandler(404)
def page_not_found(e):
    # Access session data
    username = session.get('username')
    role = session.get('role')
    # Render a custom 404 page with session data
    return render_template('404.html', username=username, role=role)


# if __name__ == '__main__':
