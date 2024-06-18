from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.User import User
from flask_app import app

class Receipe : 
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
 
        self.user = None


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes join users on recipes.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        if not results :
            return []
        receipes = []
        for row in results:
            receipe = cls(row)
            user_data = {
                'id':row["users.id"],
                'first_name':row["first_name"],
                'last_name': row["last_name"],
                'email': row["email"],
                'password':row["password"],
                'created_at': row["users.created_at"],
                'updated_at': row["users.updated_at"]
            }
            receipe.user = User(user_data)
            receipes.append(receipe)
        return receipes
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes join users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if not results:
            return None
        receipe = cls(results[0])
        user_data = {
            'id':results[0]["users.id"],
            'first_name':results[0]["first_name"],
            'last_name': results[0]["last_name"],
            'email': results[0]["email"],
            'password':results[0]["password"],
            'created_at': results[0]["users.created_at"],
            'updated_at': results[0]["users.updated_at"]
        }
        receipe.user = User(user_data)
        return receipe
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO recipes (name,description,instructions,date_made,under,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under)s,%(user_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under = %(under)s WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return results
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return results
    
