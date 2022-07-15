from db import db


class DailySalesModel(db.Model):
    __tablename__ = "dailysales"

    pid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    salesamount = db.Column(db.Integer)
    profitpercent = db.Column(db.Float(precision=2))

    def __init__(self, pid, description, salesamount, profitpercent):
        self.pid = pid
        self.description = description
        self.salesamount = salesamount
        self.profitpercent = profitpercent

    def json(self):
        return {
            "pid": self.pid,
            "description": self.description,
            "salesamount": self.salesamount,
            "profitpercent": self.profitpercent,
        }

    @classmethod
    def find_by_pid(cls, pid):
        return cls.query.filter_by(pid=pid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
