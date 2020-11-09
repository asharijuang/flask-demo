from flask import jsonify, Blueprint
from flask_restful import Resource, Api

import models

class MessageList(Resource):
    def get(self):

        messages = {}
        query = models.Message.select()

        for row in query:
            messages[row.id] = {'content': row.text,
                                'created_at': row.created_at}

        return jsonify({'messages': [messages]})
    
class Message(Resource):
    def get(self, id):
        message = models.Message.get_by_id(id)
        return jsonify({'message': message.text})

messages_api = Blueprint('resources.messages', __name__)
api = Api(messages_api)

api.add_resource(MessageList, '/messages', endpoint='messages')
api.add_resource(Message, '/message/<int:id>', endpoint='message')