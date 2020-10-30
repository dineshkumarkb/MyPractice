from flask import Flask
from flask_restful import Resource,Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Emp(Resource):

    def get(self):

        conn = db_connect.connect()
        query = conn.execute("select * from employees")
        return {'employees': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(Emp, '/employees')

if __name__ == "__main__":
    app.run(port=5002)