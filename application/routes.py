from flask import render_template, request, session, url_for, redirect
from application import app
from application.fake_data import validate_login


@app.route('/')
@app.route('/home/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username)


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
