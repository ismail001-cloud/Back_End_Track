from flask import request, jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from src.api.controllers import auth
from src.db.core import db

# Create blueprint for auth routes
auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

class Auth(Resource):
    def get(self):
        '''get single authentication'''
        auth = Auth.query.all()
        return {"users": [auth.serialize() for auth in auth]}, 200

    def post(self):
        '''get all authentication'''
        data = request.get_json()
        auth = Auth.query.filter_by(name=data['authentication']).first()
        if not auth or not auth.check_password(data['password']):
            return {"message": "Invalid username or password"}, 401


# Register the Auth resource
api.add_resource(Auth, '/auth')