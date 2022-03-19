from biorhythm import mongo
from bson import ObjectId
from datetime import datetime

db = mongo.db


class User(db.Model):
    id = db.Colum(db.Integer, primary_key = True)
    username = db.Colum(db.String(20), unique = True, nullable = False)
    birthdate = db.Colum(db.Date)
    email = db.Colum(db.String(128), unique = True. nullable = False)
    image_file = db.Colum(db.String(20), nullable = False, default = "default.jpg")
    password  = db.Column(db.String(20), nullable = False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)