from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from models.products import DailySalesModel


class DailySales(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id",
        type=int,
        help="id field cannot be left blank",
    )
    parser.add_argument(
        "product_id",
        type=str,
        help="product_id field cannot be left blank",
    )
    parser.add_argument(
        "description",
        type=str,
        required=True,
        help="description field cannot be left blank",
    )

    @jwt_required()
    def get(self, product_id):
        item = DailySalesModel.find_by_product_id(product_id)
        if item:
            return item.json()
        return {"message": "Item not found"}, 400

    def post(self, product_id):
        if DailySalesModel.find_by_product_id(product_id):
            return {
                "message": "an item with the name {} already exists".format(
                    product_id
                )
            }, 400
        data = DailySales.parser.parse_args()
        item = DailySalesModel(data["id"], product_id, data["description"])

        try:
            item.save_to_db()

        except:
            return {"message": "an error occured inserting the item"}, 500

        return item.json(), 201

    def delete(self, product_id):
        item = DailySalesModel.find_by_product_id(product_id)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}

    def put(self, product_id):
        data = DailySales.parser.parse_args()

        item = DailySalesModel.find_by_product_id(product_id)
        if item is None:
            item = DailySalesModel(
                data["id"],
                data["product_id"],
                data["description"],
            )
        else:
            data["id"],
            item.product_id = data["product_id"]
            item.description = data["description"]

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [x.json() for x in DailySalesModel.query.all()]}
