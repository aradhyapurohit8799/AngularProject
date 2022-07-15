from db import db


class UniqueCustModel(db.Model):
    __tablename__ = "unique-customer"

    name = db.Column(db.String(80), primary_key=True)
    uniquecust = db.Column(db.Integer)

    def __init__(self, name, uniquecust):
        self.name = name
        self.uniquecust = uniquecust

    def json(self):
        return {"name": self.name, "uniquecust": self.uniquecust}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
