from datetime import date

from db import db


class TotalSalesModel(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(
        db.String(80), db.ForeignKey("dailysales.product_id")
    )
    sales_amount = db.Column(db.Integer)
    sales_date = db.Column(db.String(80), default=str(date.today()))

    def __init__(self, id, userid, product_id, sales_amount, sales_date):
        self.id = id
        self.userid = userid
        self.product_id = product_id
        self.sales_amount = sales_amount
        self.sales_date = sales_date

    def json(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "product_id": self.product_id,
            "sales_amount": self.sales_amount,
            "sales_date": self.sales_date,
        }

    @classmethod
    def find_by_date(cls, sales_date):

        mainlist = []

        mylist = []
        list2 = cls.query.filter_by(sales_date=sales_date).all()

        for item in list2:
            mylist.append(item.sales_amount)

        myset = set()
        for item in list2:
            myset.add(item.userid)

        mainlist.append(mylist)
        mainlist.append(myset)

        return mainlist

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(userid=userid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
