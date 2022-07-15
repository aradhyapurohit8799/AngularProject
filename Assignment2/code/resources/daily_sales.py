from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from models.daily_sales import DailySalesModel


class DailySales(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "pid",
        type=int,
        required=True,
        help="pid field cannot be left blank",
    )
    parser.add_argument(
        "description",
        type=str,
        required=True,
        help="description field cannot be left blank",
    )
    parser.add_argument(
        "salesamount",
        type=str,
        required=True,
        help="sales amount field cannot be left blank",
    )
    parser.add_argument(
        "profitpercent",
        type=float,
        required=True,
        help="profit percent field cannot be left blank",
    )

    @jwt_required()
    def get(self, pid):
        item = DailySalesModel.find_by_pid(pid)
        if item:
            return item.json()
        return {"message": "Item not found"}, 400

    def post(self, pid):
        if DailySalesModel.find_by_pid(pid):
            return {
                "message": "an item with the name {} already exists".format(
                    pid
                )
            }, 400
        data = DailySales.parser.parse_args()
        item = DailySalesModel(
            data["pid"],
            data["description"],
            data["salesamount"],
            data["profitpercent"],
        )

        try:
            item.save_to_db()

        except:
            return {"message": "an error occured inserting the item"}, 500

        return item.json(), 201

    def delete(self, pid):
        item = DailySalesModel.find_by_pid(pid)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}

    def put(self, pid):
        data = DailySales.parser.parse_args()

        item = DailySalesModel.find_by_pid(pid)
        if item is None:
            item = DailySalesModel(
                data["pid"],
                data["description"],
                data["salesamount"],
                data["profitpercent"],
            )
        else:
            item.description = data["description"]
            item.salesamount = data["salesamount"]
            item.profitpercent = data["profitpercent"]

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [x.json() for x in DailySalesModel.query.all()]}
