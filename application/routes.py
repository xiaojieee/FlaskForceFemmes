from flask import render_template, request, session, url_for, redirect
from application import app
from application.data_access import get_all_books, get_genres
from application.data_access import get_user


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


@app.route('/add_student/')
def add_student():
    username = session.get('username')
    role = session.get('role')
    return render_template('add_student.html', username=username, role=role)


@app.route('/all_students/')
def all_students():
    username = session.get('username')
    role = session.get('role')
    return render_template('all_students.html', username=username, role=role)


# TO DO: test this further
@app.errorhandler(404)
def page_not_found(e):
    # Access session data
    username = session.get('username')
    role = session.get('role')
    # Render a custom 404 page with session data
    return render_template('404.html', username=username, role=role)

# todo: check get_book function in data access
# @app.route('/my_library/', methods=['GET'])
# def my_library():
#     books = get_book(None, None, None)
#     return render_template('my_library.html', title='my_library', books=books)
