from flask_app.config.mysqlconnection import connectToMySQL, DB

class Books :
    def __init__(self, data) :
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_user = []


    @classmethod
    def create_book(cls,data):
        query = "INSERT INTO books (title, num_of_pages) values (%(title)s, %(num_of_pages)s)"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DB).query_db(query)
        for book in results:
            book = cls(book)
        return results
    @classmethod
    def get_book_by_id(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results == []:
            return []
        return results[0]
