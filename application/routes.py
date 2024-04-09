from flask import render_template, request, session, url_for, redirect
from application import app
from application.fake_data import validate_login
# from application.data_access import get_book # todo: uncomment after fixing
# from application.data_access import get_user # todo: uncomment after fixing


@app.route('/')
@app.route('/home/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username)


# todo: update with database data, see get_user in data access
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Perform login validation
    if validate_login(username, password):
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error='Invalid username or password')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('remember_me', None)  # Clear the "Remember me" flag from session
    return redirect(url_for('home'))


@app.route('/my_library')
def my_library():
    return render_template('my_library.html', title='my_library')


# todo: check get_book function in data access
# @app.route('/my_library/', methods=['GET'])
# def my_library():
#     books = get_book(None, None, None)
#     return render_template('my_library.html', title='my_library', books=books)
