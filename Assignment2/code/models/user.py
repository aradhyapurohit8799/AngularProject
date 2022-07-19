from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    def __init__(self, id, firstname, lastname, username, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()
