from flask  import session , redirect , render_template , request
from flask_app.models.user import User
from flask_app import app


@app.route('/')
def index():
    if 'logged_user_email' in session:
        return redirect('/dashboard')
    return render_template('index.html')
@app.route('/register', methods=['POST'])
def register1():
    data = request.form
    if User.validate_registration(data):
        User.create(data)
    return redirect('/')

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        session['logged_user_email'] = data['email']
        return redirect('/dashboard')
    return redirect('/')
@app.route('/dashboard')
def dashboard():
    if not 'logged_user_email' in session:
        return redirect('/')
    return render_template('welcom.html')

@app.route('/disconnect')
def disconnect():
    session.clear()
    return redirect('/')






