from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://172.31.16.148:27017/myDatabase"
mongo = PyMongo(app)


def get_cases_by_location(lat, lon):
    try:
        lat = round(float(lat), 1)
        lon = round(float(lon), 1)
        return mongo.db.cases.find(
            {lat: lat, lon: lon})
    except ValueError:
        return None
