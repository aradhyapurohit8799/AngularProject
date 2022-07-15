from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from models.avg_sales import AvgSalesModel


class AvgSales(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="name field cannot be left blank",
    )
    parser.add_argument(
        "avgsales",
        type=str,
        required=True,
        help="name field cannot be left blank",
    )

    @jwt_required()
    def get(self, name):
        item = AvgSalesModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 400

    def post(self, name):
        if AvgSalesModel.find_by_name(name):
            return {
                "message": "an item with the name {} already exists".format(
                    name
                )
            }, 400
        data = AvgSales.parser.parse_args()
        item = AvgSalesModel(data["avgsales"])

        try:
            item.save_to_db()

        except:
            return {"message": "an error occured inserting the item"}, 500

        return item.json(), 201

    def delete(self, name):
        item = AvgSalesModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}

    def put(self, name):
        data = AvgSales.parser.parse_args()

        item = AvgSalesModel.find_by_name(name)
        if item is None:
            item = AvgSalesModel(data["name"], data["avgsales"])
        else:
            item.avgsales = data["avgsales"]

        item.save_to_db()
        return item.json()