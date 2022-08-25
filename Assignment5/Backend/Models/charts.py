from db import db


class chartsModel(db.Model):
    __tablename__ = "insurance"

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(80))
    bmi = db.Column(db.Float)
    children = db.Column(db.Integer)
    smoker = db.Column(db.String(80))
    region = db.Column(db.String(800))
    charges = db.Column(db.Float)

    def __init__(self, age, sex, bmi, children, smoker, region, charges):

        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges

    @classmethod
    def AgeCountPlot(cls):

        ageResult = cls.query.with_entities(chartsModel.age).all()

        return ageResult

    @classmethod
    def BMIChargeScatterPlot(cls):

        bmichargeResult = cls.query.with_entities(
            chartsModel.bmi, chartsModel.charges
        ).all()

        return bmichargeResult

    @classmethod
    def ChildrenCountPlot(cls):

        childrenResult = cls.query.with_entities(chartsModel.children).all()

        return childrenResult

    @classmethod
    def SexPieChart(cls):

        sexResult = cls.query.with_entities(chartsModel.sex).all()

        return sexResult

    @classmethod
    def SmokerPieChart(cls):

        smokerResult = cls.query.with_entities(chartsModel.smoker).all()

        return smokerResult
