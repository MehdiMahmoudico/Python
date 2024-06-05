from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def rout():
    return render_template ('index.html',x=8 , y=8 ,color1="white",color2="black")



@app.route("/<int:x>")
def rout2(x):
    return render_template ('index.html',x=x,y=8,color1="white",color2="black")

@app.route("/<int:x>/<int:y>")
def rout3(x,y):
    return render_template('index.html',x=x,y=y,color1="white",color2="black")

@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def rout4(x,y,color1,color2):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
