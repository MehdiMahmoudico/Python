from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.book import Books
from flask_app.models.user import Users



@app.route('/books')
def books():
    data = Books.get_all_books()
    return render_template('books.html', books=data)
@app.route('/create_book', methods=['POST'])
def create_book():
    Books.create_book(request.form)
    return redirect('/books')
@app.route('/book/<int:id>')
def book_id(id):
    data = {"id": id}
    Books1 = Books.get_book_by_id(data)
    return render_template('bookpage.html', book=Books1 , authors = Users.get_all_authors())

@app.route("/author/favorite",methods=["POST"])
def author_favorite():
    data = {
        "user_id" : request.form["user_id"],
        "book_id" : request.form["book_id"]
    }
    Users.add_to_user(data)
    return redirect(f'/book/{request.form["book_id"]}')