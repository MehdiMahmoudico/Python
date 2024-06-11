from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja


@app.route('/ninja')
def get_ninjas():
    return render_template('ninja.html',dojo = Dojo.get_all())


@app.route('/create/ninja' , methods=['POST'])
def create():
    Ninja.create(request.form)
    return redirect('/')

@app.route('/delete/<int:id>/<int:id2>/ninja')
def delete(id,id2):
    data = {'id':id}  
    Ninja.delete(data)
    return redirect(f'/show/{id2}')


@app.route("/ninja/<int:id>/update")
def getbyid(id):
    data = {"id":id} 
    return render_template ("update.html",ninja=Ninja.get_by_id(data),dojo = Dojo.get_all())

@app.route('/update/ninja',methods=['POST'])
def update():
    data = {
        "id":request.form["id"],
        "firstname":request.form["firstname"],
        "lastname":request.form["lastname"],
        "age":request.form["age"]}
    Ninja.update(data)
    return redirect ("/")