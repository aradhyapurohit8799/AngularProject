from db import db


class TotalSalesModel(db.Model):
    __tablename__ = "totalsales"

    name = db.Column(db.String(80), primary_key=True)
    totalsales = db.Column(db.String(80))

    def __init__(self, name, totalsales):
        self.name = name
        self.totalsales = totalsales

    def json(self):
        return {"name": self.name, "totalsales": self.totalsales}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
