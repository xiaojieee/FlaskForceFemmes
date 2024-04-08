from flask import render_template
from application import app


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html',title='home')

@app.route('/my_library')
def my_library():
    return render_template('my_library.html', title='my_library')


