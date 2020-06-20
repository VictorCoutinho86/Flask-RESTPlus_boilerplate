import uuid
from datetime import datetime

from app.main import db
from app.main.model.user import User

def save_new_user(data):
    user = get_a_user_by_email(data['email'])
    if not user:
        new_user = User(
            public_id = str(uuid.uuid4()),
            email = data['email'].lower(),
            username = data['username'],
            password = data['password'],
            registered_on = datetime.utcnow()
        )

        save_changes(new_user)

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.'
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user_by_public_id(public_id):
    return User.query.filter_by(public_id=public_id).first()


def get_a_user_by_email(email):
    return User.query.filter_by(email=email.lower()).first()


def get_a_user_by_username(username):
    return User.query.filter_by(username=username).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()