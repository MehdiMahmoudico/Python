from flask_app.config.mysqlconnection import  connectToMySQL , DB
from flask_app.models.dojo import Dojo
class Ninja :
    def __init__(self, data) :
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data ["dojo_id"]
        


    @classmethod
    def get_by_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(id)s"
        results = connectToMySQL(DB).query_db(query,data)
        if results == []:
            return []
        ninja = []
        for i in results:
            n = {
                'id': i['ninjas.id'],
                'firstname': i['firstname'],
                'lastname': i['lastname'],
                'age': i['age'],
                'created_at': i['ninjas.created_at'],
                'updated_at': i['ninjas.updated_at'],
                'dojo_id': i['dojo_id']

            }
            ninja.append(cls(n))
        return ninja

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
    

