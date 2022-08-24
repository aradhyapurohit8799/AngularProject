from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_restful import Api

from Resources.charts import ageCountPlot
from Resources.charts import bmivschargesScatterPlot
from Resources.charts import childrenCountPlot
from Resources.charts import malevsfemalePieChart
from Resources.charts import smokerPieChart
from Resources.user import UserRegister
from security import authenticate
from security import identity

app = Flask(__name__)
CORS(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///insurance.db"  # Telling SQLAlchemy about insurance database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
app.secret_key = "Aradhya@8799"


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(ageCountPlot, "/acPlot")
api.add_resource(bmivschargesScatterPlot, "/bcScatterPlot")
api.add_resource(childrenCountPlot, "/cCountPlot")
api.add_resource(smokerPieChart, "/smokerPieChart")
api.add_resource(malevsfemalePieChart, "/mvsfPieChart")
api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    import sqlite3
    from pathlib import Path

    import pandas as pd

    from db import db

    Path("insurance.db").touch()  # Making an emopty insurance database file

    connection = sqlite3.connect("insurance.db")
    cursor = connection.cursor()

    insurance = pd.read_csv("Dataset/insurance.csv")
    insurance.to_sql(
        "insurance", connection, if_exists="replace", index=False
    )  # making an insurance table inside insurance database

    connection.commit()
    connection.close()
    db.init_app(app)
    app.run(port=5000, debug=True)
