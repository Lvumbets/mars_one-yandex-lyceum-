import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Colonist(SqlAlchemyBase):
    __tablename__ = 'colonists'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)

    jobs = orm.relationship("Jobs", back_populates='user')
    departments = orm.relationship('Department', back_populates='user')

    def __repr__(self):
        return '{surname} {name}'.format(surname=self.surname, name=self.name)
