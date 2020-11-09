from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

from resources.messages import messages_api

import models

app = Flask(__name__)
app.register_blueprint(messages_api, url_prefix='/api/v1')


if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)
