from flask import Flask , render_template


app = Flask(__name__)


@app.route('/play')
def root1() :
    return render_template ("play.html", x=3 , color = "cyan")


@app.route('/play/<int:x>')
def play (x):
    return render_template ("play.html",x=x)


@app.route('/play/<int:x>/<string:color>')
def color (x,color):
    return render_template ("play.html",x=x,color=color)


if __name__ == '__main__':
    app.run(debug=True)