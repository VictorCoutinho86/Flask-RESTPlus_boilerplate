from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """User login resource"""

    @api.doc('User login')
    @api.expect(user_auth, validate=True)
    def post(self):
        data = request.json
        return Auth.login_user(data)
    

@api.route('/logout')
class UserLogout(Resource):
    """User logout resource"""

    @api.doc('User logout')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(auth_header)