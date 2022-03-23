from flask import Flask
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask import Flask

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
SESSION_SECRET = os.getenv("SESSION_SECRET")

app = Flask(__name__)

app.config["SECRET_KEY"] = SESSION_SECRET
app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)

import biorhythm.views.registerView
import biorhythm.views.dashboardView
import biorhythm.views.createEventView
import biorhythm.views.friendRequestView
import biorhythm.views.findUsersView
import biorhythm.views.loginView
import biorhythm.views.logoutView
import biorhythm.views.views
