import datetime
from peewee import *

DATABASE = SqliteDatabase('database.db')

class BaseModel(Model):

    class Meta():
        database = DATABASE

# define model
# class Account(Resource):
# 	def get(self):
# 		return {"name": "juang"}

# 	def put(self):
# 		accounts[id] = request.form['account']
# 		return {'name': accounts[id]}


class Message(BaseModel):

    text = TextField()
    created_at = DateTimeField(default=datetime.datetime.now())

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Message], safe = True)
    DATABASE.close