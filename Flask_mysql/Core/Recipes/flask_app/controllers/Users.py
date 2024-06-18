from flask_app import app
from flask_app.models.User import User
from flask import redirect , render_template , request ,session
from flask_app.controllers import Receipes

@app.route('/')
def index():
    if 'userid' in session:
        return redirect('/receipe')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register() : 
    data = request.form
    if User.validate_register(data):
        User.create_user(data)
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        user = User.get_by_email(data)
        session['userid'] = user.id
        return redirect('/receipe')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')