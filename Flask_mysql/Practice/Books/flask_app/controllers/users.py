from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import Users
from flask_app.models.book import Books
@app.route("/")
def index() :
    data = Users.get_all_authors()
    return render_template("authors.html", authors = data)

@app.route("/create/user", methods=["POST"])
def create_user() :
    Users.create_author(request.form)
    return redirect("/")

@app.route("/author/<int:id>")
def author_id(id):
    data = {"id":id}
    author=Users.get_one_author(data)
    return render_template("authorpage.html", authors = author, data2 = Books.get_all_books())