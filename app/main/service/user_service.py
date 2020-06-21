import uuid
from datetime import datetime

from app.main import db
from app.main.model.user import User

def save_new_user(data):
    user = get_a_user_by_email(data['email'].lower())
    if not user:
        new_user = User(
            public_id = str(uuid.uuid4()),
            email = data['email'].lower(),
            username = data['username'],
            password = data['password'],
            registered_on = datetime.utcnow()
        )

        save_changes(new_user)

        generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.'
        }
        return response_object, 409


def get_all_users():
    users = User.query.all()
    for user in users:
        print(user.email)
    return users


def get_a_user_by_public_id(public_id):
    return User.query.filter_by(public_id=public_id).first()


def get_a_user_by_email(email):
    return User.query.filter_by(email=email.lower()).first()


def get_a_user_by_username(username):
    return User.query.filter_by(username=username).first()

def generate_token(user):
    try:
        auth_token = user.encode_auth_token()
        response_object = {
            'status': 'success',
            'message': 'Successfully registered',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401 

def save_changes(data):
    db.session.add(data)
    db.session.commit()