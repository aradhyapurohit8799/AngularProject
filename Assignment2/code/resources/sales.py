import sqlite3
from datetime import date

from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from models.sales import TotalSalesModel


class TotalSales(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "id",
        type=int,
        help="This field cannot be left blank",
    )
    parser.add_argument(
        "userid",
        type=int,
        help="This field cannot be left blank",
    )
    parser.add_argument(
        "product_id",
        type=str,
        required=True,
        help="This field cannot be left blank",
    )
    parser.add_argument(
        "sales_amount",
        type=int,
        required=True,
        help="This field cannot be left blank",
    )
    parser.add_argument(
        "sales_date",
        type=str,
        help="This field cannot be left blank",
    )

    @jwt_required()
    def get(self, userid):
        item = TotalSalesModel.find_by_userid(userid)
        if item:
            return {"Items": [x.json() for x in TotalSalesModel.query.all()]}
        return {"message": "Item not found"}, 400

    def post(self, userid):
        data = TotalSales.parser.parse_args()

        item = TotalSalesModel(
            data["id"],
            userid,
            data["product_id"],
            data["sales_amount"],
            data["sales_date"],
        )

        item.save_to_db()
        return item.json()


class totalsalesvalue(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = (
            "SELECT SUM(sales_amount) FROM sales WHERE sales_date == DATE();"
        )
        result = cursor.execute(query)
        row = result.fetchone()
        connection.close()
        if row:
            return {"total sales": row[0]}


class uniquecustomer(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT COUNT (DISTINCT(userid)) FROM sales WHERE sales_date == DATE();"
        result = cursor.execute(query)
        row = result.fetchone()
        connection.close()
        if row:
            return {"unique": row[0]}


class averagesales(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query1 = (
            "SELECT SUM(sales_amount) FROM sales WHERE sales_date == DATE();"
        )
        result1 = cursor.execute(query1)
        row1 = result1.fetchone()

        query2 = "SELECT COUNT (DISTINCT(userid)) FROM sales WHERE sales_date == DATE();"
        result2 = cursor.execute(query2)
        row2 = result2.fetchone()

        print(row1[0])
        print(row2[0])

        print(date.today())

        connection.close()
        if row1 and row2:
            return {"average customers": row1[0] / row2[0]}
