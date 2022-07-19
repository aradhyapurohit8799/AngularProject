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
        return {
            "Total Sales": sum(
                TotalSalesModel.find_by_date(str(date.today()))[0]
            )
        }


class uniquecustomer(Resource):
    def get(self):
        return {
            "unique cutomers": len(
                TotalSalesModel.find_by_date(str(date.today()))[1]
            )
        }


class averagesales(Resource):
    def get(self):
        total_amnt = sum(TotalSalesModel.find_by_date(str(date.today()))[0])
        unique_cust = len(TotalSalesModel.find_by_date(str(date.today()))[1])
        return {"Average Sales": total_amnt / unique_cust}
