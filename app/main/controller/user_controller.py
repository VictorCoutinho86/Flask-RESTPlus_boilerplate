from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user_by_email, get_a_user_by_public_id, get_a_user_by_username


api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('List all registered users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created')
    @api.doc('Create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Create a new user"""
        data = request.json
        return save_new_user(data=data)


@api.route('/public_id/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found')
class UserPublicId(Resource):
    @api.doc('Get a user by public_id')
    @api.marshal_with(_user)
    def get(self, public_id):
        """Get a user by public_id"""
        user = get_a_user_by_public_id(public_id)
        if not user:
            api.abort(404, status='fail', message='User not found')
        else:
            return user


@api.route('/email/<email>')
@api.param('email', 'The User email')
@api.response(404, 'User not found')
class UserEmail(Resource):
    @api.doc('Get a user by email')
    @api.marshal_with(_user)
    def get(self, email):
        """Get a user by email"""
        user = get_a_user_by_email(email)
        if not user:
            api.abort(404, status='fail', message='User not found')
        else:
            return user


@api.route('/username/<username>')
@api.param('username', 'The User username')
@api.response(404, 'User not found')
class UserUsername(Resource):
    @api.doc('Get a user by username')
    @api.marshal_with(_user)
    def get(self, username):
        """Get a user by username"""
        user = get_a_user_by_username(username)
        if not user:
            api.abort(404, status='fail', message='User not found')
        else:
            return user
