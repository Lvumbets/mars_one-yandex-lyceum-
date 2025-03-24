from flask import jsonify
from flask_restful import Resource, abort

from . import db_session
from .user_regparser import parser
from .users import User


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('name', 'surname', 'age', 'position', 'speciality', 'address', 'email')) for item in users]})

    def post(self):
        args = parser.parse_args()
        if args['password'] != args['password_again']:
            abort(404, message="Пароли не совпадают!")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == args['email']).first():
            abort(404, message="Такой пользователь уже есть!")

        user = User(
            name=args['name'],
            email=args['email'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address']
        )
        user.set_password(args.password.data)
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'id': user.id})
