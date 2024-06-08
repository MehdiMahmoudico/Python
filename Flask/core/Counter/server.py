from flask import Flask , render_template , session ,redirect , request


app = Flask(__name__)
app.secret_key = 'aeazdazdazdlf;z^f;'



@app.route('/' )
def index():
    if "count" not in session :
        session["count"] = 0
    session["count"] += 1
    return render_template('index.html')


@app.route('/plus')
def plus():
    session["count"] += 0
    return redirect('/')

@app.route('/increms')
def increms():
    session["count"] += 1
    return redirect('/')

@app.route('/increms1', methods=['POST'])
def increms1():
    session["count"] += int(request.form["texte"]) - 1
    return redirect('/')


@app.route('/increm')
def increm():
    session.clear()
    return redirect('/')


if __name__== '__main__':
    app.run(debug=True)