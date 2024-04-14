from flask import render_template, request, session, url_for, redirect
from application import app
from application.data_access import get_all_books, get_genres, insert_student, get_user_role
from application.data_access import get_user
import bcrypt


@app.route('/')
@app.route('/home/')
def home():
    username = session.get('username')
    role = session.get('role')
    return render_template('home.html', username=username, role=role)


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user_info = get_user(username)

    if user_info and bcrypt.checkpw(password.encode('utf-8'), user_info[3].encode('utf-8')):
        session['username'] = username
        session['role'] = get_user_role(username)
        return redirect(url_for('home'))

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


@app.route('/all_students/')
def all_students():
    username = session.get('username')
    role = session.get('role')
    return render_template('all_students.html', username=username, role=role)


# TODO: test this further
# todo: we already have this in the errors.py, is it possible to update that instead?
@app.errorhandler(404)
def page_not_found(e):
    # Access session data
    username = session.get('username')
    role = session.get('role')
    # Render a custom 404 page with session data
    return render_template('404.html', username=username, role=role)
