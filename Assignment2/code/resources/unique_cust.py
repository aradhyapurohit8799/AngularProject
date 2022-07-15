from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from models.unique_cust import UniqueCustModel


class UniqueCust(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="name field cannot be left blank",
    )
    parser.add_argument(
        "uniquecust",
        type=str,
        required=True,
        help="name field cannot be left blank",
    )

    @jwt_required()
    def get(self, name):
        item = UniqueCustModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 400

    # def post(self, name):
    #     if UniqueCustModel.find_by_name(name):
    #         return {
    #             "message": "an item with the name {} already exists".format(
    #                 name
    #             )
    #         }, 400
    #     data = UniqueCust.parser.parse_args()
    #     item = UniqueCustModel(data["value"])

    #     try:
    #         item.save_to_db()

    #     except:
    #         return {"message": "an error occured inserting the item"}, 500

    #     return item.json(), 201

    # def delete(self, name):
    #     item = UniqueCustModel.find_by_name(name)
    #     if item:
    #         item.delete_from_db()
    #     return {"message": "Item deleted"}

    def put(self, name):
        data = UniqueCust.parser.parse_args()

        item = UniqueCustModel.find_by_name(name)
        if item is None:
            item = UniqueCustModel(data["name"], data["uniquecust"])
        else:
            item.name = data["name"]
            item.uniquecust = data["uniquecust"]

        item.save_to_db()
        return item.json()
