import numpy as np
from flask_jwt import jwt_required
from flask_restful import Resource
from Models.charts import chartsModel


class ageCountPlot(Resource):
    @jwt_required()
    def get(self):
        mainList = []
        age = chartsModel.AgeCountPlot()
        for data in age:
            mainList.append(data[0])
        category, value = np.unique(mainList, return_counts=True)
        return {"age": category.tolist(), "count": value.tolist()}


class bmivschargesScatterPlot(Resource):
    @jwt_required()
    def get(self):
        mainList = []
        bmicharge = chartsModel.BMIChargeScatterPlot()
        for data in bmicharge:
            mainList.append((data[0], data[1]))
        # print(mainList)
        return {"bmiCharge": mainList}


class childrenCountPlot(Resource):
    @jwt_required()
    def get(self):
        mainList = []
        children = chartsModel.ChildrenCountPlot()
        for data in children:
            mainList.append(data[0])
        category, value = np.unique(mainList, return_counts=True)
        return {"children": category.tolist(), "count": value.tolist()}


class smokerPieChart(Resource):
    @jwt_required()
    def get(self):
        mainList = []
        smoker = chartsModel.SmokerPieChart()
        for data in smoker:
            mainList.append(data[0])
        category, value = np.unique(mainList, return_counts=True)
        return {"smoker": category.tolist(), "count": value.tolist()}


class malevsfemalePieChart(Resource):
    @jwt_required()
    def get(self):
        mainList = []
        sex = chartsModel.SexPieChart()
        for data in sex:
            mainList.append(data[0])
        category, value = np.unique(mainList, return_counts=True)
        return {"sex": category.tolist(), "count": value.tolist()}
