from distutils.log import debug
import os
from flask import Flask
from flask_pymongo import PyMongo


MONGO_URL = os.getenv("MONGO_URL")
SESSION_SECRET = os.getenv("SESSION_SECRET")

app = Flask(__name__)
app.config["SECRET_KEY"] = SESSION_SECRET
app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)

if __name__=='__main__':
    app.run(debug = True)

import biorhythm.views