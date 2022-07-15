from db import db


class AvgSalesModel(db.Model):
    __tablename__ = "avgsales"

    name = db.Column(db.String(80), primary_key=True)
    avgsales = db.Column(db.String(80))

    def __init__(self, name, avgsales):
        self.name = name
        self.avgsales = avgsales

    def json(self):
        return {"name": self.name, "avgsales": self.avgsales}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
