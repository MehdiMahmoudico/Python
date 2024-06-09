from flask import Flask , render_template , redirect , request , session

app = Flask(__name__)


app.secret_key = 'zefzefzefzefzef'




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process.info',methods=["POST"])
def process():
    session["first_name"]=request.form["first_name"]
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    session["comment"]=request.form["comment"]
    if session["first_name"] and session["location"] and session["language"] and session["comment"] != "":
        return render_template('display.html')
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear
    return redirect('/')



























if __name__ == '__main__':
    app.run(debug=True)