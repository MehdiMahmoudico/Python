import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  


def validateId(id):
    try :
        a,b,c = id.split("-")
        __,___,____ = int(a),int(b),int(c)
    except Exception :
        return False
    else :
        return True

@app.route('/')         
def index():
    return render_template("index.html")


def get_suffix(date):
    if date % 10 == 1:
        suffix='st'
    elif date%10==2:
        suffix='nd'
    elif date%10==3:
        suffix='rd'
    else:
        suffix='th'
    return suffix

@app.route('/checkout', methods=['POST'])         
def checkout():
    id = validateId(request.form["student_id"])
    date = datetime.datetime.now()
    suffixa = get_suffix(date.day)
    dateformat=date.strftime(f"%B %D{suffixa} %Y %I:%M:%S")
    total = int(request.form["strawberry"])+int(request.form["raspberry"])+int(request.form["apple"])
    print(request.form)
    return render_template("checkout.html",total=total, date = dateformat , id = id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    