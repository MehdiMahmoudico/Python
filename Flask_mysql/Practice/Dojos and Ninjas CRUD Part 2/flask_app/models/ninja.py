from flask_app.config.mysqlconnection import  connectToMySQL , DB

class Ninja :
    def __init__(self, data) :
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data) :
        query = "INSERT INTO ninjas (firstname,lastname,age,dojo_id) VALUES (%(firstname)s, %(lastname)s, %(age)s,%(dojo_id)s);"
        return connectToMySQL(DB).query_db(query, data)
    

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results == []:
            return []
        return results[0]
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET firstname = %(firstname)s, lastname = %(lastname)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)