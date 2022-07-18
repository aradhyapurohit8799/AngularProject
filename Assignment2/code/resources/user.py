from flask_restful import Resource
from flask_restful import reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id",
        type=int,
        required=True,
        help="This field can't be left blanck",
    )
    parser.add_argument(
        "firstname",
        type=str,
        required=True,
        help="This field can't be left blanck",
    )
    parser.add_argument(
        "lastname",
        type=str,
        required=True,
        help="This field can't be left blanck",
    )
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field can't be left blanck",
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field can't be left blanck",
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "User with this user name already exists"}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
