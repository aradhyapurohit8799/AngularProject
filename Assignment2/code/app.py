from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.avg_sales import AvgSales
from resources.daily_sales import DailySales
from resources.daily_sales import ItemList
from resources.total_sales import TotalSales
from resources.unique_cust import UniqueCust
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


api.add_resource(DailySales, "/Daily Sales/<int:pid>")
api.add_resource(ItemList, "/Daily Sales")
api.add_resource(TotalSales, "/total sales/<string:name>")
api.add_resource(AvgSales, "/avg sales/<string:name>")
api.add_resource(UniqueCust, "/unique cust/<string:name>")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
