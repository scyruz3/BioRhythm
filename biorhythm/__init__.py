from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
SESSION_SECRET = os.getenv("SESSION_SECRET")

app = Flask(__name__)

app.config["SECRET_KEY"] = SESSION_SECRET

import biorhythm.views
import biorhythm.dashboard
