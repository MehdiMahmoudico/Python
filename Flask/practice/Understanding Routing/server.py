from flask import Flask, render_template


app = Flask (__name__)

@app.route('/')
def root_route():
    return render_template("index.html")

@app.route('/dojo')
def root_anotherroute():
    return "Dojo"

@app.route('/say/<string:name>/')
def say (name):
    return f"hi {name}"

@app.route('/repeat/<int:number>/<string:random>')
def root_anotherroute2(number,random):
    so = ''
    for i in range (0,number):
        so += random + '<br>'
    return f"{so}"
    
@app.route("/<path:path>")
def not_route (path):
    return f'<h1>Sorry! No response. Try again.<h1>'


if __name__ == '__main__' :
    app.run(debug=True)