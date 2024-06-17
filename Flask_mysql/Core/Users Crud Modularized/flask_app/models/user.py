from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data) :
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "select * from users"
        results = connectToMySQL(DB).query_db(query)
        if results == [] :
            return []
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_by_email(cls,data):
        query = "select * from users where email =%(email)s"
        results = connectToMySQL(DB).query_db(query,data)
        if results == ():
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = "select * from users where id =%(id)s"
        results = connectToMySQL(DB).query_db(query,data)
        if results == [] :
            return []
        return cls(results[0])

    @classmethod
    def create(cls,data):
        query ="insert into users (first_name,last_name,email) values(%(first_name)s,%(last_name)s,%(email)s)"
        results = connectToMySQL(DB).query_db(query,data)
        return results
    
    @classmethod
    def update(cls,data):
        query = "update users set first_name=  %(first_name)s, last_name= %(last_name)s, email = %(email)s where id = %(id)s ;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "delete from users where id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        user_exist = User.get_by_email(data)
        if len(data["first_name"]) < 1:
            flash("Invalid first name")
            is_valid = False
        if len(data["last_name"]) < 1:
            flash("Invalid last name")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            is_valid = False
            flash("Invalid email address")
        if user_exist :
            is_valid = False
            flash("Email already exist")

        return is_valid