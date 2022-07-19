from db import db


class DailySalesModel(db.Model):
    __tablename__ = "dailysales"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.String(80))
    description = db.Column(db.String(80))

    def __init__(self, id, product_id, description):

        self.id = id
        self.product_id = product_id
        self.description = description

    def json(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "description": self.description,
        }

    @classmethod
    def find_by_product_id(cls, product_id):
        return cls.query.filter_by(product_id=product_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
