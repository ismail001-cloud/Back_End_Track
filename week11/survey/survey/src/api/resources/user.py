from flask import request, jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from src.db.models.user import User
from src.db.core import db

# Create blueprint for users routes
users_bp = Blueprint('users', __name__)
api = Api(users_bp)

class UserList(Resource):
    def get(self, user_id):
        """Retrieve a specific user by ID"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return jsonify(user.serialize())

   
    def put(self, user_id):
        """Update an existing user"""
        data = request.get_json()
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        if "name" in data:
            if User.query.filter_by(name=data["name"]).first():
                return {"message": "User name already exists"}, 400
            user.name = data["name"]

        db.session.commit()
        return jsonify({"message": "User updated successfully", "user": user.serialize()})

    def delete(self, user_id):
        """Delete a user"""
        user = User.query.get(user_id)

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200

class UserResource(Resource):
    def get(self):
        """Retrieve all users"""
        users = User.query.all()
        return {"users": [user.serialize() for user in users]}, 200
    
    def post(self):
        """Create a new user"""
        data = request.get_json()
        if not data or 'name' not in data:
            return {"message": "Please insert a name"}, 400

        if User.query.filter_by(name=data['name']).first():
            return {"message": "User name already exists"}, 400

        new_user = User(name=data["name"])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully", "user": new_user.serialize()}), 201


# Register resources with distinct endpoints
api.add_resource(UserList, '/users/<int:user_id>')
api.add_resource(UserResource, '/users')