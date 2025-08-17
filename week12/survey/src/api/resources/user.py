from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from flask import Blueprint
from src.db.models.user import User
from src.db.core import db
from werkzeug.security import generate_password_hash, check_password_hash

#  create blueprint for users routes
users_bp = Blueprint('users', __name__)
api = Api(users_bp)

#userparser for posting
Userparser = reqparse.RequestParser()
Userparser.add_argument('first_name', type=str, required=True, help='first name is required')
Userparser.add_argument('last_name', type=str)
Userparser.add_argument('email', type=str, required=True, help='email is required')
Userparser.add_argument('phone', type=str, help='phone number is missing')
Userparser.add_argument('address', type=str, help='address is missing')
Userparser.add_argument('password', type=str, required=True, help='insert password')
Userparser.add_argument('role', type=str, default='USER')


class UserList(Resource):

    def get(self, user_id):
        """retrieve a specific user by ID"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'address': user.address,
            'role': user.role.name
        }
        return jsonify({'user':user_data})

# to get all
class UserResource(Resource):
    """handle collection of sections"""
    def get(self):
        """retrieve all users"""
        users = User.query.all()
        if not users:
            return {"message": "No users found", "users":[]}, 404
        
        return ([user.serialize() for user in users]), 200

    def post(self):
        """create new section for user"""
        args = Userparser.parse_args()
        hashed_password = generate_password_hash(args['password'])
        new_user = User(
            first_name=args['first_name'],
            last_name=args['last_name'],
            email=args['email'],
            phone=args['phone'],
            password=hashed_password,
            address=args['address']
        )

        if User.query.filter_by(email=new_user.email). first():
            return {"message": "user with the provided details already exists"}, 400

        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully", "user":{'id':new_user.id, 'first_name':new_user.first_name}}, 201

# Register resources with distinct endpoints
api.add_resource(UserResource, '/users')
api.add_resource(UserList, '/users/<int:user_id>')