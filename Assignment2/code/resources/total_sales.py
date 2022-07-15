from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from models.total_sales import TotalSalesModel


class TotalSales(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="name field cannot be left blank",
    )
    parser.add_argument(
        "totalsales",
        type=str,
        required=True,
        help="This field cannot be left blank",
    )

    @jwt_required()
    def get(self, name):
        item = TotalSalesModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 400

    def put(self, name):
        data = TotalSales.parser.parse_args()

        item = TotalSalesModel.find_by_name(name)
        if item is None:
            item = TotalSalesModel(data["name"], data["totalsales"])
        else:
            item.name = data["name"]
            item.totalsales = data["totalsales"]

        item.save_to_db()
        return item.json()
