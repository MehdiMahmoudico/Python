from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models.book import Books
class Users :
    def __init__(self, data) :
        self.id = data['id']
        self.fullname = data['fullname']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_book = []

    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO users (fullname) VALUES (%(fullname)s);"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        for author in results:
            author = cls(author)
        return results
    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results == []:
            return []
        return results[0]
    @classmethod
    def add_to_user(cls,data):
        query = "INSERT INTO favorites (user_id, book_id) values (%(user_id)s,%(book_id)s)"
        return connectToMySQL(DB).query_db(query,data)