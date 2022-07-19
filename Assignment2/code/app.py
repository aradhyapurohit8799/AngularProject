from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.products import DailySales
from resources.products import ItemList
from resources.sales import TotalSales
from resources.sales import averagesales
from resources.sales import totalsalesvalue
from resources.sales import uniquecustomer
from resources.user import UserRegister
from security import authenticate
from security import identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
app.secret_key = "Aradhya@8799"


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(DailySales, "/Daily Sales/<string:product_id>")
api.add_resource(totalsalesvalue, "/Total Sales Value")
api.add_resource(uniquecustomer, "/Unique")
api.add_resource(averagesales, "/AVG")
api.add_resource(ItemList, "/Daily Sales")
api.add_resource(TotalSales, "/total sales/<int:userid>")
api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
