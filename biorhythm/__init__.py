from distutils.log import debug
from flask import Flask
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
SESSION_SECRET = os.getenv("SESSION_SECRET")

app = Flask(__name__)

app.config["SECRET_KEY"] = SESSION_SECRET
app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)
Bootstrap(app)
datepicker(app=app, local=['static/js/jquery-ui.js', 'static/css/jquery-ui.css'])

import biorhythm.views.views
import biorhythm.views.dashboardView
import biorhythm.views.createEventView

