from flask_app import app
from flask_app.models.User import User
from flask_app.models.Receipe import Receipe
from flask import redirect , render_template , request ,session
from flask_app.controllers import Users
import datetime

@app.route('/receipe')
def receipe():
    if not 'userid' in session:
        return redirect('/')
    user_data = {"id":session["userid"]}
    logged_user = User.get_by_id(user_data)
    receipe1 = Receipe.get_all()

    return render_template('dashboard.html', users= logged_user, receipe = receipe1)

@app.route('/receipe/new')
def new_receipe():
    if not 'userid' in session:
        return redirect('/')
    user_data = {"id":session["userid"]}
    logged_user = User.get_by_id(user_data)
    return render_template('new_receipe.html', users= logged_user)

@app.route('/receipe/create', methods=['POST'])
def create_receipe():
    if not 'userid' in session:
        return redirect('/')
    data = request.form
    Receipe.create(data)
    return redirect('/receipe')

@app.route('/receipe/<int:id>/delete')
def delete_receipe(id):
    data = {'id':id}
    Receipe.delete(data)
    return redirect('/receipe')

@app.route('/receipe/<int:id>/edit')
def edit_receipe(id):
    if not 'userid' in session:
        return redirect('/')
    data = {'id':id}
    receipe = Receipe.get_one(data)
    user_data = {"id":session["userid"]}
    logged_user = User.get_by_id(user_data)
    if receipe.user.id != logged_user.id :
        return redirect('/receipe')
    return render_template('/editme.html', receipes = receipe)

@app.route('/receipe/edit', methods = ['POST'])
def update_receipe():
    if not 'userid' in session:
        return redirect('/')
    data = request.form
    Receipe.update(data)
    return redirect('/receipe')



@app.route('/receipe/<int:id>/show')
def show_receipe(id):
    if not 'userid' in session:
        return redirect('/')
    data = {'id':id}
    user_data = {"id":session["userid"]}
    logged_user = User.get_by_id(user_data)
    receipe = Receipe.get_one(data)
    datet = receipe.date_made
    dates=datet.strftime((f"%B %d ,%Y"))
    return render_template('/show.html', receipes = receipe, users = logged_user , date = dates)
